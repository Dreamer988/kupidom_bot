import os
from datetime import date

import googleapiclient
from googleapiclient import discovery
import httplib2
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from oauth2client.service_account import ServiceAccountCredentials

from filters.is_digit import IsDigit
from keyboards.default.apartment import kb_back, kb_main_menu
from keyboards.default.by_sell import kb_currency
from keyboards.default.delete_object import kb_yes_or_no
from loader import dp
from states import BySell


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


@dp.message_handler(IsDigit(), state=BySell.Prepayment_Q1)
async def set_prepayment(message: types.Message, state=FSMContext):
    sum_prepayment = message.text
    await state.update_data(var_sum_prepayment=sum_prepayment)
    await message.answer('Выберите валюту в которой был взят аванс',
                         reply_markup=kb_currency)
    await BySell.Prepayment_Q2.set()


@dp.message_handler(state=BySell.Prepayment_Q2)
async def set_prepayment(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Prepayment_Q1.set()
        await message.answer('Укажите сумму взятого вами аванса',
                             reply_markup=kb_back)
    else:
        currency_prepayment = message.text
        await state.update_data(var_currency_prepayment=currency_prepayment)
        await message.answer('Укажите дату получения аванса \n(Пример : 30.01.2020)',
                             reply_markup=kb_back)
        await BySell.Prepayment_Q3.set()


@dp.message_handler(state=BySell.Prepayment_Q3)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Prepayment_Q2.set()
        await message.answer('Выберите валюту в которой был взят аванс',
                             reply_markup=ReplyKeyboardRemove())
    else:
        date_prepayment = message.text
        await state.update_data(var_date_prepayment=date_prepayment)

        await message.answer(f"Все заполнил(-а) правильно ?", reply_markup=kb_yes_or_no)
        await BySell.Prepayment_Q4.set()


@dp.message_handler(state=BySell.Prepayment_Q4)
async def select_district(message: types.Message, state=FSMContext):
    filled_in_correctly = message.text
    answer = await state.get_data()
    user_name = message.from_user.full_name

    if filled_in_correctly.lower() == 'да':
        dt_time = str(date.today())
        answer = await state.get_data()
        list_answer = []
        list_answer.append(dt_time)
        list_answer.append(user_name)
        list_answer.append(answer['var_sum_prepayment'])
        list_answer.append(answer['var_currency_prepayment'])
        list_answer.append(answer['var_date_prepayment'])
        await state.reset_state()
        await message.answer('Аванс отправлен', reply_markup=kb_main_menu)
        google_sendler('1cybTRAnHDJ1gRiX5aY9XkD_84LXbMKccQPmjZn4YcCs', 'Аванс!A', 'E', list_answer)
    elif filled_in_correctly.lower() == 'нет':
        await state.reset_state()
        await message.answer('Вы отменили отправку', reply_markup=kb_main_menu)
    else:
        await message.answer('Отправлено не верное значение( Попробуйте снова')
