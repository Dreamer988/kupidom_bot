from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from keyboards.default.apartment import kb_type_of_property, kb_type_of_service, kb_object_menu
from loader import dp
from states import MenuState


@dp.message_handler(Text(equals='Объект'), state=None)
async def get_menu(message: types.Message):
    await message.answer(f"Виберите одно из действий", reply_markup=kb_object_menu)
    await MenuState.Object.set()


@dp.message_handler(Text(equals='Купля - Продажа'), state=None)
async def get_menu(message: types.Message):
    # await message.answer(f"Виберите одно из действий", reply_markup=kb_object_menu)
    await MenuState.BySell.set()


@dp.message_handler(Text(equals='Объект'), state=None)
async def get_menu(message: types.Message):
    # await message.answer(f"Виберите одно из действий", reply_markup=kb_object_menu)
    await MenuState.Search.set()


@dp.message_handler(Text(equals='Объект'), state=None)
async def get_menu(message: types.Message):
    # await message.answer(f"Виберите одно из действий", reply_markup=kb_object_menu)
    await MenuState.Broker.set()
