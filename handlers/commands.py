from aiogram import Dispatcher, types
from keyboards import reply
from database.sqlite import user as db


async def bot_start(msg: types.Message):
    await msg.delete()
    user_id = msg.from_user.id
    name = msg.from_user.first_name
    user = await db.status(user_id)
    if user:
        await msg.answer(f"Привет, {name}!", reply_markup=reply.start_keyboard())
    else:
        await msg.answer(f'Привет, {name}!\n'
                         f'Здесь будет приветственное сообщение для пользователя без подписки.',
                         reply_markup=reply.start_keyboard_new_user())


def register(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands='start', state='*')
