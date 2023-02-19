from aiogram import Dispatcher, types


async def text1(msg: types.Message):
    await msg.answer("Answer to 1")


async def text2(msg: types.Message):
    await msg.answer("Answer to 2")


async def text3(msg: types.Message):
    await msg.answer("Answer to 3")


async def text4(msg: types.Message):
    await msg.answer("Answer to 4")


async def text5(msg: types.Message):
    await msg.answer("Answer to 5")


async def text6(msg: types.Message):
    await msg.answer("Answer to 6")


async def text7(msg: types.Message):
    await msg.answer("Answer to 7")


def register(dp: Dispatcher):
    dp.register_message_handler(text1, text='1', state='*')
    dp.register_message_handler(text2, text='2', state='*')
    dp.register_message_handler(text3, text='3', state='*')
    dp.register_message_handler(text4, text='4', state='*')
    dp.register_message_handler(text5, text='5', state='*')
    dp.register_message_handler(text6, text='6', state='*')
    dp.register_message_handler(text7, text='7', state='*')
