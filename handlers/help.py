from aiogram import Dispatcher, types


async def help_no(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('Вы отменили связь с технической поддержкой.')


def register(dp: Dispatcher):
    dp.register_callback_query_handler(help_no, text='help_no')
