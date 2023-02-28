import mysql.connector
from datetime import datetime, timedelta
import pybit.exceptions
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from keyboards import inline
from config.states import ApiConnector
from database.mysql import user, user_exchange
from parse import bybit, bittrex


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
    user_x = await user_exchange.api_key_status(user_id)
    status = await user.status(user_id)
    if not user_x and status[1] == 'Free':
        await msg.delete()
        subscribe = 'Free'
        subscribe_start = datetime.now().strftime("%d.%m.%Y")
        subscribe_finish = (datetime.now() + timedelta(days=14)).strftime("%d.%m.%Y")
        await user.subscription(user_id, subscribe, subscribe_start, subscribe_finish)
        await user_exchange.add_exchange(user_id, data)
        await msg.answer('Данные успешно сохранены!')
        await state.finish()
    else:
        try:
            await user_exchange.add_exchange(user_id, data)
            await msg.answer('Данные успешно сохранены!')
            await state.finish()
        except mysql.connector.errors.IntegrityError:
            await state.finish()
            await msg.answer('У вас уже есть API этой биржи!')


async def more_parse(call: types.CallbackQuery):
    user_id = call.from_user.id
    exc = call.data.split("_")[0]
    stat = await user_exchange.get_api(user_id, exc)
    if exc == 'bybit':
        try:
            x = bybit.connect_bybit(stat)
            await call.message.answer(f'Биржа: {str(exc).capitalize()}\n\n'
                                      f'Баланс:\n{x[0]}\n'
                                      f'У вас активных ордеров {8}\n'
                                      f'{str(exc).capitalize()} BTC/USDT:\nВход:\n'
                                      f'TP/SL: {x[1]}/{x[2]}\n',
                                      reply_markup=inline.cmd_close(data=f'{exc}_close'))
        except pybit.exceptions.InvalidRequestError:
            await call.message.answer(f'API_KEY {str(exc).capitalize()} введен некорректно',
                                      reply_markup=inline.delete_api_key(data=f'{exc}_delete_api'))

    if exc == 'bittrex':
        try:
            x = bittrex.bittrex_connect(stat)
            await call.message.answer(f'Биржа: {str(exc).capitalize()}\n\n'
                                      f'Баланс:\n{x[0]}\n'
                                      f'Активные ордера:\n{x[1]},',
                                      reply_markup=inline.cmd_close(data=f'{exc}_close'))
        except pybit.exceptions.InvalidRequestError:
            await call.message.answer(f'API_KEY {str(exc).capitalize()} введен некорректно',
                                      reply_markup=inline.delete_api_key(data=f'{exc}_delete_api'))

        except TypeError:
            await call.message.answer(f'API_KEY {str(exc).capitalize()} введен некорректно',
                                      reply_markup=inline.delete_api_key(data=f'{exc}_delete_api'))
    else:
        await call.message.answer('Функция в разработке.')


async def delete_api(call: types.CallbackQuery):
    await call.message.delete()
    exc = call.data.split("_")[0]
    user_id = call.from_user.id
    await user_exchange.delete_api(user_id, exc)
    await call.message.answer(f'API_KEY {str(exc).capitalize()} успешно удален')


async def exc_close(call: types.CallbackQuery):
    await call.message.delete()
    user_id = call.from_user.id
    exc = call.data.split("_")[0]
    stat = await user_exchange.get_api(user_id, exc)
    if exc == 'bybit':
        x = bybit.close_bybit(stat)
        if not x:
            x = 'Все активные ордера закрыты'
            await call.message.answer(f'{x}')
        else:
            await call.message.answer(f'{x}')
    if exc == 'bittrex':
        x = bittrex.cancel_all_orders(stat)
        await call.message.answer(f'{x}')


def register(dp: Dispatcher):
    for data in callback_data:
        dp.register_callback_query_handler(delete_api, text=f'{data}_delete_api')
        dp.register_callback_query_handler(more_parse, text=f'{data}_api')
        dp.register_callback_query_handler(exc_close, text=f'{data}_close')
    dp.register_callback_query_handler(api_main, text='connect_api')
    dp.register_callback_query_handler(api_step1, state=ApiConnector.exc)
    dp.register_message_handler(api_step2, state=ApiConnector.api_key)
    dp.register_message_handler(api_step3, state=ApiConnector.api_secret)
