import os
from datetime import date

import googleapiclient.discovery
import httplib2
from aiogram import types
from aiogram.dispatcher import FSMContext
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials

from keyboards.default.apartment import kb_main_menu
from keyboards.default.delete_object import kb_yes_or_no
from loader import dp
from states import ActiveObjectState, ObjectState

load_dotenv()


def google_sendler(sheet_id, start_col, end_col, array_data):
    CREDENTAILS_FILE = os.getenv('credentails_file')
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


# Отслеживаем сообщение по фильтру состояния ObjectState.Active
@dp.message_handler(state=ObjectState.Activate)
async def set_start_price(message: types.Message, state=FSMContext):
    id_object = message.text
    await state.update_data(var_id_object=id_object)
    await message.answer('Вы ввели все верно?', reply_markup=kb_yes_or_no)
    await ActiveObjectState.Q1.set()


# Состояние ActiveObjectState.Q1  -->  Все заполнил(-а) правильно ?
@dp.message_handler(state=ActiveObjectState.Q1)
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
        google_sendler('1D41UHIXRICwbW6X_ZCMr0fW5ETB75RGars2Ci7AQFUg', 'Активация!A', 'C', list_answer)
        await message.answer('Объект отправлен на активацию)', reply_markup=kb_main_menu)
        await state.reset_state()
    elif filled_in_correctly.lower() == 'нет':
        await message.answer('Вы отменили отправку', reply_markup=kb_main_menu)
        await state.reset_state()
    else:
        await message.answer('Отправлено не верное значение( Попробуйте снова')
