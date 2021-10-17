from aiogram.dispatcher.filters.state import State, StatesGroup


class MenuState(StatesGroup):
    Object = State()
    BySell = State()
    Search = State()
    Broker = State()
    Broker_Q1 = State()
    OLX = State()
    Calling = State()
    CallingMenu = State()
