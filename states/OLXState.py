from aiogram.dispatcher.filters.state import State, StatesGroup


class OLXState(StatesGroup):
    OLX_New = State()
    OLX_Waiting = State()
    OLX_Object = State()
    OLX_Object_Waiting = State()
    OLX_Get = State()
    OLX_Get_Waiting = State()
    OLX_Sell = State()
    OLX_Sell_Waiting = State()
    OLX_Call = State()
    OLX_Zone = State()
    OLX_Sector = State()
    OLX_Delete = State()
    OLX_NotLoyal = State()
