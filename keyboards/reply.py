from aiogram.types.reply_keyboard import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


def start_keyboard():
    keyboard = ReplyKeyboardMarkup([

        [KeyboardButton(text="Аккаунт"),
         KeyboardButton(text="Помощь"),
         KeyboardButton(text="Торговля")],

        [KeyboardButton(text="Партнерская программа"),
         KeyboardButton(text="Ордера")],

        [KeyboardButton(text="Настройка уведомлений")],

    ], resize_keyboard=True)
    return keyboard


def start_keyboard_new_user():
    keyboard = ReplyKeyboardMarkup([
        [KeyboardButton(text="Аккаунт"),
         KeyboardButton(text="Помощь")]
        ], resize_keyboard=True)
    return keyboard
