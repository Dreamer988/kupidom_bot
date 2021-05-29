from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from keyboards.default.apartment import kb_type_of_property, kb_type_of_service, kb_object_menu
from loader import dp
from states import MenuState


@dp.message_handler(Text(equals='Объект'), state=None)
async def get_menu(message: types.Message):
    await message.answer(f"Виберите одно из действий", reply_markup=kb_object_menu)
    await MenuState.first()


@dp.message_handler(Text(equals='Добавить'), state=MenuState.Q1)
async def get_menu(message: types.Message):
    await message.answer(f"Выбери вид услуги", reply_markup=kb_type_of_service)
    await MenuState.next()


@dp.message_handler(state=MenuState.Q2)
async def get_menu(message: types.Message, state=FSMContext):
    type_of_property = message.text
    await state.update_data(var_type_of_property=type_of_property)
    await message.answer(f"Выбери вид недвижимости", reply_markup=kb_type_of_property)
    await MenuState.next()
