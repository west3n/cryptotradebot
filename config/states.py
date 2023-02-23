from aiogram.dispatcher.filters.state import State, StatesGroup


class ApiConnector(StatesGroup):
    exc = State()
    api_key = State()
    api_secret = State()
