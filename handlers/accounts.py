from aiogram import Dispatcher, types
from keyboards import inline
from datetime import datetime, timedelta
import database.sqlite.create as sqlite


async def subscribe_description(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="Подписка - открывает доступ к тому и тому",
                              reply_markup=inline.kb_subscribe_description())


async def free_sub(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text='Тестовая подписка активирована!')


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
        await call.message.answer('Пробная подписка активирована.')
        subscribe = 'Free'
        subscribe_start = datetime.now().strftime("%d.%m.%Y")
        subscribe_finish = (datetime.now() + timedelta(days=30)).strftime("%d.%m.%Y")
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
    await sqlite.subscription(user_id, subscribe, subscribe_start, subscribe_finish)


def register(dp: Dispatcher):
    dp.register_callback_query_handler(subscribe_description, text='subscribe')
    dp.register_callback_query_handler(pay_basic, text='pay_basic')
    dp.register_callback_query_handler(pay_advanced, text='pay_advanced')
    dp.register_callback_query_handler(handle_callback_query, text=[
                                         'free_sub', 'pay_basic_30', 'pay_basic_90', 'pay_basic_180', 'pay_basic_365',
                                         'pay_advanced_30', 'pay_advanced_90', 'pay_advanced_180', 'pay_advanced_365'])
