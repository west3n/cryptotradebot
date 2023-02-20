from aiogram import Dispatcher, types
from keyboards import reply
from database.sqlite import create


async def bot_start(msg: types.Message):
    await msg.delete()
    user_id = msg.from_user.id
    name = msg.from_user.first_name
    await msg.answer(f"Привет, {name}!", reply_markup=reply.start_keyboard())
    user = await create.status(user_id)
    if not user:
        await create.add_user(user_id)


def register(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands='start', state='*')
