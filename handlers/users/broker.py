import os
import re
from datetime import date

import googleapiclient.discovery
import googleapiclient.discovery
import httplib2
from aiogram import types
from aiogram.dispatcher import FSMContext
from oauth2client.service_account import ServiceAccountCredentials

from filters.is_phone import IsPhone
from keyboards.default.commerce import kb_yes_or_no, kb_main_menu
from loader import dp
from states import MenuState


def google_sendler(sheet_id, start_col, end_col, array_data):
    CREDENTAILS_FILE = os.getenv('CREDENTAILS_FILE')
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


@dp.message_handler(IsPhone(), state=MenuState.Broker)
async def select_by_sell(message: types.Message, state=FSMContext):
    broker_number = message.text
    broker_number = re.findall(r'\d+', broker_number)
    broker_number = ''.join(broker_number)
    broker_correct_number = f'998{broker_number[-9:]}'
    await state.update_data(var_broker_correct_number=broker_correct_number)
    await message.answer(f"Все заполнил(-а) правильно ?", reply_markup=kb_yes_or_no)
    await MenuState.Broker_Q1.set()


# Состояние MenuState.Broker_Q1 -->  Все заполнил(-а) правильно ?
@dp.message_handler(state=MenuState.Broker_Q1)
async def select_district(message: types.Message, state=FSMContext):
    filled_in_correctly = message.text
    answer = await state.get_data()
    user_name = message.from_user.full_name

    if filled_in_correctly.lower() == 'да':
        dt_time = str(date.today())
        answer = await state.get_data()
        list_answer = []
        list_answer.append(answer['var_broker_correct_number'])
        await state.reset_state()
        await message.answer('Маклер добавлен в базу)', reply_markup=kb_main_menu)
        google_sendler('1o71IQm9tcRyDcYVApTig0Xx6zmEGv6lJq8c401lWW6c', 'Маклера!A', 'A', list_answer)
    elif filled_in_correctly.lower() == 'нет':
        await state.reset_state()
        await message.answer('Вы отменили отправку', reply_markup=kb_main_menu)
    else:
        await message.answer('Отправлено не верное значение( Попробуйте снова')
