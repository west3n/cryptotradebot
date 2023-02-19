from aiogram import Dispatcher, types
from keyboards import reply


async def bot_start(msg: types.Message):
    await msg.delete()
    await msg.answer("Привет!", reply_markup=reply.start_keyboard())


def register(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands='start', state='*')
