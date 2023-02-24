from aiogram import Dispatcher, types


async def on_button_clicked(call: types.CallbackQuery):
    try:
        if call.data == "hide_all_buttons":
            keyboard = types.InlineKeyboardMarkup(inline_keyboard=[])
            await call.message.edit_text("Все уведомления скрыты.", reply_markup=keyboard)
        # else:
        #     btn_index = int(call.data.replace("btn", ""))
        #     current_state = call.message.reply_markup.inline_keyboard[btn_index - 1][0].text.split()[0]
        #     new_state = "🔕" if current_state == "🔔" else "🔔"
        #     button_text = call.message.reply_markup.inline_keyboard[btn_index - 1][0].text
        #     new_button_text = button_text.replace(current_state, new_state)
        #     call.message.reply_markup.inline_keyboard[btn_index - 1][0].text = new_button_text
        #     await call.bot.edit_message_reply_markup(
        #         chat_id=call.message.chat.id,
        #         message_id=call.message.message_id,
        #         reply_markup=call.message.reply_markup)
    except ValueError:
        await call.message.answer("Это тестовое сообщение, которое отлавливает ошибку")


async def hide_all(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[])
    await call.message.edit_text("Все уведомления скрыты.", reply_markup=keyboard)


def register(dp: Dispatcher):
    dp.register_callback_query_handler(on_button_clicked)
    dp.register_callback_query_handler(hide_all, text='hide_all_buttons')
