from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def subscribe() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Управление подпиской', callback_data='subscribe')]
    ])
    return kb


def kb_subscribe_description() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Бесплатное тестирование', callback_data='free_sub')],
        [InlineKeyboardButton('Оплатить подписку Basic', callback_data='pay_basic')],
        [InlineKeyboardButton('Оплатить подписку Advanced', callback_data='pay_advanced')]
    ])
    return kb


def kb_subscribe_old() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Оплатить подписку Basic', callback_data='pay_basic')],
        [InlineKeyboardButton('Оплатить подписку Advanced', callback_data='pay_advanced')]
    ])
    return kb


def kb_pay_basic() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Оплатить на 30 дней', callback_data='pay_basic_30')],
        [InlineKeyboardButton('Оплатить на 90 дней', callback_data='pay_basic_90')],
        [InlineKeyboardButton('Оплатить на 180 дней', callback_data='pay_basic_180')],
        [InlineKeyboardButton('Оплатить на 365 дней', callback_data='pay_basic_365')],
        [InlineKeyboardButton('Вернуться назад', callback_data='subscribe')]
    ])
    return kb


def kb_pay_advanced() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Оплатить на 30 дней', callback_data='pay_advanced_30')],
        [InlineKeyboardButton('Оплатить на 90 дней', callback_data='pay_advanced_90')],
        [InlineKeyboardButton('Оплатить на 180 дней', callback_data='pay_advanced_180')],
        [InlineKeyboardButton('Оплатить на 365 дней', callback_data='pay_advanced_365')],
        [InlineKeyboardButton('Вернуться назад', callback_data='subscribe')]
    ])
    return kb


def help_decision() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Да', callback_data='help_yes', url="https://t.me/artok14"),
         InlineKeyboardButton('Нет', callback_data='help_no')]
    ])
    return kb


def trading_main_menu() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Черный список торговых пар', callback_data='trading_blacklist')],
        [InlineKeyboardButton('Настройки по стратегиям', callback_data='trading_strategy_settings')],
        [InlineKeyboardButton('Стратегия', callback_data='trading_strategy')]
    ])
    return kb


def trading_cancel() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Назад', callback_data='trading_cancel')]
    ])
    return kb


def referral_main_menu() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Рефералы', callback_data='referral_list'),
         InlineKeyboardButton('Вывод', callback_data='funds_withdrawal')]
    ])
    return kb


def referral_cancel() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Назад', callback_data='referral_cancel')]
    ])
    return kb


def withdrawal_choice() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('На баланс', callback_data='withdrawal_on_balance'),
         InlineKeyboardButton("На карту", callback_data='withdrawal_on_card')]
    ])
    return kb


def connect_api() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Подключить API', callback_data='connect_api')]
    ])
    return kb


def notification_settings() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("🔕 Уведомление 1", callback_data="btn1")],
        [InlineKeyboardButton("🔕 Уведомление 2", callback_data="btn2")],
        [InlineKeyboardButton("🔕 Уведомление 3", callback_data="btn3")],
        [InlineKeyboardButton("🔕 Уведомление 4", callback_data="btn4")],
        [InlineKeyboardButton("🔕 Уведомление 5", callback_data="btn5")],
        [InlineKeyboardButton("🔕 Уведомление 6", callback_data="btn6")],
        [InlineKeyboardButton("🔕 Уведомление 7", callback_data="btn7")],
        [InlineKeyboardButton("Скрыть все уведомления", callback_data="hide_all_buttons")]
    ])
    return kb


def api_main() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Basic', callback_data='api_basic')],
        [InlineKeyboardButton('Advanced', callback_data='api_advanced')]
    ])
    return kb


def api_main_basic() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Bybit', callback_data='bybit')],
        [InlineKeyboardButton('Bittrex', callback_data='bittrex')],
        [InlineKeyboardButton('Huobi', callback_data='huobi')],
        [InlineKeyboardButton('Poloniex (в разработке)', callback_data='poloniex')],
        [InlineKeyboardButton('Exmo (в разработке)', callback_data='exmo')],
        [InlineKeyboardButton('Kucoin (в разработке)', callback_data='kucoin')],
        [InlineKeyboardButton('OKX (в разработке)', callback_data='okx')],
        [InlineKeyboardButton('MXC (в разработке)', callback_data='mxc')],
        [InlineKeyboardButton('Gate (в разработке)', callback_data='gate')],
        [InlineKeyboardButton('HitBTC (в разработке)', callback_data='hitbtc')],

    ])

    return kb


def api_main_adv() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Binance (в разработке)', callback_data='binance')],
        [InlineKeyboardButton('Coinbase (в разработке)', callback_data='coinbase')],
        [InlineKeyboardButton('Kraken (в разработке)', callback_data='kraken')],
        [InlineKeyboardButton('Kukoin Futures (в разработке)', callback_data='kukoin_futures')],
        [InlineKeyboardButton('Bitfinex (в разработке)', callback_data='bitfinex')],

    ])

    return kb


def cmd_more(data) -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Подробнее', callback_data=data)]
    ])

    return kb


def cmd_close(data) -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Закрыть активные ордера', callback_data=data)]
    ])
    return kb