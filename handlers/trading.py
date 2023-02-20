from aiogram import Dispatcher, types
from keyboards import inline


async def trading_main_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("В этом разделе вы можете выбрать стратегию торговли и настроить",
                              reply_markup=inline.trading_main_menu())


async def trading_blacklist(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('Здесь будет черный список торговых пар', reply_markup=inline.trading_cancel())


async def trading_strategy_settings(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('Здесь будут настройки по стратегиям', reply_markup=inline.trading_cancel())


async def trading_strategy(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('Здесь будут стратегии', reply_markup=inline.trading_cancel())


def register(dp: Dispatcher):
    dp.register_callback_query_handler(trading_blacklist, text='trading_blacklist')
    dp.register_callback_query_handler(trading_strategy_settings, text='trading_strategy_settings')
    dp.register_callback_query_handler(trading_strategy, text='trading_strategy')
    dp.register_callback_query_handler(trading_main_menu, text='trading_cancel')
