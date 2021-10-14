from aiogram.dispatcher.filters.state import State, StatesGroup


class OLXState(StatesGroup):
    OLX_Object = State()
    OLX_Get = State()
    OLX_Sell = State()
    OLX_Call = State()
    OLX_Zone = State()
    OLX_Sector = State()
    OLX_Delete = State()
    OLX_NotLoyal = State()
