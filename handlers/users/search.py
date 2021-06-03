from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.search import kb_word_object
from loader import dp
from states import MenuState, SearchState


@dp.message_handler(text='Поиск по ID', state=MenuState.Search)
async def search(message: types.Message, state=FSMContext):
    await message.answer('Выберите букву объекта:\n'
                         'К - квартира\n'
                         'Н - квартира\n'
                         'И - квартира\n'
                         'КМ - квартира\n'
                         'Д - квартира\n'
                         'АК - квартира\n'
                         'АКМ - квартира\n'
                         'АД - квартира\n'
                         , reply_markup=kb_word_object)
    await SearchState.SearchId_Q1.set()


@dp.message_handler(text='Поиск по номеру', state=MenuState.Search)
async def search(message: types.Message, state=FSMContext):
    await message.answer('Введите номер телфона', reply_markup=ReplyKeyboardRemove())
    await SearchState.SearchNumber_Q1.set()
