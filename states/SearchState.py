from aiogram.dispatcher.filters.state import State, StatesGroup


class SearchState(StatesGroup):
    SearchNumber_Q1 = State()
    SearchNumber_Q2 = State()
    SearchId_Q1 = State()
    SearchId_Q2 = State()
    SearchId_Q3 = State()