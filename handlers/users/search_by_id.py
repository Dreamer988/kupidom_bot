import os

from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
import googleapiclient.discovery
import httplib2
from aiogram import types
from aiogram.dispatcher import FSMContext
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials
import time

from keyboards.default.apartment import kb_main_menu
from keyboards.default.search import kb_go_start, kb_word_object
from loader import dp
from states import SearchState

load_dotenv()

CREDENTAILS_FILE = os.getenv('CREDENTAILS_FILE')
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTAILS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)
spreadsheet_id = "1mev3u2Pe4xF73waNj7wg4m8RAaNI2Pr6uxKYQHxu14I"


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


def verified_time_data(user_id, user_name):
    global base_day
    global base_hour
    global count_day
    global count_hour
    global point_sheet

    data_offset_sheets = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=f"Home!A:F",
        majorDimension="COLUMNS"
    ).execute()
    ver = True
    data_id = data_offset_sheets['values'][0]
    point_sheet = 0
    for id in data_id:
        if str(id) == str(user_id):
            base_day = data_offset_sheets['values'][2][point_sheet]  # Получаем последнюю дату запроса с таблиц (день)
            base_hour = data_offset_sheets['values'][3][point_sheet]  # Получаем последнюю дату запроса с таблиц (час)
            count_day = data_offset_sheets['values'][1][point_sheet]  # Получаем сколько уже зопрошено объектов в день
            count_hour = data_offset_sheets['values'][4][point_sheet]  # Получаем сколько уже зопрошено объектов в час
            ver = False
            break
        else:
            point_sheet += 1
            continue
    if ver:
        return "Вас нету в базе данных ID"

    data_time = time.time()  # Время в секундах с 1970 года
    hour = int(float(data_time / 60 / 60))
    day = int(float(hour / 24))
    limit_day = 33
    limit_hour = 10

    if int(base_day) < int(day):
        new_data_day = service.spreadsheets().values().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body={
                "value_input_option": 'USER_ENTERED',
                "data": [
                    {
                        "range": f'Home!A{point_sheet + 1}:F',
                        "majorDimension": "ROWS",
                        "values": [[user_id, 1, day, hour, 1, user_name]]
                    }
                ]
            }
        ).execute()
        return True
    elif int(base_hour) < int(hour):
        new_data_hour = service.spreadsheets().values().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body={
                "value_input_option": 'USER_ENTERED',
                "data": [
                    {
                        "range": f'Home!A{point_sheet + 1}:F',
                        "majorDimension": "ROWS",
                        "values": [[user_id, count_day, day, hour, 1, user_name]]
                    }
                ]
            }
        ).execute()
        return True
    elif int(count_day) > limit_day:
        return 'Вы превысили лимит в день'
    elif int(count_hour) > limit_hour:
        return 'Вы превысили лимит в день'
    else:
        return True


# Квартиры
def search_by_id_apartment(id_object, user_id, user_name):
    verified = verified_time_data(user_id, user_name)
    sheet = service.spreadsheets().values().get(
        spreadsheetId='1_OlIeV7jYMN5H6zXZOqVsKrfuDjlJwpkhGoIjOQIUkg',
        range=f"Общая база!A:BE",
        majorDimension="ROWS"
    ).execute()
    objects = sheet['values']
    if verified == True:
        for object in objects:
            if str(object[0]) == str(id_object):
                answer = f'ID:  {object[0]}\n' \
                         f'Квартал:  {object[1]}\n' \
                         f'Ориентиры:  {object[2]}\n' \
                         f'Улица:  {object[3]}\n' \
                         f'Номер дома:  {object[29]}\n' \
                         f'Номер квартиры:  {object[30]}\n' \
                         f'Кол-во комнат:  {object[4]}\n' \
                         f'Этаж:  {object[5]}\n' \
                         f'Этаж-сть:  {object[6]}\n' \
                         f'S общая:  {object[7]}\n' \
                         f'Балкон:  {object[8]}\n' \
                         f'Сан.узел:  {object[9]}\n' \
                         f'Ремонт:  {object[10]}\n' \
                         f'Тип строения:  {object[11]}\n' \
                         f'Планировка:  {object[12]}\n' \
                         f'Тип постройки:  {object[13]}\n' \
                         f'Высота потолков:  {object[15]}\n' \
                         f'Мебель:  {object[16]}\n' \
                         f'Техника:  {object[17]}\n' \
                         f'Стартовая цена:  {object[21]}\n' \
                         f'Цена:  {object[22]}\n' \
                         f'Имя собственника:  {object[23]}\n' \
                         f'Номер телефона:  {object[24]}\n' \
                         f'Доп.номер телефона:  {object[25]}\n' \
                         f'Вариант:  {object[35]}\n' \
                         f'Ссылка на сайт:  {object[51]}\n'

                add_request = service.spreadsheets().values().batchUpdate(
                    spreadsheetId=spreadsheet_id,
                    body={
                        "value_input_option": 'USER_ENTERED',
                        "data": [
                            {
                                "range": f'Home!A{point_sheet + 1}:F',
                                "majorDimension": "ROWS",
                                "values": [
                                    [user_id, str(int(count_day) + 1), base_day, base_hour, str(int(count_hour) + 1),
                                     user_name]]
                            }
                        ]
                    }
                ).execute()
                return answer
            else:
                continue
        return 'Объекта нету в базе'
    else:
        return verified


# Коммерция
def search_by_id_commerce(id_object, user_id, user_name):
    verified = verified_time_data(user_id, user_name)
    sheet = service.spreadsheets().values().get(
        spreadsheetId='1Q2jSOeCYi2FPVs0gI7vLQVljw1DfYKBHdUq7HpZVz4k',
        range=f"Общая база!A:BE",
        majorDimension="ROWS"
    ).execute()
    objects = sheet['values']
    if verified == True:
        for object in objects:
            if str(object[0]) == str(id_object):
                answer = f'ID:  {object[0]}\n' \
                         f'Район:  {object[1]}\n' \
                         f'Ориентиры:  {object[2]}\n' \
                         f'Улица:  {object[3]}\n' \
                         f'Номер дома:  {object[31]}\n' \
                         f'Кол-во комнат:  {object[4]}\n' \
                         f'Этаж:  {object[5]}\n' \
                         f'Этаж-сть:  {object[6]}\n' \
                         f'S общая:  {object[7]}\n' \
                         f'S полезная:  {object[8]}\n' \
                         f'Площадь земли:  {object[14]}\n' \
                         f'Ремонт:  {object[9]}\n' \
                         f'Назначение:  {object[12]}\n' \
                         f'Тип строения:  {object[10]}\n' \
                         f'Тип недвижимости:  {object[11]}\n' \
                         f'Количество строений:  {object[13]}\n' \
                         f'Переведено в нежилое:  {object[15]}\n' \
                         f'Высота потолков:  {object[16]}\n' \
                         f'Проходимость:  {object[18]}\n' \
                         f'Завершенное строительство:  {object[21]}\n' \
                         f'Стартовая цена:  {object[23]}\n' \
                         f'Цена:  {object[24]}\n' \
                         f'Имя собственника:  {object[25]}\n' \
                         f'Номер телефона:  {object[26]}\n' \
                         f'Доп.номер телефона:  {object[27]}\n' \
                         f'Вариант:  {object[38]}\n' \
                         f'Ссылка на сайт:  {object[42]}\n'

                add_request = service.spreadsheets().values().batchUpdate(
                    spreadsheetId=spreadsheet_id,
                    body={
                        "value_input_option": 'USER_ENTERED',
                        "data": [
                            {
                                "range": f'Home!A{point_sheet + 1}:F',
                                "majorDimension": "ROWS",
                                "values": [
                                    [user_id, str(int(count_day) + 1), base_day, base_hour, str(int(count_hour) + 1),
                                     user_name]]
                            }
                        ]
                    }
                ).execute()
                return answer
            else:
                continue
        return 'Объекта нету в базе'
    else:
        return verified


# Дома
def search_by_id_home(id_object, user_id, user_name):
    verified = verified_time_data(user_id, user_name)
    sheet = service.spreadsheets().values().get(
        spreadsheetId='1zLwG9oJQU3wHSe0OQgOO27v7EDF_CCWrRVji1qr3dqs',
        range=f"Общая база!A:BE",
        majorDimension="ROWS"
    ).execute()
    objects = sheet['values']
    if verified == True:
        for object in objects:
            if str(object[0]) == str(id_object):
                answer = f'ID:  {object[0]}\n' \
                         f'Район:  {object[1]}\n' \
                         f'Ориентиры:  {object[2]}\n' \
                         f'Улица:  {object[3]}\n' \
                         f'Номер дома:  {object[28]}\n' \
                         f'Кол-во комнат:  {object[4]}\n' \
                         f'Жилых комнат:  {object[5]}\n' \
                         f'Этаж-сть:  {object[6]}\n' \
                         f'S участка:  {object[7]}\n' \
                         f'S дома:  {object[8]}\n' \
                         f'Форма участка:  {object[9]}\n' \
                         f'Ремонт:  {object[11]}\n' \
                         f'Тип строения:  {object[12]}\n' \
                         f'Вид строительства:  {object[13]}\n' \
                         f'Строительство завершено:  {object[14]}\n' \
                         f'Высота потолков:  {object[16]}\n' \
                         f'Сан.узел:  {object[10]}\n' \
                         f'Мебель:  {object[17]}\n' \
                         f'Техника:  {object[18]}\n' \
                         f'Стартовая цена:  {object[21]}\n' \
                         f'Цена:  {object[22]}\n' \
                         f'Имя собственника:  {object[23]}\n' \
                         f'Номер телефона:  {object[24]}\n' \
                         f'Доп.номер телефона:  {object[25]}\n' \
                         f'Вариант:  {object[32]}\n' \
                         f'Ссылка на сайт:  {object[36]}\n'

                add_request = service.spreadsheets().values().batchUpdate(
                    spreadsheetId=spreadsheet_id,
                    body={
                        "value_input_option": 'USER_ENTERED',
                        "data": [
                            {
                                "range": f'Home!A{point_sheet + 1}:F',
                                "majorDimension": "ROWS",
                                "values": [
                                    [user_id, str(int(count_day) + 1), base_day, base_hour, str(int(count_hour) + 1),
                                     user_name]]
                            }
                        ]
                    }
                ).execute()
                return answer
            else:
                continue
        return 'Объекта нету в базе'
    else:
        return verified


# Аренда Квартиры
def search_by_id_apartment_rent(id_object, user_id, user_name):
    verified = verified_time_data(user_id, user_name)
    sheet = service.spreadsheets().values().get(
        spreadsheetId='1KA7eydXuGpmPDrYWisGQOnGHpeXEnlCv2ciBEcOMxNw',
        range=f"Квартиры!A:BE",
        majorDimension="ROWS"
    ).execute()
    objects = sheet['values']
    if verified == True:
        for object in objects:
            if str(object[0]) == str(id_object):
                answer = f'ID:  {object[0]}\n' \
                         f'Квартал:  {object[1]}\n' \
                         f'Ориентиры:  {object[2]}\n' \
                         f'Улица:  {object[3]}\n' \
                         f'Номер дома:  {object[33]}\n' \
                         f'Номер квартиры:  {object[34]}\n' \
                         f'Кол-во комнат:  {object[4]}\n' \
                         f'Этаж:  {object[5]}\n' \
                         f'Этаж-сть:  {object[6]}\n' \
                         f'S общая:  {object[7]}\n' \
                         f'Балкон:  {object[8]}\n' \
                         f'Сан.узел:  {object[9]}\n' \
                         f'Ремонт:  {object[10]}\n' \
                         f'Тип строения:  {object[11]}\n' \
                         f'Планировка:  {object[12]}\n' \
                         f'Тип постройки:  {object[13]}\n' \
                         f'Высота потолков:  {object[28]}\n' \
                         f'Мебель:  {object[15]}\n' \
                         f'Техника:  {object[16]}\n' \
                         f'Кондиционер:  {object[17]}\n' \
                         f'Цена ежемесячная:  {object[20]}\n' \
                         f'Депозит:  {object[21]}\n' \
                         f'Предоплата:  {object[22]}\n' \
                         f'Комунальные:  {object[23]}\n' \
                         f'Имя собственника:  {object[24]}\n' \
                         f'Номер телефона:  {object[25]}\n' \
                         f'Доп.номер телефона:  {object[26]}\n' \
                         f'Вариант:  {object[37]}\n' \
                         f'Ссылка на сайт:  {object[41]}\n'

                add_request = service.spreadsheets().values().batchUpdate(
                    spreadsheetId=spreadsheet_id,
                    body={
                        "value_input_option": 'USER_ENTERED',
                        "data": [
                            {
                                "range": f'Home!A{point_sheet + 1}:F',
                                "majorDimension": "ROWS",
                                "values": [
                                    [user_id, str(int(count_day) + 1), base_day, base_hour, str(int(count_hour) + 1),
                                     user_name]]
                            }
                        ]
                    }
                ).execute()
                return answer
            else:
                continue
        return 'Объекта нету в базе'
    else:
        return verified


# Аренда Коммерция
def search_by_id_commerce_rent(id_object, user_id, user_name):
    verified = verified_time_data(user_id, user_name)
    sheet = service.spreadsheets().values().get(
        spreadsheetId='1KA7eydXuGpmPDrYWisGQOnGHpeXEnlCv2ciBEcOMxNw',
        range=f"Коммерция!A:BE",
        majorDimension="ROWS"
    ).execute()
    objects = sheet['values']
    if verified == True:
        for object in objects:
            if str(object[0]) == str(id_object):
                answer = f'ID:  {object[0]}\n' \
                         f'Район:  {object[1]}\n' \
                         f'Ориентиры:  {object[3]}\n' \
                         f'Улица:  {object[2]}\n' \
                         f'Номер дома:  {object[32]}\n' \
                         f'Кол-во комнат:  {object[4]}\n' \
                         f'Этаж:  {object[5]}\n' \
                         f'Этаж-сть:  {object[6]}\n' \
                         f'S общая:  {object[8]}\n' \
                         f'S полезная:  {object[9]}\n' \
                         f'Площадь земли:  {object[10]}\n' \
                         f'Ремонт:  {object[11]}\n' \
                         f'Назначение:  {object[15]}\n' \
                         f'Тип строения:  {object[12]}\n' \
                         f'Парковка:  {object[20]}\n' \
                         f'Высота потолков:  {object[16]}\n' \
                         f'Проходимость:  {object[18]}\n' \
                         f'Цена ежемесячная:  {object[22]}\n' \
                         f'Депозит:  {object[23]}\n' \
                         f'Предоплата:  {object[24]}\n' \
                         f'Коммунальные:  {object[25]}\n' \
                         f'Имя собственника:  {object[27]}\n' \
                         f'Номер телефона:  {object[28]}\n' \
                         f'Доп.номер телефона:  {object[29]}\n' \
                         f'Вариант:  {object[36]}\n' \
                         f'Ссылка на сайт:  {object[40]}\n'

                add_request = service.spreadsheets().values().batchUpdate(
                    spreadsheetId=spreadsheet_id,
                    body={
                        "value_input_option": 'USER_ENTERED',
                        "data": [
                            {
                                "range": f'Home!A{point_sheet + 1}:F',
                                "majorDimension": "ROWS",
                                "values": [
                                    [user_id, str(int(count_day) + 1), base_day, base_hour, str(int(count_hour) + 1),
                                     user_name]]
                            }
                        ]
                    }
                ).execute()
                return answer
            else:
                continue
        return 'Объекта нету в базе'
    else:
        return verified


# Аренда Дома
def search_by_id_home_rent(id_object, user_id, user_name):
    verified = verified_time_data(user_id, user_name)
    sheet = service.spreadsheets().values().get(
        spreadsheetId='1KA7eydXuGpmPDrYWisGQOnGHpeXEnlCv2ciBEcOMxNw',
        range=f"Дома!A:BE",
        majorDimension="ROWS"
    ).execute()
    objects = sheet['values']
    if verified == True:
        for object in objects:
            if str(object[0]) == str(id_object):
                answer = f'ID:  {object[0]}\n' \
                         f'Район:  {object[1]}\n' \
                         f'Ориентиры:  {object[3]}\n' \
                         f'Улица:  {object[2]}\n' \
                         f'Номер дома:  {object[28]}\n' \
                         f'Кол-во комнат:  {object[4]}\n' \
                         f'Жилых комнат:  {object[5]}\n' \
                         f'Этаж-сть:  {object[6]}\n' \
                         f'S участка:  {object[7]}\n' \
                         f'S дома:  {object[8]}\n' \
                         f'Ремонт:  {object[10]}\n' \
                         f'Тип строения:  {object[11]}\n' \
                         f'Арендатор:  {object[12]}\n' \
                         f'Высота потолков:  {object[14]}\n' \
                         f'Сан.узел:  {object[9]}\n' \
                         f'Мебель:  {object[15]}\n' \
                         f'Техника:  {object[16]}\n' \
                         f'Цена ежемесячная:  {object[19]}\n' \
                         f'Депозит:  {object[20]}\n' \
                         f'Предоплата:  {object[21]}\n' \
                         f'Комунальные:  {object[22]}\n' \
                         f'Имя собственника:  {object[23]}\n' \
                         f'Номер телефона:  {object[24]}\n' \
                         f'Доп.номер телефона:  {object[25]}\n' \
                         f'Вариант:  {object[31]}\n' \
                         f'Ссылка на сайт:  {object[35]}\n'

                add_request = service.spreadsheets().values().batchUpdate(
                    spreadsheetId=spreadsheet_id,
                    body={
                        "value_input_option": 'USER_ENTERED',
                        "data": [
                            {
                                "range": f'Home!A{point_sheet + 1}:F',
                                "majorDimension": "ROWS",
                                "values": [
                                    [user_id, str(int(count_day) + 1), base_day, base_hour, str(int(count_hour) + 1),
                                     user_name]]
                            }
                        ]
                    }
                ).execute()
                return answer
            else:
                continue
        return 'Объекта нету в базе'
    else:
        return verified


@dp.message_handler(state=SearchState.SearchId_Q1)
async def get_object_word(message: types.Message, state=FSMContext):
    word_object = message.text
    await state.update_data(var_word_id=word_object)
    await message.answer('Введите ID объекта', reply_markup=ReplyKeyboardRemove())
    await SearchState.SearchId_Q2.set()


@dp.message_handler(state=SearchState.SearchId_Q2)
async def get_id_object(message: types.Message, state=FSMContext):
    id_object = message.text
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    if len(id_object) >= 6:
        data = await state.get_data()
        word_object = data['var_word_id']

        if word_object == 'К' or word_object == 'Н' or word_object == 'И':
            await message.answer(f"Поиск в базе квартир...")
            answer = search_by_id_apartment(id_object, user_id, user_name)
            await message.answer(f"{answer}")
            await message.answer(f"Выберите нужный вам вариант", reply_markup=kb_go_start)
            await SearchState.SearchId_Q3.set()

        elif word_object == 'КМ':
            await message.answer(f"Поиск в базе коммерции...")
            answer = search_by_id_commerce(id_object, user_id, user_name)
            await message.answer(f"{answer}")
            await message.answer(f"Выберите нужный вам вариант", reply_markup=kb_go_start)
            await SearchState.SearchId_Q3.set()

        elif word_object == 'Д':
            await message.answer(f"Поиск в базе домов...")
            answer = search_by_id_home(id_object, user_id, user_name)
            await message.answer(f"{answer}")
            await message.answer(f"Выберите нужный вам вариант", reply_markup=kb_go_start)
            await SearchState.SearchId_Q3.set()

        elif word_object == 'АК':
            await message.answer(f"Поиск в базе аренды квартир...")
            answer = search_by_id_apartment_rent(id_object, user_id, user_name)
            await message.answer(f"{answer}")
            await message.answer(f"Выберите нужный вам вариант", reply_markup=kb_go_start)
            await SearchState.SearchId_Q3.set()

        elif word_object == 'АКМ':
            await message.answer(f"Поиск в базе аренды коммерции...")
            answer = search_by_id_commerce_rent(id_object, user_id, user_name)
            await message.answer(f"{answer}")
            await message.answer(f"Выберите нужный вам вариант", reply_markup=kb_go_start)
            await SearchState.SearchId_Q3.set()

        elif word_object == 'АД':
            await message.answer(f"Поиск в базе аренды домов...")
            answer = search_by_id_home_rent(id_object, user_id, user_name)
            await message.answer(f"{answer}")
            await message.answer(f"Выберите нужный вам вариант", reply_markup=kb_go_start)
            await SearchState.SearchId_Q3.set()

    else:
        await message.answer(f"Пожалуйста введите корректный ID...")
        await message.answer(f"Выберите нужный вам вариант", reply_markup=kb_go_start)
        await SearchState.SearchId_Q3.set()


@dp.message_handler(Text(equals='Повторить запрос'), state=SearchState.SearchId_Q3)
async def go_to_start(message: types.Message, state=FSMContext):
    await message.answer('Выберите букву объекта:\n'
                         'К - квартира\n'
                         'Н - квартира\n'
                         'И - квартира\n'
                         'КМ - квартира\n'
                         'Д - квартира\n'
                         'АК - квартира\n'
                         'АКМ - квартира\n'
                         'АД - квартира\n'
                         , reply_markup=kb_word_object)
    await SearchState.SearchId_Q1.set()


@dp.message_handler(Text(equals='Перейти в главное меню'), state=SearchState.SearchId_Q3)
async def go_to_start(message: types.Message, state=FSMContext):
    await message.answer('Что тебе нужно?',
                         reply_markup=kb_main_menu)
    await state.reset_state()
