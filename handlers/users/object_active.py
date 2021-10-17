from datetime import date

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from google_work.google_work import GoogleWork
from keyboards.default.send_by_apartment import kb_main_menu
from keyboards.default.delete_object import kb_yes_or_no
from loader import dp
from states import ActiveObjectState, ObjectState

# Отслеживаем сообщение по фильтру состояния ObjectState.Active
from utils import activate


@dp.message_handler(state=ObjectState.Activate)
async def set_start_price(message: types.Message, state=FSMContext):
    type_of_property = message.text

    await state.update_data(var_type_of_property=type_of_property)
    await message.answer('Введите ID объекта', reply_markup=ReplyKeyboardRemove())
    await ActiveObjectState.Q1.set()


# Состояние ActiveObjectState.Q1  -->  Введите ID объекта
@dp.message_handler(state=ActiveObjectState.Q1)
async def select_district(message: types.Message, state=FSMContext):
    id_object = message.text
    await state.update_data(var_id_object=id_object)
    await message.answer('Вы ввели все верно?', reply_markup=kb_yes_or_no)
    await ActiveObjectState.Q2.set()


# Состояние ActiveObjectState.Q2  -->  Все заполнил(-а) правильно ?
@dp.message_handler(state=ActiveObjectState.Q2)
async def select_district(message: types.Message, state=FSMContext):
    filled_in_correctly = message.text

    if filled_in_correctly.lower() == 'да':
        answer = await state.get_data()
        await state.reset_state()
        await message.answer('Объект отправлен на активацию)', reply_markup=kb_main_menu)

        type_of_property = answer['var_type_of_property'].lower().strip()
        id_object = answer['var_id_object'].strip()
        activate(type_of_property=type_of_property, id_object=id_object)

        GoogleWork().google_add_row(sheet_id='1D41UHIXRICwbW6X_ZCMr0fW5ETB75RGars2Ci7AQFUg',
                                    name_list='Активация',
                                    array_data=[
                                        answer['var_id_object'],
                                        message.from_user.full_name,
                                        '',
                                        str(date.today())
                                    ])
    elif filled_in_correctly.lower() == 'нет':
        await state.reset_state()
        await message.answer('Вы отменили отправку', reply_markup=kb_main_menu)
    else:
        await message.answer('Отправлено не верное значение( Попробуйте снова')
