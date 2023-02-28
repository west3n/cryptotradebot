from aiogram import Dispatcher, types
from keyboards import inline, reply
from datetime import datetime, timedelta
import database.mysql.user as mysql


async def subscribe_description(call: types.CallbackQuery):
    await call.message.delete()
    user_id = call.from_user.id
    user = await mysql.status(user_id)
    if user:
        await call.message.answer(text=f"<b>Цена бота</b>:\n<b>Basic:</b> 139$/месяц\n"
                                       f"<b>Advanced</b>: 379$/месяц\n\n"
                                       f"<b>Exchanges Basic</b>: Bybit+Futures, Poloniex, Exmo, "
                                       f"Bittrex, Kucoin, OKX, Huobi, MXC, Gate, HitBTC\n\n"
                                       f"<b>Exchanges Advanced</b>: Binance+futures, BinanceUS, "
                                       f"Coinbase, Kraken, Kucoin Futures Bitfinex",
                                  reply_markup=inline.kb_subscribe_old())

    else:
        await call.message.answer(text=f"<b>Бесплатное тестирование предоставляется на 14 дней</b>\n\n"
                                       f"<b>Цена бота</b>:\n<b>Basic:</b> 139$/месяц\n"
                                       f"<b>Advanced</b>: 379$/месяц\n\n"
                                       f"<b>Exchanges Basic</b>: Bybit+Futures, Poloniex, Exmo, "
                                       f"Bittrex, Kucoin, OKX, Huobi, MXC, Gate, HitBTC\n\n"
                                       f"<b>Exchanges Advanced</b>: Binance+futures, BinanceUS, "
                                       f"Coinbase, Kraken, Kucoin Futures Bitfinex",
                                  reply_markup=inline.kb_subscribe_description())


async def pay_basic(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text='Выберите вариант подписки:',
                              reply_markup=inline.kb_pay_basic())


async def pay_advanced(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text='Выберите вариант подписки:',
                              reply_markup=inline.kb_pay_advanced())


async def handle_callback_query(call: types.CallbackQuery):
    subscribe = None
    subscribe_start = None
    subscribe_finish = None
    user_id = call.from_user.id

    if call.data == 'free_sub':
        await call.message.delete()
        await call.message.answer('Пробная подписка активирована.',
                                  reply_markup=reply.start_keyboard())
        subscribe = 'Free'
        subscribe_start = datetime.now().strftime("%d.%m.%Y")
        subscribe_finish = (datetime.now() + timedelta(days=14)).strftime("%d.%m.%Y")
    elif call.data == 'pay_basic_30':
        await call.message.delete()
        await call.message.answer('Подписка Basic на 30 дней активирована.')
        subscribe = 'Basic'
        subscribe_start = datetime.now().strftime("%d.%m.%Y")
        subscribe_finish = (datetime.now() + timedelta(days=30)).strftime("%d.%m.%Y")
    elif call.data == 'pay_basic_90':
        await call.message.delete()
        await call.message.answer('Подписка Basic на 90 дней активирована.')
        subscribe = 'Basic'
        subscribe_start = datetime.now().strftime("%d.%m.%Y")
        subscribe_finish = (datetime.now() + timedelta(days=90)).strftime("%d.%m.%Y")
    elif call.data == 'pay_basic_180':
        await call.message.delete()
        await call.message.answer('Подписка Basic на 180 дней активирована.')
        subscribe = 'Basic'
        subscribe_start = datetime.now().strftime("%d.%m.%Y")
        subscribe_finish = (datetime.now() + timedelta(days=180)).strftime("%d.%m.%Y")
    elif call.data == 'pay_basic_365':
        await call.message.delete()
        await call.message.answer('Подписка Basic на 365 дней активирована.')
        subscribe = 'Basic'
        subscribe_start = datetime.now().strftime("%d.%m.%Y")
        subscribe_finish = (datetime.now() + timedelta(days=365)).strftime("%d.%m.%Y")
    elif call.data == 'pay_advanced_30':
        await call.message.delete()
        await call.message.answer('Подписка Advanced на 30 дней активирована.')
        subscribe = 'Advanced'
        subscribe_start = datetime.now().strftime("%d.%m.%Y")
        subscribe_finish = (datetime.now() + timedelta(days=30)).strftime("%d.%m.%Y")
    elif call.data == 'pay_advanced_90':
        await call.message.delete()
        await call.message.answer('Подписка Advanced на 90 дней активирована.')
        subscribe = 'Advanced'
        subscribe_start = datetime.now().strftime("%d.%m.%Y")
        subscribe_finish = (datetime.now() + timedelta(days=90)).strftime("%d.%m.%Y")
    elif call.data == 'pay_advanced_180':
        await call.message.delete()
        await call.message.answer('Подписка Advanced на 180 дней активирована.')
        subscribe = 'Advanced'
        subscribe_start = datetime.now().strftime("%d.%m.%Y")
        subscribe_finish = (datetime.now() + timedelta(days=180)).strftime("%d.%m.%Y")
    elif call.data == 'pay_advanced_365':
        await call.message.delete()
        await call.message.answer('Подписка Advanced на 365 дней активирована.')
        subscribe = 'Advanced'
        subscribe_start = datetime.now().strftime("%d.%m.%Y")
        subscribe_finish = (datetime.now() + timedelta(days=365)).strftime("%d.%m.%Y")
    await mysql.subscription(user_id, subscribe, subscribe_start, subscribe_finish)


def register(dp: Dispatcher):
    dp.register_callback_query_handler(subscribe_description, text='subscribe')
    dp.register_callback_query_handler(pay_basic, text='pay_basic')
    dp.register_callback_query_handler(pay_advanced, text='pay_advanced')
    dp.register_callback_query_handler(handle_callback_query, text=[
        'free_sub', 'pay_basic_30', 'pay_basic_90', 'pay_basic_180', 'pay_basic_365',
        'pay_advanced_30', 'pay_advanced_90', 'pay_advanced_180', 'pay_advanced_365'])
