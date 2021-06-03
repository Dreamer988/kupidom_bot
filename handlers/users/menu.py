from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from keyboards.default.apartment import kb_object_menu
from keyboards.default.by_sell import kb_menu_by_sell
from keyboards.default.search import kb_search_menu
from loader import dp
from states import MenuState


@dp.message_handler(Text(equals='Объект'), state=None)
async def get_menu(message: types.Message):
    await message.answer(f"Виберите одно из действий", reply_markup=kb_object_menu)
    await MenuState.Object.set()


@dp.message_handler(Text(equals='Купля - Продажа'), state=None)
async def get_menu(message: types.Message):
    await message.answer('Выберите раздел Купли-Продажи:', reply_markup=kb_menu_by_sell)
    await MenuState.BySell.set()


@dp.message_handler(Text(equals='Поиск'), state=None)
async def search(message: types.Message, state=FSMContext):
    await message.answer('Выберите', reply_markup=kb_search_menu)
    await MenuState.Search.set()


@dp.message_handler(Text(equals='Объект'), state=None)
async def get_menu(message: types.Message):
    # await message.answer(f"Виберите одно из действий", reply_markup=kb_object_menu)
    await MenuState.Broker.set()
