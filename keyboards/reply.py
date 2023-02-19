from aiogram.types.reply_keyboard import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


def start_keyboard():
    keyboard = ReplyKeyboardMarkup([
        [
            KeyboardButton(text="1"),
            KeyboardButton(text="2"),
            KeyboardButton(text="3"),
            KeyboardButton(text="4"),
            KeyboardButton(text="5"),
            KeyboardButton(text="6"),
            KeyboardButton(text="7"),
        ]
    ], resize_keyboard=True)
    return keyboard
