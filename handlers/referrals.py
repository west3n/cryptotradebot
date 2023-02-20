from aiogram import Dispatcher, types
from keyboards import inline


async def referral_main_menu(call: types.CallbackQuery):
    user_id = call.from_user.id
    await call.message.delete()
    await call.message.answer(f"🤝 Партнерская программа\n\n"
                              f"🤑 Сколько можно заработать?\n"
                              f"├  За реферала 1 уровня: 12%\n"
                              f"🥇 Статистика:\n"
                              f"├  Всего заработано: \n"
                              f"├  Доступно к выводу: \n"
                              f"└  Приглашенных: \n\n"
                              f"⤵️ Ваши ссылки: t.me/cryptotradetemplatebot?start={user_id}",
                              reply_markup=inline.referral_main_menu())


async def referral_list(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('📁 Найдено 0 рефералов.\n\n'
                              'Данные в формате .xls успешно сформированы.', reply_markup=inline.referral_cancel())


async def funds_withdrawal(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Вы можете вывести средства на Банковскую карту "
                              "или же вывести средства на оплату наших услуг в боте.",
                              reply_markup=inline.withdrawal_choice())


async def withdrawal_on_balance(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('Средства успешно выведены на баланс.', reply_markup=inline.referral_cancel())


async def withdrawal_on_card(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('Средства успешно выведены на карту.', reply_markup=inline.referral_cancel())


def register(dp: Dispatcher):
    dp.register_callback_query_handler(referral_main_menu, text='referral_cancel')
    dp.register_callback_query_handler(referral_list, text='referral_list')
    dp.register_callback_query_handler(funds_withdrawal, text='funds_withdrawal')
    dp.register_callback_query_handler(withdrawal_on_balance, text='withdrawal_on_balance')
    dp.register_callback_query_handler(withdrawal_on_card, text='withdrawal_on_card')
