from aiogram import Dispatcher, types


async def connect_api(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('Функция в разработке.')


def register(dp: Dispatcher):
    dp.register_callback_query_handler(connect_api, text='connect_api')
