from aiogram.dispatcher.filters.state import State, StatesGroup


class ObjectState(StatesGroup):
    Add = State()
    Rent = State()
    Sale = State()
    Delete = State()
    Edit = State()
    Activate = State()
