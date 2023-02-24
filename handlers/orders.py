import sqlite3

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from keyboards import inline
from config.states import ApiConnector
from database.sqlite import user, user_exchange

callback_data = ['bybit', 'bittrex', 'huobi', 'poloniex', 'exmo',
                 'kucoin', 'bitfinex', 'okx', 'mxc', 'kukoin_futures', 'gate',
                 'hitbtc', 'binance', 'kraken', 'coinbase']


async def api_main(call: types.CallbackQuery):
    user_id = call.from_user.id
    await call.message.delete()
    status = await user.status(user_id)
    print(str(status[1]))
    if str(status[1]) == 'Free':
        await call.message.answer(f'У вас подписка {status[1]}.\nВам доступны следующие биржы:',
                                  reply_markup=inline.api_main_basic())
        await ApiConnector.exc.set()
    if str(status[1]) == 'Basic':
        await call.message.answer(f'У вас подписка {status[1]}.\nВам доступны следующие биржы:',
                                  reply_markup=inline.api_main_basic())
        await ApiConnector.exc.set()
    if str(status[1]) == 'Advanced':
        await call.message.answer(f'У вас подписка {status[1]}.\nВам доступны следующие биржы:',
                                  reply_markup=inline.api_main_adv())
        await ApiConnector.exc.set()


async def api_step1(call: types.CallbackQuery, state: FSMContext):

    if call.data in callback_data:
        async with state.proxy() as data:
            data['exc'] = call.data
        await call.message.delete()
        await call.message.answer('Отправьте свой API_KEY от биржи:')
        await ApiConnector.next()
    else:
        await call.message.delete()
        await state.finish()


async def api_step2(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['api_key'] = msg.text
    await msg.answer('Отправьте свой API_SECRET от биржи:')
    await ApiConnector.next()


async def api_step3(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['api_secret'] = msg.text
    user_id = msg.from_user.id
    try:
        await user_exchange.add_exchange(user_id, data)
        await msg.answer('Данные успешно сохранены!')
        await state.finish()
    except sqlite3.IntegrityError:
        await state.finish()
        await msg.answer('У вас уже есть API этой биржи!')



def register(dp: Dispatcher):
    dp.register_callback_query_handler(api_main, text='connect_api')
    dp.register_callback_query_handler(api_step1, state=ApiConnector.exc)
    dp.register_message_handler(api_step2, state=ApiConnector.api_key)
    dp.register_message_handler(api_step3, state=ApiConnector.api_secret)
