from datetime import date

import googleapiclient.discovery
import httplib2
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials

from keyboards.default.apartment import kb_yes_or_no
from keyboards.default.apartment import kb_main_menu
from loader import dp
from states import EditObjectState
from states import ObjectState

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


# Отслеживаем сообщение по фильтру состояния ObjectState.Edit
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


# Состояние EditObjectState.Q2  -->  Введите имя агента на которого записан этот объект
@dp.message_handler(state=EditObjectState.Q2)
async def set_start_price(message: types.Message, state=FSMContext):
    start_price = message.text
    await state.update_data(var_start_price=start_price)
    await message.answer(
        'Введите общую цену  Пример: \n28000\n27500\n27000\n________________\n Если аренда введите  - Предоплату (Пример : 1 месяц)',
        reply_markup=ReplyKeyboardRemove())
    await EditObjectState.next()


# Состояние EditObjectState.Q3  -->  Введите имя агента на которого записан этот объект
@dp.message_handler(state=EditObjectState.Q3)
async def set_start_price(message: types.Message, state=FSMContext):
    full_price = message.text
    await state.update_data(var_full_price=full_price)
    await message.answer('Вы ввели все верно?', reply_markup=kb_yes_or_no)
    await EditObjectState.next()


# Состояние ApartmentState.Q4  -->  Все заполнил(-а) правильно ?
@dp.message_handler(state=EditObjectState.Q4)
async def select_district(message: types.Message, state=FSMContext):
    filled_in_correctly = message.text
    answer = await state.get_data()
    user_name = message.from_user.full_name

    if filled_in_correctly.lower() == 'да':
        dt_time = str(date.today())
        answer = await state.get_data()
        list_answer = []
        list_answer.append(answer['var_id_object'])
        list_answer.append(answer['var_type_of_property'])
        list_answer.append(answer['var_start_price'])
        list_answer.append(answer['var_full_price'])
        list_answer.append(user_name)
        list_answer.append('')
        list_answer.append(dt_time)
        google_sendler('1D41UHIXRICwbW6X_ZCMr0fW5ETB75RGars2Ci7AQFUg', 'Изменение!A', 'G', list_answer)
        await message.answer('Объект отправлен на изменение)', reply_markup=kb_main_menu)
        await state.reset_state()
    elif filled_in_correctly.lower() == 'нет':
        await message.answer('Вы отменили отправку', reply_markup=kb_main_menu)
        await state.reset_state()
    else:
        await message.answer('Отправлено не верное значение( Попробуйте снова')
