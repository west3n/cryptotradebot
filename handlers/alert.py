from aiogram import Bot, Dispatcher, types

BUTTON = [
    '/start',
    'Аккаунт',
    'Помощь',
    'Торговля',
    'Партнерская программа',
    'Ордера',
    'Настройка уведомлений'
]


async def alert(msg: types.Message):
    message_text = msg.text
    if message_text not in BUTTON:
        await msg.answer('Бот работает только с кнопками.')


def register(dp: Dispatcher):
    dp.register_message_handler(alert, content_types=['text', 'audio', 'photo', 'document', 'voice', 'sticker', 'video', 'location', 'animation'])
