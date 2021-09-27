from datetime import date

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from google_work.google_work import GoogleWork
from keyboards.default.send_by_apartment import kb_main_menu
from keyboards.default.delete_object import kb_yes_or_no, kb_reason_delete_back
from keyboards.default.step_back import kb_back
from loader import dp
from states import ObjectState
from states.DeleteObjectState import DeleteObjectState


# Отслеживаем сообщение по фильтру состояния ObjectState.Delete
@dp.message_handler(state=ObjectState.Delete)
async def select_property(message: types.Message, state=FSMContext):
    type_of_property = message.text

    await state.update_data(var_type_of_property=type_of_property)
    await message.answer('Введите ID объекта', reply_markup=ReplyKeyboardRemove())
    await DeleteObjectState.Q1.set()


# Состояние ApartmentState.Q1  -->  Введите ID объекта
@dp.message_handler(state=DeleteObjectState.Q1)
async def set_id_object(message: types.Message, state=FSMContext):
    id_object = message.text

    await state.update_data(var_id_object=id_object)
    await message.answer('Введите имя агента на которого записан этот объект', reply_markup=kb_back)
    await DeleteObjectState.next()


# Состояние ApartmentState.Q2  -->  Введите имя агента на которого записан этот объект
@dp.message_handler(state=DeleteObjectState.Q2)
async def set_agent_name(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await DeleteObjectState.Q1.set()
        await message.answer('Введите ID объекта', reply_markup=ReplyKeyboardRemove())
    else:
        agent_name = message.text

        await state.update_data(var_agent_name=agent_name)
        await message.answer('Выберите причину удаления объекта или впишите свою',
                             reply_markup=kb_reason_delete_back)
        await DeleteObjectState.next()


# Состояние ApartmentState.Q3  -->  Выберите причину удаления объекта или впишите свою
@dp.message_handler(state=DeleteObjectState.Q3)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await DeleteObjectState.Q2.set()
        await message.answer('Введите имя агента на которого записан этот объект', reply_markup=kb_back)
    else:
        reason_delete = message.text

        await state.update_data(var_reason_delete=reason_delete)
        await message.answer(f"Все заполнил(-а) правильно ?", reply_markup=kb_yes_or_no)
        await DeleteObjectState.next()


# Состояние ApartmentState.Q4  -->  Все заполнил(-а) правильно ?
@dp.message_handler(state=DeleteObjectState.Q4)
async def select_district(message: types.Message, state=FSMContext):
    filled_in_correctly = message.text

    if filled_in_correctly.lower() == 'да':
        answer = await state.get_data()
        await state.reset_state()
        await message.answer('Объект отправлен на удаление)', reply_markup=kb_main_menu)
        GoogleWork().google_add_row(sheet_id='1D41UHIXRICwbW6X_ZCMr0fW5ETB75RGars2Ci7AQFUg',
                                    name_list='Удаление',
                                    array_data=[
                                        answer['var_id_object'],
                                        message.from_user.full_name,
                                        answer['var_agent_name'],
                                        answer['var_reason_delete'],
                                        str(date.today()),
                                        '',
                                        answer['var_type_of_property']
                                    ])
    elif filled_in_correctly.lower() == 'нет':
        await state.reset_state()
        await message.answer('Вы отменили отправку', reply_markup=kb_main_menu)
    else:
        await message.answer('Отправлено не верное значение( Попробуйте снова')
