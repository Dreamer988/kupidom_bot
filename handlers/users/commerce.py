import os

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.commerce import kb_district, kb_location_the_road, kb_traffic_level, kb_distance_to_metro, \
    kb_toilet, kb_furniture, kb_technics, kb_number_of_buildings, kb_yes_or_no, kb_side_building, kb_type_parking, \
    kb_main_menu, kb_security, kb_repair, kb_type_of_building, kb_completed_building, kb_non_residential, \
    kb_freestanding
from loader import dp
from states import MenuState, CommerceState
from datetime import date

from pprint import pprint

import googleapiclient.discovery
import httplib2
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()


def google_sendler(sheet_id, start_col, end_col, array_data):
    CREDENTAILS_FILE = '../../creds.json'
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTAILS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)
    spreadsheet_id = sheet_id

    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range="A:A",
        majorDimension="COLUMNS"
    ).execute()
    pprint(values['values'][0])
    pprint(len(values['values'][0]))
    start_range = len(values['values'][0]) + 1
    sheet_range = f"{start_col}{start_range}:{end_col}{start_range}"

    values = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=f"A{start_range}",
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


# Отслеживаем сообщение по фильтру состояния MenuState.Q3
@dp.message_handler(text="Коммерция", state=MenuState.Q3)
async def select_district(message: types.Message, state=FSMContext):
    # Получаем текст сообщения, а после записываем значение в переменную district
    type_of_service = message.text

    # Записываем полученное значение в словарь машины состояний под ключом var_type_of_service
    await state.update_data(var_type_of_service=type_of_service)
    # Отправляем сообщение и массив кнопок
    await message.answer("Выберите район", reply_markup=kb_district)
    # Переходим в машину состояний ApartmentState
    await CommerceState.first()


# Состояние ApartmentState.Q1  -->  Выберите район
@dp.message_handler(state=CommerceState.Q1)
async def select_district(message: types.Message, state=FSMContext):
    district = message.text

    await state.update_data(var_district=district)
    await message.answer("Укажите ориентир", reply_markup=ReplyKeyboardRemove())
    await CommerceState.next()


# Состояние ApartmentState.Q2  -->  Укажите ориентир
@dp.message_handler(state=CommerceState.Q2)
async def select_district(message: types.Message, state=FSMContext):
    reference_point = message.text

    await state.update_data(var_reference_point=reference_point)
    await message.answer("Укажите улицу на которой находится объект", reply_markup=ReplyKeyboardRemove())
    await CommerceState.next()


# Состояние ApartmentState.Q3  -->  Укажите улицу на которой находится объект
@dp.message_handler(state=CommerceState.Q3)
async def select_district(message: types.Message, state=FSMContext):
    street = message.text

    await state.update_data(var_street=street)
    await message.answer("Укажите номер дома", reply_markup=ReplyKeyboardRemove())
    await CommerceState.next()


# Состояние ApartmentState.Q4  -->  Укажите номер дома
@dp.message_handler(state=CommerceState.Q4)
async def select_district(message: types.Message, state=FSMContext):
    number_home = message.text

    await state.update_data(var_number_home=number_home)
    await message.answer("Укажите номер квартиры", reply_markup=ReplyKeyboardRemove())
    await CommerceState.next()


# Состояние ApartmentState.Q5  -->  Укажите номер квартиры
@dp.message_handler(state=CommerceState.Q5)
async def select_district(message: types.Message, state=FSMContext):
    number_apartment = message.text

    await state.update_data(var_number_apartment=number_apartment)
    await message.answer("Выберите расположение от дороги", reply_markup=kb_location_the_road)
    await CommerceState.next()


# Состояние ApartmentState.Q6  -->  Выберите расположение от дороги
@dp.message_handler(state=CommerceState.Q6)
async def select_district(message: types.Message, state=FSMContext):
    location_the_road = message.text

    await state.update_data(var_location_the_road=location_the_road)
    await message.answer("Выберите уровень проходимости", reply_markup=kb_traffic_level)
    await CommerceState.next()


# Состояние ApartmentState.Q7  -->  Выберите уровень проходимости
@dp.message_handler(state=CommerceState.Q7)
async def select_district(message: types.Message, state=FSMContext):
    traffic_level = message.text

    await state.update_data(var_traffic_level=traffic_level)
    await message.answer("Выберите расстояние до метро", reply_markup=kb_distance_to_metro)
    await CommerceState.next()


# Состояние ApartmentState.Q8  -->  Выберите расстояние до метро
@dp.message_handler(state=CommerceState.Q8)
async def select_district(message: types.Message, state=FSMContext):
    distance_to_metro = message.text

    await state.update_data(var_distance_to_metro=distance_to_metro)
    await message.answer("Укажите инфраструктуру (дет.сад, магазин, больницы, транспортная развязка и т.д.)",
                         reply_markup=ReplyKeyboardRemove())
    await CommerceState.next()


# Состояние ApartmentState.Q9  -->  Укажите инфраструктуру (дет.сад, магазин, больницы, транспортная развязка и т.д.)
@dp.message_handler(state=CommerceState.Q9)
async def select_district(message: types.Message, state=FSMContext):
    infrastructure = message.text

    await state.update_data(var_infrastructure=infrastructure)
    await message.answer("Укажите количество комнат", reply_markup=ReplyKeyboardRemove())
    await CommerceState.next()


# Состояние ApartmentState.Q10  -->  Укажите количество комнат
@dp.message_handler(state=CommerceState.Q10)
async def select_district(message: types.Message, state=FSMContext):
    counter_room = message.text

    await state.update_data(var_counter_room=counter_room)
    await message.answer("Укажите этаж", reply_markup=ReplyKeyboardRemove())
    await CommerceState.next()


# Состояние ApartmentState.Q11  -->  Укажите этаж
@dp.message_handler(state=CommerceState.Q11)
async def select_district(message: types.Message, state=FSMContext):
    floor = message.text

    await state.update_data(var_floor=floor)
    await message.answer("Укажите этажность", reply_markup=ReplyKeyboardRemove())
    await CommerceState.next()


# Состояние ApartmentState.Q12  -->  Укажите этажность
@dp.message_handler(state=CommerceState.Q12)
async def select_district(message: types.Message, state=FSMContext):
    number_floor = message.text

    await state.update_data(var_number_floor=number_floor)
    await message.answer("Выберите количество сан. узлов", reply_markup=kb_toilet)
    await CommerceState.next()


# Состояние ApartmentState.Q13  -->  Выберите количество сан. узлов
@dp.message_handler(state=CommerceState.Q13)
async def select_district(message: types.Message, state=FSMContext):
    counter_dress = message.text

    await state.update_data(var_counter_dress=counter_dress)
    await message.answer("Укажите высоту потолков", reply_markup=ReplyKeyboardRemove())
    await CommerceState.next()


# Состояние ApartmentState.Q14  -->  Укажите высоту потолков
@dp.message_handler(state=CommerceState.Q14)
async def select_district(message: types.Message, state=FSMContext):
    ceiling_height = message.text

    await state.update_data(var_ceiling_height=ceiling_height)
    await message.answer("Выберите вариант мебелировки", reply_markup=kb_furniture)
    await CommerceState.next()


# Состояние ApartmentState.Q15  -->  Выберите вариант мебелировки
@dp.message_handler(state=CommerceState.Q15)
async def select_district(message: types.Message, state=FSMContext):
    furniture = message.text

    await state.update_data(var_furniture=furniture)
    await message.answer("Имеется ли наличие техники или оборудования ?", reply_markup=kb_technics)
    await CommerceState.next()


# Состояние ApartmentState.Q16  -->  Имеется ли наличие техники или оборудования ?
@dp.message_handler(state=CommerceState.Q16)
async def select_district(message: types.Message, state=FSMContext):
    technics = message.text

    await state.update_data(var_technics=technics)
    await message.answer("Укажите дополнительное оборудование если оно имеется", reply_markup=ReplyKeyboardRemove())
    await CommerceState.next()


# Состояние ApartmentState.Q17  -->  Укажите дополнительное оборудование если оно имеется
@dp.message_handler(state=CommerceState.Q17)
async def select_district(message: types.Message, state=FSMContext):
    add_technics = message.text

    await state.update_data(var_add_technics=add_technics)
    await message.answer("Укажите общую площадь (м2)", reply_markup=ReplyKeyboardRemove())
    await CommerceState.next()


# Состояние ApartmentState.Q18  -->  Укажите общую площадь (м2)
@dp.message_handler(state=CommerceState.Q18)
async def select_district(message: types.Message, state=FSMContext):
    commerce_area = message.text

    await state.update_data(var_commerce_area=commerce_area)
    await message.answer("Укажите полезную площадь (м2)", reply_markup=ReplyKeyboardRemove())
    await CommerceState.next()


# Состояние ApartmentState.Q19  -->  Укажите полезную площадь (м2)
@dp.message_handler(state=CommerceState.Q19)
async def select_district(message: types.Message, state=FSMContext):
    effective_area = message.text

    await state.update_data(var_effective_area=effective_area)
    await message.answer("Укажите общую площадь земли (м2)", reply_markup=ReplyKeyboardRemove())
    await CommerceState.next()


# Состояние ApartmentState.Q20  -->  Укажите общую площадь земли (м2)
@dp.message_handler(state=CommerceState.Q20)
async def select_district(message: types.Message, state=FSMContext):
    land_area = message.text

    await state.update_data(var_land_area=land_area)
    await message.answer("Опишите территорию", reply_markup=ReplyKeyboardRemove())
    await CommerceState.next()


# Состояние ApartmentState.Q21  -->  Опишите территорию
@dp.message_handler(state=CommerceState.Q21)
async def select_district(message: types.Message, state=FSMContext):
    desc_territory = message.text

    await state.update_data(var_desc_territory=desc_territory)
    await message.answer("Выберите количество строений", reply_markup=kb_number_of_buildings)
    await CommerceState.next()


# Состояние ApartmentState.Q22  -->  Выберите количество строений
@dp.message_handler(state=CommerceState.Q22)
async def select_district(message: types.Message, state=FSMContext):
    number_of_buildings = message.text

    await state.update_data(var_desc_territory=number_of_buildings)
    await message.answer("Имеется ли дополнительная территория ?", reply_markup=kb_yes_or_no)
    await CommerceState.next()


# Состояние ApartmentState.Q23  -->  Имеется ли дополнительная территория ?
@dp.message_handler(state=CommerceState.Q23)
async def select_district(message: types.Message, state=FSMContext):
    add_territory = message.text

    await state.update_data(var_add_territory=add_territory)
    await message.answer("Выберите расположение", reply_markup=kb_side_building)
    await CommerceState.next()


# Состояние ApartmentState.Q24  -->  Выберите расположение
@dp.message_handler(state=CommerceState.Q24)
async def select_district(message: types.Message, state=FSMContext):
    side_building = message.text

    await state.update_data(var_side_building=side_building)
    await message.answer("Выберите вариант парковки", reply_markup=kb_type_parking)
    await CommerceState.next()


# Состояние ApartmentState.Q25  -->  Выберите вариант парковки
@dp.message_handler(state=CommerceState.Q25)
async def select_district(message: types.Message, state=FSMContext):
    type_parking = message.text

    await state.update_data(var_type_parking=type_parking)
    await message.answer("Выберите уровень безопасности", reply_markup=kb_security)
    await CommerceState.next()


# Состояние ApartmentState.Q26  -->  Выберите уровень безопасности
@dp.message_handler(state=CommerceState.Q26)
async def select_district(message: types.Message, state=FSMContext):
    security = message.text

    await state.update_data(var_security=security)
    await message.answer("Выберите состояние ремонта", reply_markup=kb_repair)
    await CommerceState.next()


# Состояние ApartmentState.Q27  -->  Выберите состояние ремонта
@dp.message_handler(state=CommerceState.Q27)
async def select_district(message: types.Message, state=FSMContext):
    type_repair = message.text

    await state.update_data(var_type_repair=type_repair)
    await message.answer("Выберите тип строения", reply_markup=kb_type_of_building)
    await CommerceState.next()


# Состояние ApartmentState.Q28  -->  Выберите тип строения
@dp.message_handler(state=CommerceState.Q28)
async def select_district(message: types.Message, state=FSMContext):
    type_of_building = message.text

    await state.update_data(var_type_of_building=type_of_building)
    await message.answer("Завершено ли строительство дома?", reply_markup=kb_completed_building)
    await CommerceState.next()


# Состояние ApartmentState.Q29  -->  Завершено ли строительство дома?
@dp.message_handler(state=CommerceState.Q29)
async def select_district(message: types.Message, state=FSMContext):
    completed_building = message.text

    await state.update_data(var_completed_building=completed_building)
    await message.answer("Переведён ли в нежилое ?", reply_markup=kb_non_residential)
    await CommerceState.next()


# Состояние ApartmentState.Q30  -->  Завершено ли строительство дома?
@dp.message_handler(state=CommerceState.Q30)
async def select_district(message: types.Message, state=FSMContext):
    non_residential = message.text

    await state.update_data(var_non_residential=non_residential)
    await message.answer("Здание", reply_markup=kb_freestanding)
    await CommerceState.next()


# Состояние ApartmentState.Q31  -->  Здание
@dp.message_handler(state=CommerceState.Q31)
async def select_district(message: types.Message, state=FSMContext):
    freestanding = message.text

    await state.update_data(var_freestanding=freestanding)
    await message.answer("Сейчас вам надо будет выбрать под какие назначения подходит коммерческое помещение.")
    await message.answer("Выберите назначение")
    await CommerceState.next()

# __________________________________________________________________________________________
# __________________________________________________________________________________________
# __________________________________________________________________________________________
# Состояние ApartmentState.Q42  -->  Рекламировать на торговых площадках ?
# @dp.message_handler(state=CommerceState.Q42)
# async def select_district(message: types.Message, state=FSMContext):
#     public = message.text
#
#     await state.update_data(var_public=public)
#     await message.answer(f"Все заполнил(-а) правильно ?", reply_markup=kb_yes_or_no)
#     await CommerceState.next()
#
#
# # Состояние ApartmentState.Q43  -->  Все заполнил(-а) правильно ?
# @dp.message_handler(state=CommerceState.Q43)
# async def select_district(message: types.Message, state=FSMContext):
#     filled_in_correctly = message.text
#     answer = await state.get_data()
#     user_name = message.from_user.first_name
#
#     if filled_in_correctly.lower() == 'да':
#         dt_time = str(date.today())
#         answer = await state.get_data()
#         list_answer = []
#         list_answer.append(answer['var_type_of_property'])
#         list_answer.append(answer['var_quarter'])
#         list_answer.append(answer['var_reference_point'])
#         list_answer.append(answer['var_street'])
#         list_answer.append(answer['var_counter_room'])
#         list_answer.append(answer['var_floor'])
#         list_answer.append(answer['var_number_floor'])
#         list_answer.append(answer['var_apartment_area'])
#         list_answer.append(answer['var_balcony_size'])
#         list_answer.append(answer['var_type_dress'])
#         list_answer.append(answer['var_repair'])
#         list_answer.append(answer['var_type_building'])
#         list_answer.append(answer['var_apartment_layout'])
#         list_answer.append(answer['var_type_layout'])
#         list_answer.append(answer['var_side_building'])
#         list_answer.append(answer['var_ceiling_height'])
#         list_answer.append(answer['var_furniture'])
#         list_answer.append(answer['var_technics'])
#         list_answer.append(answer['var_condition'])
#         list_answer.append(answer['var_kitchen_area'])
#         list_answer.append(answer['var_plastic_windows'])
#         list_answer.append(answer['var_price'])
#         list_answer.append(answer['var_full_price'])
#         list_answer.append(answer['var_owner'])
#         list_answer.append(answer['var_number_phone'])
#         list_answer.append(answer['var_additional_number_phone'])
#         list_answer.append(' ')
#         list_answer.append(answer['var_location_the_road'])
#         list_answer.append(answer['var_distance_to_metro'])
#         list_answer.append(answer['var_number_apartment'])
#         list_answer.append(answer['var_number_home'])
#         list_answer.append(' ')
#         list_answer.append(' ')
#         list_answer.append(user_name)
#         list_answer.append(dt_time)
#         list_answer.append(dt_time)
#         list_answer.append(answer['var_informant'])
#         list_answer.append(' ')
#         list_answer.append(answer['var_district'])
#         list_answer.append(answer['var_infrastructure'])
#         list_answer.append(answer['var_redevelopment'])
#         list_answer.append(answer['var_type_parking'])
#         list_answer.append(answer['var_description'])
#         list_answer.append(answer['var_elevator_condition'])
#         list_answer.append(answer['var_roof_condition'])
#         list_answer.append(answer['var_checkout_time'])
#         list_answer.append(answer['var_scribed_people'])
#         list_answer.append(answer['var_under_to_office'])
#         list_answer.append(answer['var_exclusive'])
#         list_answer.append(answer['var_public'])
#         google_sendler('1-B80joNKTOSTIJRLiACOcfH1E3dH5yrNPbS-CU5Bvxc', 'A', 'AX', list_answer)
#         await message.answer('Ваша объективка отправлена)', reply_markup=kb_main_menu)
#         await state.reset_state()
#     elif filled_in_correctly.lower() == 'нет':
#         await state.update_data(var_filled_in_correctly=filled_in_correctly)
#     else:
#         await message.answer('Отправлено не верное значение( Попробуйте снова')
