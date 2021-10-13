import datetime
import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types.reply_keyboard import ReplyKeyboardRemove

from filters.is_digit import IsDigit
from filters.is_phone import IsPhone
from keyboards.default.send_by_apartment import kb_type_of_property, kb_district
from loader import dp
from states import SystemState
from sql.sql_query import SqlQuery


@dp.message_handler(state=SystemState.OlxStart)
async def start_system_olx(message: types.Message, state=FSMContext):
    await message.answer('Выберите вид недвижимости', reply_markup=kb_type_of_property)
    await SystemState.OLX_Q1.set()


@dp.message_handler(state=SystemState.OLX_Q1)
async def get_question(message: types.Message, state=FSMContext):
    type_of_property = message.text.strip().lower()
    await state.update_data(var_type_of_property=type_of_property)
    await message.answer('Выберите район', reply_markup=kb_district)
    await SystemState.OLX_Q2.set()


@dp.message_handler(state=SystemState.OLX_Q2)
async def get_question(message: types.Message, state=FSMContext):
    district = message.text.strip().lower()
    await state.update_data(var_district=district)
    await message.answer('Введите сектор', reply_markup=ReplyKeyboardRemove())
    await SystemState.OLX_Q3.set()


@dp.message_handler(IsDigit(), state=SystemState.OLX_Q3)
async def get_question(message: types.Message, state=FSMContext):
    sector = message.text.strip().lower()
    await state.update_data(var_sector=sector)
    await message.answer('Введите номер телефона в формате (кодстраны + номер телфона)', reply_markup=ReplyKeyboardRemove())
    await SystemState.OLX_Q4.set()


@dp.message_handler(IsPhone(), state=SystemState.OLX_Q4)
async def get_question(message: types.Message, state=FSMContext):
    number_object = message.text
    # Получаем с помощью регулярного выражения только числа
    decor_number = re.findall(r'\d+', number_object)
    # Получаем 9 чисел с правой стороны
    decor_number = int(''.join(decor_number)[-9:])

    await state.update_data(var_phone=decor_number)
    await message.answer('Введите информацию', reply_markup=ReplyKeyboardRemove())
    await SystemState.OLX_Q5.set()


@dp.message_handler(state=SystemState.OLX_Q5)
async def end_system_olx(message: types.Message, state=FSMContext):
    information = message.text.lower()
    await state.update_data(var_information=information)
    values = await state.get_data()
    date = datetime.datetime.today().isoformat(timespec='seconds')
    SqlQuery().add_row(table_name="olx",
                       keys=[
                           'type_of_property',
                           'district',
                           'sector',
                           'phone',
                           'information',
                           'date'
                       ],
                       values=(
                           values['var_type_of_property'],
                           values['var_district'],
                           values['var_sector'],
                           values['var_phone'],
                           values['var_information'],
                           date
                       ))
    await state.reset_state()
    await state.reset_data()
    await message.answer('OLX добавлен в базу данных')
    await message.answer(
        'Мы перенаправили вас в Главное Меню\nПожалуйста введите <b>пароль</b> чтобы продолжить ...')
    await SystemState.Start.set()
