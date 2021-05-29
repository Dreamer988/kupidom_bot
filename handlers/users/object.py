from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from keyboards.default.apartment import kb_type_of_property, kb_type_of_service, kb_object_menu
from loader import dp
from states import MenuState, ObjectState


@dp.message_handler(Text(equals='Добавить'), state=MenuState.Object)
async def get_menu(message: types.Message):
    await message.answer(f"Выбери вид услуги", reply_markup=kb_type_of_service)


@dp.message_handler(Text(equals='Удалить'), state=MenuState.Object)
async def get_menu(message: types.Message):
    await message.answer(f"Выбери вид услуги", reply_markup=kb_type_of_service)
    await ObjectState.Delete.set()


@dp.message_handler(Text(equals='Изменить'), state=MenuState.Object)
async def get_menu(message: types.Message):
    await message.answer(f"Выбери вид услуги", reply_markup=kb_type_of_service)
    await ObjectState.Edit.set()


@dp.message_handler(Text(equals='Активировать'), state=MenuState.Object)
async def get_menu(message: types.Message):
    await message.answer(f"Выбери вид услуги", reply_markup=kb_type_of_service)
    await ObjectState.Activate.set()


@dp.message_handler(text="Продажа", state=MenuState.Object)
async def get_menu(message: types.Message, state=FSMContext):
    type_of_property = message.text
    await state.update_data(var_type_of_property=type_of_property)
    await message.answer(f"Выбери вид недвижимости", reply_markup=kb_type_of_property)
    await ObjectState.Sale.set()


@dp.message_handler(text="Аренда", state=MenuState.Object)
async def get_menu(message: types.Message, state=FSMContext):
    type_of_property = message.text
    await state.update_data(var_type_of_property=type_of_property)
    await message.answer(f"Выбери вид недвижимости", reply_markup=kb_type_of_property)
    await ObjectState.Rent.set()
