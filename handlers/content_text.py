from aiogram import Dispatcher, types
from keyboards import inline
from database.sqlite import create


async def bot_account(msg: types.Message):
    user_id = msg.from_user.id
    await msg.delete()
    user = await create.status(user_id)

    if user[3] is not None:
        days = await create.days_between_dates(user[2], user[3])
        await msg.answer(text=f'Вся необходимая информация о вашем профиле\n'
                              f'\n👁‍🗨 ID: {user_id}'
                              f'\n👁‍🗨 Активные подписки: {user[1]} до {user[3]} ({days} дней)'
                              f'\n\n💶 Мой кошелёк: {user[4]}'
                              f'\n💷 Мой партнёрский счёт: '
                              f'\n\n🔎 Моя статистика сделок:'
                              f'\n├ Кол-во закрытых сделок (все):'
                              f'\n├ Кол-во закрытых сделок (30 дней):'
                              f'\n└ Кол-во закрытых сделок (7 дней):',
                         reply_markup=inline.subscribe())
    else:
        await msg.answer(text=f'Вся необходимая информация о вашем профиле\n'
                              f'\n👁‍🗨 ID: {user_id}'
                              f'\n👁‍🗨 Активные подписки: Нет активной подписки.',
                         reply_markup=inline.subscribe())


async def bot_help(msg: types.Message):
    await msg.delete()
    await msg.answer(f"Мы постараемся помочь как можно быстрее, но ожидание может занять время.\n\n"
                     f"График работы: 10:00-00:00 GMT+3.\n\n"
                     f"Связаться с поддержкой для помощи?",
                     reply_markup=inline.help_decision())


async def bot_trading(msg: types.Message):
    await msg.delete()
    await msg.answer("В этом разделе вы можете выбрать стратегию торговли и настроить",
                     reply_markup=inline.trading_main_menu())


async def bot_partnership_program(msg: types.Message):
    await msg.delete()
    user_id = msg.from_user.id
    await msg.answer(f"🤝 Партнерская программа\n\n"
                     f"🤑 Сколько можно заработать?\n"
                     f"├  За реферала 1 уровня: 12%\n"
                     f"🥇 Статистика:\n"
                     f"├  Всего заработано: \n"
                     f"├  Доступно к выводу: \n"
                     f"└  Приглашенных: \n\n"
                     f"⤵️ Ваши ссылки: t.me/cryptotradetemplatebot?start={user_id}",
                     reply_markup=inline.referral_main_menu())


async def bot_orders(msg: types.Message):
    await msg.delete()
    await msg.answer(f"У вас нет активных ордеров!\n\n"
                     f"Для начала подключите API.",
                     reply_markup=inline.connect_api())


async def bot_notification_settings(msg: types.Message):
    await msg.delete()
    await msg.answer("Настройка уведомлений", reply_markup=inline.notification_settings())


def register(dp: Dispatcher):
    dp.register_message_handler(bot_account, text='Аккаунт', state='*')
    dp.register_message_handler(bot_help, text='Помощь', state='*')
    dp.register_message_handler(bot_trading, text='Торговля', state='*')
    dp.register_message_handler(bot_partnership_program, text='Партнерская программа', state='*')
    dp.register_message_handler(bot_orders, text='Ордера', state='*')
    dp.register_message_handler(bot_notification_settings, text='Настройка уведомлений', state='*')
