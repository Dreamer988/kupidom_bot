import os
import re
import googleapiclient.discovery
import httplib2
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

from filters.is_phone import IsPhone
from keyboards.default.apartment import kb_main_menu
from keyboards.default.search import kb_word_object, kb_go_start
from loader import dp
from states import SearchState

load_dotenv()


def binary_search(array_number, number: int):
    left_point = 0
    right_point = len(array_number)
    middle_point = int((right_point + left_point) / 2)
    while (right_point - 1 > left_point):
        if number == int(array_number[middle_point]):
            return middle_point
        elif number < int(array_number[middle_point]):
            right_point = middle_point
            middle_point = int((right_point + left_point) / 2)
        elif number > int(array_number[middle_point]):
            left_point = middle_point
            middle_point = int((right_point + left_point) / 2)

    return False


def search_by_number(number):
    CREDENTAILS_FILE = os.getenv('CREDENTAILS_FILE')
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTAILS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)
    spreadsheet_id = "1dNu9kjbn02aFVeQz3Uk8ivwW2QQUENApoDqbeM2LEl0"

    number_sheets = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=f"Общая база!A:F",
        majorDimension="COLUMNS"
    ).execute()

    broker_sheets = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=f"Маклера!A:A",
        majorDimension="COLUMNS"
    ).execute()

    broker_number = int('998' + str(number))
    number_point = binary_search(number_sheets['values'][0], number)
    broker_point = binary_search(broker_sheets['values'][0], broker_number)

    if broker_point:
        return 'Маклер'

    elif number_point:
        answer = list()
        number_point = number_point - 10
        for num in range(21):
            number_point += 1
            res = list()
            if str(number) == number_sheets['values'][0][number_point]:
                number_object = number_sheets['values'][0][number_point]
                id = number_sheets['values'][1][number_point]
                street = number_sheets['values'][2][number_point]
                point = number_sheets['values'][3][number_point]
                apartment = number_sheets['values'][4][number_point]
                home = number_sheets['values'][5][number_point]
                res.append(number_object)
                res.append(id)
                res.append(street)
                res.append(point)
                res.append(apartment)
                res.append(home)
                answer.append(res)
            else:
                continue
        return answer
    else:
        return 'Нету в базе'


@dp.message_handler(IsPhone(), state=SearchState.SearchNumber_Q1)
async def search(message: types.Message, state=FSMContext):
    number_object = message.text
    decor_number = re.findall(r'\d+', number_object)
    decor_number = int(''.join(decor_number)[-9:])
    objects = search_by_number(decor_number)
    if objects == 'Маклер':
        await message.answer(f'{objects}')
    elif objects == 'Нету в базе':
        await message.answer('Номера нету в базе данных')
    else:
        await message.answer('Все варианты найденые по номеру телефона:')
        for obj in objects:
            await message.answer(f"Номер телефона:  {obj[0]}\n"
                                 f"ID:  {obj[1]}\n"
                                 f"Квартал/Район:  {obj[2]}\n"
                                 f"Ориентир:  {obj[3]}\n"
                                 f"Квартира:  {obj[4]}\n"
                                 f"Дом:  {obj[5]}\n"
                                 )

    await message.answer(f"Выберите нужный вам вариант", reply_markup=kb_go_start)
    await SearchState.SearchNumber_Q2.set()


@dp.message_handler(Text(equals='Повторить запрос'), state=SearchState.SearchNumber_Q2)
async def go_to_start(message: types.Message, state=FSMContext):
    await message.answer('Введите номер телфона', reply_markup=ReplyKeyboardRemove())
    await SearchState.SearchNumber_Q1.set()


@dp.message_handler(Text(equals='Перейти в главное меню'), state=SearchState.SearchNumber_Q2)
async def go_to_start(message: types.Message, state=FSMContext):
    await message.answer('Что тебе нужно?',
                         reply_markup=kb_main_menu)
    await state.reset_state()
