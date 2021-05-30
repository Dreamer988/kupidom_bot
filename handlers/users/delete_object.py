from datetime import date

import googleapiclient.discovery
import httplib2
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials

from keyboards.default.apartment import kb_main_menu
from keyboards.default.delete_object import kb_reason_delete, kb_yes_or_no
from loader import dp
from states import ObjectState
from states.DeleteObjectState import DeleteObjectState

load_dotenv()


def google_sendler(sheet_id, start_col, end_col, array_data):
    CREDENTAILS_FILE = "C:/Users/User/Desktop/udemy_course-master/creds.json"
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTAILS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)
    spreadsheet_id = sheet_id

    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=f"{start_col}:{end_col}",
        majorDimension="COLUMNS"
    ).execute()
    start_range = len(values['values'][0]) + 1
    sheet_range = f"{start_col}{start_range}:{end_col}{start_range}"

    values = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=f"{start_col}{start_range}",
        valueInputOption="USER_ENTERED",
        body={
            "values": [['']]
        }
    ).execute()

    values = service.spreadsheets().values().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body={
            "valueInputOption": "USER_ENTERED",
            "data": [
                {
                    "range": sheet_range,
                    "majorDimension": "ROWS",
                    "values": [array_data]
                }
            ]
        }
    ).execute()


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
    await message.answer('Введите имя агента на которого записан этот объект', reply_markup=ReplyKeyboardRemove())
    await DeleteObjectState.next()


# Состояние ApartmentState.Q2  -->  Введите имя агента на которого записан этот объект
@dp.message_handler(state=DeleteObjectState.Q2)
async def set_agent_name(message: types.Message, state=FSMContext):
    agent_name = message.text
    await state.update_data(var_agent_name=agent_name)
    await message.answer('Выберите причину удаления объекта или впишите свою', reply_markup=kb_reason_delete)
    await DeleteObjectState.next()


# Состояние ApartmentState.Q3  -->  Выберите причину удаления объекта или впишите свою
@dp.message_handler(state=DeleteObjectState.Q3)
async def select_district(message: types.Message, state=FSMContext):
    reason_delete = message.text

    await state.update_data(var_reason_delete=reason_delete)
    await message.answer(f"Все заполнил(-а) правильно ?", reply_markup=kb_yes_or_no)
    await DeleteObjectState.next()


# Состояние ApartmentState.Q4  -->  Все заполнил(-а) правильно ?
@dp.message_handler(state=DeleteObjectState.Q4)
async def select_district(message: types.Message, state=FSMContext):
    filled_in_correctly = message.text
    answer = await state.get_data()
    user_name = message.from_user.full_name

    if filled_in_correctly.lower() == 'да':
        dt_time = str(date.today())
        answer = await state.get_data()
        list_answer = []
        list_answer.append(answer['var_id_object'])
        list_answer.append(user_name)
        list_answer.append(answer['var_agent_name'])
        list_answer.append(answer['var_reason_delete'])
        list_answer.append(dt_time)
        list_answer.append('')
        list_answer.append(answer['var_type_of_property'])
        google_sendler('1D41UHIXRICwbW6X_ZCMr0fW5ETB75RGars2Ci7AQFUg', 'Удаление!A', 'G', list_answer)
        await message.answer('Объект отправлен на удаление)', reply_markup=kb_main_menu)
        await state.reset_state()
    elif filled_in_correctly.lower() == 'нет':
        await message.answer('Вы отменили отправку', reply_markup=kb_main_menu)
        await state.reset_state()
    else:
        await message.answer('Отправлено не верное значение( Попробуйте снова')
