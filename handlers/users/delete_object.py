import os

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.apartment import kb_district
from loader import dp
from states import ObjectState, ApartmentState
from datetime import date

from pprint import pprint

import googleapiclient.discovery
import httplib2
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials

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
        range="Продажа квартиры!A:A",
        majorDimension="COLUMNS"
    ).execute()
    pprint(values['values'][0])
    pprint(len(values['values'][0]))
    start_range = len(values['values'][0]) + 1
    sheet_range = f"{start_col}{start_range}:{end_col}{start_range}"

    values = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=f"Продажа квартиры!A{start_range}",
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
@dp.message_handler(text="Удалить", state=ObjectState.Delete)
async def select_district(message: types.Message, state=FSMContext):

    await message.answer("Вы вошли в удаление")
