from datetime import date, datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from google_work.google_work import GoogleWork
from keyboards.default.send_by_apartment import kb_main_menu
from keyboards.default.send_by_apartment import kb_yes_or_no
from keyboards.default.step_back import kb_back
from loader import dp
from states import EditObjectState
from states import ObjectState


# Отслеживаем сообщение по фильтру состояния ObjectState.Edit
from utils import activate


@dp.message_handler(state=ObjectState.Edit)
async def select_property(message: types.Message, state=FSMContext):
    type_of_property = message.text

    await state.update_data(var_type_of_property=type_of_property)
    await message.answer('Введите ID объекта', reply_markup=ReplyKeyboardRemove())
    await EditObjectState.Q1.set()


# Состояние EditObjectState.Q1  -->  Введите ID объекта
@dp.message_handler(state=EditObjectState.Q1)
async def set_id_object(message: types.Message, state=FSMContext):
    id_object = message.text

    await state.update_data(var_id_object=id_object)
    await message.answer('Введите стартовую цену  (Пример: 28000)', reply_markup=ReplyKeyboardRemove())
    await EditObjectState.next()


# Состояние EditObjectState.Q2  -->  Введите стартовую цену
@dp.message_handler(state=EditObjectState.Q2)
async def set_start_price(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await EditObjectState.Q1.set()
        await message.answer('Введите ID объекта', reply_markup=ReplyKeyboardRemove())
    else:
        start_price = message.text

        await state.update_data(var_start_price=start_price)
        await message.answer(
            'Введите общую цену  Пример: \n28000\n27500\n27000\n'
            '________________'
            '\n Если аренда введите  - Предоплату (Пример : 1 месяц)',
            reply_markup=kb_back)
        await EditObjectState.next()


# Состояние EditObjectState.Q3  -->  Введите имя агента на которого записан этот объект
@dp.message_handler(state=EditObjectState.Q3)
async def set_start_price(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await EditObjectState.Q1.set()
        await message.answer('Введите стартовую цену  (Пример: 28000)', reply_markup=kb_back)
    else:
        full_price = message.text

        await state.update_data(var_full_price=full_price)
        await message.answer('Вы ввели все верно?', reply_markup=kb_yes_or_no)
        await EditObjectState.next()


# Состояние ApartmentState.Q4  -->  Все заполнил(-а) правильно ?
@dp.message_handler(state=EditObjectState.Q4)
async def select_district(message: types.Message, state=FSMContext):
    filled_in_correctly = message.text

    if filled_in_correctly.lower() == 'да':
        answer = await state.get_data()
        await state.reset_state()
        await message.answer('Объект отправлен на изменение)', reply_markup=kb_main_menu)
        type_of_property = answer['var_type_of_property'].lower().strip()
        id_object = answer['var_id_object'].strip()
        activate(type_of_property=type_of_property,id_object=id_object)

        GoogleWork().google_add_row(sheet_id='1D41UHIXRICwbW6X_ZCMr0fW5ETB75RGars2Ci7AQFUg',
                                    name_list='Изменение',
                                    array_data=[
                                        answer['var_id_object'],
                                        answer['var_type_of_property'],
                                        answer['var_start_price'],
                                        answer['var_full_price'],
                                        message.from_user.full_name,
                                        '',
                                        str(date.today())
                                    ])
    elif filled_in_correctly.lower() == 'нет':
        await state.reset_state()
        await message.answer('Вы отменили отправку', reply_markup=kb_main_menu)
    else:
        await message.answer('Отправлено не верное значение( Попробуйте снова')
