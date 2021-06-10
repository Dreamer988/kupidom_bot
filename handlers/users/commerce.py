import os
from datetime import date

import googleapiclient.discovery
import httplib2
from aiogram import types
from aiogram.dispatcher import FSMContext
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials

from keyboards.default.commerce import kb_district, kb_location_the_road, kb_traffic_level, kb_distance_to_metro, \
    kb_toilet, kb_furniture, kb_technics, kb_number_of_buildings, kb_yes_or_no, kb_side_building, kb_type_parking, \
    kb_main_menu, kb_security, kb_repair, kb_type_of_building, kb_completed_building, kb_non_residential, \
    kb_freestanding, kb_appointment, kb_tenants, kb_power_supply, kb_sewerage, kb_system_gas, kb_system_heating, \
    kb_business, kb_infrastructure, kb_number_floor, kb_number_room, kb_back
from loader import dp
from states import ObjectState, CommerceState

load_dotenv()


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


# Отслеживаем сообщение по фильтру состояния MenuState.Sale
@dp.message_handler(text="Коммерция", state=ObjectState.Sale)
async def select_district(message: types.Message, state=FSMContext):
    # Получаем текст сообщения, а после записываем значение в переменную district
    type_of_service = message.text

    # Записываем полученное значение в словарь машины состояний под ключом var_type_of_service
    await state.update_data(var_type_of_service=type_of_service)
    # Отправляем сообщение и массив кнопок
    await message.answer("Выберите район", reply_markup=kb_district)
    # Переходим в машину состояний ApartmentState
    await CommerceState.first()


# Состояние CommerceState.Q1  -->  Выберите район
@dp.message_handler(state=CommerceState.Q1)
async def select_district(message: types.Message, state=FSMContext):
    district = message.text

    await state.update_data(var_district=district)
    await message.answer("Укажите ориентир", reply_markup=kb_back)
    await CommerceState.next()


# Состояние CommerceState.Q2  -->  Укажите ориентир
@dp.message_handler(state=CommerceState.Q2)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q1.set()
        await message.answer("Выберите район", reply_markup=kb_district)
    else:
        reference_point = message.text

        await state.update_data(var_reference_point=reference_point)
        await message.answer("Укажите улицу на которой находится объект", reply_markup=kb_back)
        await CommerceState.next()


# Состояние CommerceState.Q3  -->  Укажите улицу на которой находится объект
@dp.message_handler(state=CommerceState.Q3)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q2.set()
        await message.answer("Укажите ориентир", reply_markup=kb_back)
    else:
        street = message.text

        await state.update_data(var_street=street)
        await message.answer("Укажите номер дома", reply_markup=kb_back)
        await CommerceState.next()


# Состояние CommerceState.Q4  -->  Укажите номер дома
@dp.message_handler(state=CommerceState.Q4)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q3.set()
        await message.answer("Укажите улицу на которой находится объект", reply_markup=kb_back)
    else:
        number_home = message.text

        await state.update_data(var_number_home=number_home)
        await message.answer("Укажите номер квартиры", reply_markup=kb_back)
        await CommerceState.next()


# Состояние CommerceState.Q5  -->  Укажите номер квартиры
@dp.message_handler(state=CommerceState.Q5)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q4.set()
        await message.answer("Укажите номер дома", reply_markup=kb_back)
    else:
        number_apartment = message.text

        await state.update_data(var_number_apartment=number_apartment)
        await message.answer("Выберите расположение от дороги", reply_markup=kb_location_the_road)
        await CommerceState.next()


# Состояние CommerceState.Q6  -->  Выберите расположение от дороги
@dp.message_handler(state=CommerceState.Q6)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q5.set()
        await message.answer("Укажите номер квартиры", reply_markup=kb_back)
    else:
        location_the_road = message.text

        await state.update_data(var_location_the_road=location_the_road)
        await message.answer("Выберите уровень проходимости", reply_markup=kb_traffic_level)
        await CommerceState.next()


# Состояние CommerceState.Q7  -->  Выберите уровень проходимости
@dp.message_handler(state=CommerceState.Q7)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q6.set()
        await message.answer("Выберите расположение от дороги", reply_markup=kb_location_the_road)
    else:
        traffic_level = message.text

        await state.update_data(var_traffic_level=traffic_level)
        await message.answer("Выберите расстояние до метро", reply_markup=kb_distance_to_metro)
        await CommerceState.next()


# Состояние CommerceState.Q8  -->  Выберите расстояние до метро
@dp.message_handler(state=CommerceState.Q8)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q7.set()
        await message.answer("Выберите уровень проходимости", reply_markup=kb_traffic_level)
    else:
        distance_to_metro = message.text

        await state.update_data(var_distance_to_metro=distance_to_metro)
        await message.answer("Укажите инфраструктуру (дет.сад, магазин, больницы, транспортная развязка и т.д.)",
                             reply_markup=kb_infrastructure)
        await CommerceState.next()


# Состояние CommerceState.Infrastructure  -->  Укажите инфраструктуру
@dp.message_handler(text="Готово ✅", state=CommerceState.Infrastructure)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q8.set()
        await message.answer("Выберите расстояние до метро", reply_markup=kb_distance_to_metro)
    else:
        answer = await state.get_data()
        infrastructures = answer['var_infrastructures']
        separator = ','
        infrastructures = separator.join(infrastructures)

        await message.answer(f'Инфраструктура которую вы выбрали: {infrastructures}')
        await message.answer("/--/--/--/--/--/--/------/--/--/--/--/--/--/--/")
        await state.update_data(var_infrastructures=infrastructures)

        await message.answer("Укажите количество комнат", reply_markup=kb_number_room)
        await CommerceState.next()


# Состояние CommerceState.Q9  -->  Укажите инфраструктуру (дет.сад, магазин, больницы, транспортная развязка и т.д.)
@dp.message_handler(state=CommerceState.Q9)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q8.set()
        await message.answer("Выберите расстояние до метро", reply_markup=kb_distance_to_metro)
    else:
        infrastructure = message.text
        infrastructures = list()
        infrastructures.append(infrastructure)
        await state.update_data(var_infrastructures=infrastructures)
        await message.answer("Выберите еще варианты или нажмите на кнопку 'Готово ✅", reply_markup=kb_infrastructure)
        await CommerceState.Infrastructure.set()


# Состояние CommerceState.Infrastructure  -->  Повтор
@dp.message_handler(state=CommerceState.Infrastructure)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q8.set()
        await message.answer("Выберите расстояние до метро", reply_markup=kb_distance_to_metro)
    else:
        infrastructure = message.text
        answer = await state.get_data()
        infrastructures = answer['var_infrastructures']
        infrastructures.append(infrastructure)
        await state.update_data(var_infrastructures=infrastructures)
    await message.answer(f"{infrastructures}", reply_markup=kb_infrastructure)


# Состояние CommerceState.Q10  -->  Укажите количество комнат
@dp.message_handler(state=CommerceState.Q10)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q9.set()
        await message.answer("Укажите инфраструктуру (дет.сад, магазин, больницы, транспортная развязка и т.д.)",
                             reply_markup=kb_infrastructure)
    else:
        counter_room = message.text

        await state.update_data(var_counter_room=counter_room)
        await message.answer("Укажите этаж", reply_markup=kb_number_floor)
        await CommerceState.next()


# Состояние CommerceState.Q11  -->  Укажите этаж
@dp.message_handler(state=CommerceState.Q11)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q10.set()
        await message.answer("Укажите количество комнат", reply_markup=kb_number_room)
    else:
        floor = message.text

        await state.update_data(var_floor=floor)
        await message.answer("Укажите этажность", reply_markup=kb_number_floor)
        await CommerceState.next()


# Состояние CommerceState.Q12  -->  Укажите этажность
@dp.message_handler(state=CommerceState.Q12)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q11.set()
        await message.answer("Укажите этаж", reply_markup=kb_number_floor)
    else:
        number_floor = message.text

        await state.update_data(var_number_floor=number_floor)
        await message.answer("Выберите количество сан. узлов", reply_markup=kb_toilet)
        await CommerceState.next()


# Состояние CommerceState.Q13  -->  Выберите количество сан. узлов
@dp.message_handler(state=CommerceState.Q13)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q12.set()
        await message.answer("Укажите этажность", reply_markup=kb_number_floor)
    else:
        counter_dress = message.text

        await state.update_data(var_counter_dress=counter_dress)
        await message.answer("Укажите высоту потолков", reply_markup=kb_back)
        await CommerceState.next()


# Состояние CommerceState.Q14  -->  Укажите высоту потолков
@dp.message_handler(state=CommerceState.Q14)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q13.set()
        await message.answer("Выберите количество сан. узлов", reply_markup=kb_toilet)
    else:
        ceiling_height = message.text

        await state.update_data(var_ceiling_height=ceiling_height)
        await message.answer("Выберите вариант мебелировки", reply_markup=kb_furniture)
        await CommerceState.next()


# Состояние CommerceState.Q15  -->  Выберите вариант мебелировки
@dp.message_handler(state=CommerceState.Q15)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q14.set()
        await message.answer("Укажите высоту потолков", reply_markup=kb_back)
    else:
        furniture = message.text

        await state.update_data(var_furniture=furniture)
        await message.answer("Имеется ли наличие техники или оборудования ?", reply_markup=kb_technics)
        await CommerceState.next()


# Состояние CommerceState.Q16  -->  Имеется ли наличие техники или оборудования ?
@dp.message_handler(state=CommerceState.Q16)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q15.set()
        await message.answer("Выберите вариант мебелировки", reply_markup=kb_furniture)
    else:
        technics = message.text

        await state.update_data(var_technics=technics)
        await message.answer("Укажите дополнительное оборудование если оно имеется", reply_markup=kb_back)
        await CommerceState.next()


# Состояние CommerceState.Q17  -->  Укажите дополнительное оборудование если оно имеется
@dp.message_handler(state=CommerceState.Q17)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q16.set()
        await message.answer("Имеется ли наличие техники или оборудования ?", reply_markup=kb_technics)
    else:
        add_technics = message.text

        await state.update_data(var_add_technics=add_technics)
        await message.answer("Укажите общую площадь (м2)", reply_markup=kb_back)
        await CommerceState.next()


# Состояние CommerceState.Q18  -->  Укажите общую площадь (м2)
@dp.message_handler(state=CommerceState.Q18)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q17.set()
        await message.answer("Укажите дополнительное оборудование если оно имеется", reply_markup=kb_back)
    else:
        commerce_area = message.text

        await state.update_data(var_commerce_area=commerce_area)
        await message.answer("Укажите полезную площадь (м2)", reply_markup=kb_back)
        await CommerceState.next()


# Состояние CommerceState.Q19  -->  Укажите полезную площадь (м2)
@dp.message_handler(state=CommerceState.Q19)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q18.set()
        await message.answer("Укажите общую площадь (м2)", reply_markup=kb_back)
    else:
        effective_area = message.text

        await state.update_data(var_effective_area=effective_area)
        await message.answer("Укажите общую площадь земли (м2)", reply_markup=kb_back)
        await CommerceState.next()


# Состояние CommerceState.Q20  -->  Укажите общую площадь земли (м2)
@dp.message_handler(state=CommerceState.Q20)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q19.set()
        await message.answer("Укажите полезную площадь (м2)", reply_markup=kb_back)
    else:
        land_area = message.text

        await state.update_data(var_land_area=land_area)
        await message.answer("Опишите территорию", reply_markup=kb_back)
        await CommerceState.next()


# Состояние CommerceState.Q21  -->  Опишите территорию
@dp.message_handler(state=CommerceState.Q21)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q20.set()
        await message.answer("Укажите общую площадь земли (м2)", reply_markup=kb_back)
    else:
        desc_territory = message.text

        await state.update_data(var_desc_territory=desc_territory)
        await message.answer("Выберите количество строений", reply_markup=kb_number_of_buildings)
        await CommerceState.next()


# Состояние CommerceState.Q22  -->  Выберите количество строений
@dp.message_handler(state=CommerceState.Q22)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q21.set()
        await message.answer("Опишите территорию", reply_markup=kb_back)
    else:
        number_of_buildings = message.text

        await state.update_data(var_desc_territory=number_of_buildings)
        await message.answer("Имеется ли дополнительная территория ?", reply_markup=kb_yes_or_no)
        await CommerceState.next()


# Состояние CommerceState.Q23  -->  Имеется ли дополнительная территория ?
@dp.message_handler(state=CommerceState.Q23)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q22.set()
        await message.answer("Выберите количество строений", reply_markup=kb_number_of_buildings)
    else:
        add_territory = message.text

        await state.update_data(var_add_territory=add_territory)
        await message.answer("Выберите расположение", reply_markup=kb_side_building)
        await CommerceState.next()


# Состояние CommerceState.Q24  -->  Выберите расположение
@dp.message_handler(state=CommerceState.Q24)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q23.set()
        await message.answer("Имеется ли дополнительная территория ?", reply_markup=kb_yes_or_no)
    else:
        side_building = message.text

        await state.update_data(var_side_building=side_building)
        await message.answer("Выберите вариант парковки", reply_markup=kb_type_parking)
        await CommerceState.next()


# Состояние CommerceState.Q25  -->  Выберите вариант парковки
@dp.message_handler(state=CommerceState.Q25)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q24.set()
        await message.answer("Выберите расположение", reply_markup=kb_side_building)
    else:
        type_parking = message.text

        await state.update_data(var_type_parking=type_parking)
        await message.answer("Выберите уровень безопасности", reply_markup=kb_security)
        await CommerceState.next()


# Состояние CommerceState.Q26  -->  Выберите уровень безопасности
@dp.message_handler(state=CommerceState.Q26)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q25.set()
        await message.answer("Выберите вариант парковки", reply_markup=kb_type_parking)
    else:
        security = message.text

        await state.update_data(var_security=security)
        await message.answer("Выберите состояние ремонта", reply_markup=kb_repair)
        await CommerceState.next()


# Состояние CommerceState.Q27  -->  Выберите состояние ремонта
@dp.message_handler(state=CommerceState.Q27)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q26.set()
        await message.answer("Выберите уровень безопасности", reply_markup=kb_security)
    else:
        type_repair = message.text

        await state.update_data(var_type_repair=type_repair)
        await message.answer("Выберите тип строения", reply_markup=kb_type_of_building)
        await CommerceState.next()


# Состояние CommerceState.Q28  -->  Выберите тип строения
@dp.message_handler(state=CommerceState.Q28)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q27.set()
        await message.answer("Выберите состояние ремонта", reply_markup=kb_repair)
    else:
        type_of_building = message.text

        await state.update_data(var_type_of_building=type_of_building)
        await message.answer("Завершено ли строительство дома?", reply_markup=kb_completed_building)
        await CommerceState.next()


# Состояние CommerceState.Q29  -->  Завершено ли строительство дома?
@dp.message_handler(state=CommerceState.Q29)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q28.set()
        await message.answer("Выберите тип строения", reply_markup=kb_type_of_building)
    else:
        completed_building = message.text

        await state.update_data(var_completed_building=completed_building)
        await message.answer("Переведён ли в нежилое ?", reply_markup=kb_non_residential)
        await CommerceState.next()


# Состояние CommerceState.Q30  -->  Переведён ли в нежилое ?
@dp.message_handler(state=CommerceState.Q30)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q29.set()
        await message.answer("Завершено ли строительство дома?", reply_markup=kb_completed_building)
    else:
        non_residential = message.text

        await state.update_data(var_non_residential=non_residential)
        await message.answer("Здание", reply_markup=kb_freestanding)
        await CommerceState.next()


# Состояние CommerceState.Q31  -->  Здание
@dp.message_handler(state=CommerceState.Q31)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q30.set()
        await message.answer("Переведён ли в нежилое ?", reply_markup=kb_non_residential)
    else:
        freestanding = message.text

        await state.update_data(var_freestanding=freestanding)
        await message.answer("Сейчас вам надо будет выбрать под какие назначения подходит коммерческое помещение.")
        await message.answer("Выберите назначение", reply_markup=kb_appointment)
        await CommerceState.next()


# Состояние CommerceState.Q32  -->  Выберите назначение
@dp.message_handler(state=CommerceState.Q32)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q31.set()
        await message.answer("Здание", reply_markup=kb_freestanding)
    else:
        appointments = list()
        appointments.append(message.text)
        await message.answer(f"Назначения: {appointments}")

        await state.update_data(var_appointment=appointments)
        await message.answer("Выберите еще назначение или нажмите на кнопку 'Готово ✅'", reply_markup=kb_appointment)
        await CommerceState.next()


# Состояние CommerceState.Q33  -->  Выберите назначение --> Готово ✅
@dp.message_handler(text="Готово ✅", state=CommerceState.Q33)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q31.set()
        await message.answer("Здание", reply_markup=kb_freestanding)
    else:
        answer = await state.get_data()
        appointments = answer['var_appointment']
        separator = ','
        appointments = separator.join(appointments)

        await state.update_data(var_appointment=appointments)
        await message.answer(f"Выбранные вами назначения {appointments}")
        await message.answer("/--/--/--/--/--/--/------/--/--/--/--/--/--/--/")
        await message.answer("Имеются ли арендаторы?", reply_markup=kb_tenants)
        await CommerceState.next()


# Состояние CommerceState.Q33  -->  Выберите назначение --> Повтор
@dp.message_handler(state=CommerceState.Q33)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q31.set()
        await message.answer("Здание", reply_markup=kb_freestanding)
    else:
        answer = await state.get_data()
        appointments = answer['var_appointment']
        appointments.append(message.text)
        await message.answer(f"{appointments}")

        await state.update_data(var_appointment=appointments)
        await message.answer(f"Назначение '{message.text}' добавлено", reply_markup=kb_appointment)


# Состояние CommerceState.Q34  -->  Имеются ли арендаторы?
@dp.message_handler(state=CommerceState.Q34)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q32.set()
        await message.answer("Выберите назначение", reply_markup=kb_appointment)
    else:
        tenants = message.text

        await state.update_data(var_tenants=tenants)
        await message.answer("Эксклюзив ?", reply_markup=kb_yes_or_no)
        await CommerceState.next()


# Состояние CommerceState.Q35  -->  Эксклюзив ?
@dp.message_handler(state=CommerceState.Q35)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q34.set()
        await message.answer("Имеются ли арендаторы?", reply_markup=kb_tenants)
    else:
        exclusive = message.text

        await state.update_data(var_exclusive=exclusive)
        await message.answer("Выберите систему электроснабжения", reply_markup=kb_power_supply)
        await CommerceState.next()


# Состояние CommerceState.Q36  -->  Выберите систему электроснабжения
@dp.message_handler(state=CommerceState.Q36)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q35.set()
        await message.answer("Эксклюзив ?", reply_markup=kb_yes_or_no)
    else:
        power_supply = message.text

        await state.update_data(var_power_supply=power_supply)
        await message.answer("Выберите холодную воду и канализацию", reply_markup=kb_sewerage)
        await CommerceState.next()


# Состояние CommerceState.Q37  -->  Выберите холодную воду и канализацию
@dp.message_handler(state=CommerceState.Q37)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q36.set()
        await message.answer("Выберите систему электроснабжения", reply_markup=kb_power_supply)
    else:
        sewerage = message.text

        await state.update_data(var_sewerage=sewerage)
        await message.answer("Выберите систему газового снабжения", reply_markup=kb_system_gas)
        await CommerceState.next()


# Состояние CommerceState.Q38  -->  Выберите систему газового снабжения
@dp.message_handler(state=CommerceState.Q38)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q37.set()
        await message.answer("Выберите холодную воду и канализацию", reply_markup=kb_sewerage)
    else:
        system_gas = message.text

        await state.update_data(var_system_gas=system_gas)
        await message.answer("Выберите систему отопления и ГВС", reply_markup=kb_system_heating)
        await CommerceState.next()


# Состояние CommerceState.Q39  -->  Выберите систему отопления и ГВС
@dp.message_handler(state=CommerceState.Q39)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q38.set()
        await message.answer("Выберите систему газового снабжения", reply_markup=kb_system_gas)
    else:
        system_heating = message.text

        await state.update_data(var_system_heating=system_heating)
        await message.answer(f"Укажите стартовую цену ( $ )", reply_markup=kb_back)
        await CommerceState.next()


# Состояние CommerceState.Q40  -->  Укажите стартовую цену ( $ )
@dp.message_handler(state=CommerceState.Q40)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q39.set()
        await message.answer("Выберите систему отопления и ГВС", reply_markup=kb_system_heating)
    else:
        price = message.text

        await state.update_data(var_price=price)
        await message.answer(f"Стартовая\nС процентами\nЦена на руки", reply_markup=kb_back)
        await CommerceState.next()


# Состояние CommerceState.Q41  -->  Стартовая С процентами Цена на руки
@dp.message_handler(state=CommerceState.Q41)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q40.set()
        await message.answer(f"Укажите стартовую цену ( $ )", reply_markup=kb_back)
    else:
        full_price = message.text

        await state.update_data(var_full_price=full_price)
        await message.answer(f"Укажите имя собственника", reply_markup=kb_back)
        await CommerceState.next()


# Состояние CommerceState.Q42  -->  Укажите имя собственника
@dp.message_handler(state=CommerceState.Q42)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q41.set()
        await message.answer(f"Стартовая\nС процентами\nЦена на руки", reply_markup=kb_back)
    else:
        owner = message.text

        await state.update_data(var_owner=owner)
        await message.answer(f"Введите контактный номер телефона собственника. \nПример ввода  987777777",
                             reply_markup=kb_back)
        await CommerceState.next()


# Состояние CommerceState.Q43  -->  Введите контактный номер телефона собственника. Пример ввода  987777777
@dp.message_handler(state=CommerceState.Q43)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q42.set()
        await message.answer(f"Укажите имя собственника", reply_markup=kb_back)
    else:
        number_phone = message.text

        await state.update_data(var_number_phone=number_phone)
        await message.answer(f"Если имеется дополнительный номер телефона, введите его",
                             reply_markup=kb_back)
        await CommerceState.next()


# Состояние CommerceState.Q44  -->  Если имеется дополнительный номер телефона, введите его
@dp.message_handler(state=CommerceState.Q44)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q43.set()
        await message.answer(f"Введите контактный номер телефона собственника. \nПример ввода  987777777",
                             reply_markup=kb_back)
    else:
        additional_number_phone = message.text

        await state.update_data(var_additional_number_phone=additional_number_phone)
        await message.answer(f"Имеется ли информатор ?", reply_markup=kb_yes_or_no)
        await CommerceState.next()


# Состояние CommerceState.Q45  -->  Имеется ли информатор ?
@dp.message_handler(state=CommerceState.Q45)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q44.set()
        await message.answer(f"Если имеется дополнительный номер телефона, введите его",
                             reply_markup=kb_back)
    else:
        informant = message.text

        await state.update_data(var_informant=informant)
        await message.answer(f"Бизнес", reply_markup=kb_business)
        await CommerceState.next()


# Состояние CommerceState.Q46  -->  Бизнес
@dp.message_handler(state=CommerceState.Q46)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q45.set()
        await message.answer(f"Имеется ли информатор ?", reply_markup=kb_yes_or_no)
    else:
        business = message.text

        await state.update_data(var_business=business)
        await message.answer(f"Напишите полное описание квартиры", reply_markup=kb_back)
        await CommerceState.next()


# Состояние CommerceState.Q47  -->  Напишите полное описание квартиры
@dp.message_handler(state=CommerceState.Q47)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q46.set()
        await message.answer(f"Бизнес", reply_markup=kb_business)
    else:
        description = message.text

        await state.update_data(var_description=description)
        await message.answer(f"Рекламировать на торговых площадках ?", reply_markup=kb_yes_or_no)
        await CommerceState.next()


# Состояние ApartmentState.Q48  -->  Рекламировать на торговых площадках ?
@dp.message_handler(state=CommerceState.Q48)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await CommerceState.Q47.set()
        await message.answer(f"Напишите полное описание квартиры", reply_markup=kb_back)
    else:
        public = message.text

        await state.update_data(var_public=public)
        await message.answer(f"Все заполнил(-а) правильно ?", reply_markup=kb_yes_or_no)
        await CommerceState.next()


# Состояние ApartmentState.Q49  -->  Все заполнил(-а) правильно ?
@dp.message_handler(state=CommerceState.Q49)
async def select_district(message: types.Message, state=FSMContext):
    filled_in_correctly = message.text
    answer = await state.get_data()
    user_name = message.from_user.full_name

    if filled_in_correctly.lower() == 'да':
        dt_time = str(date.today())
        answer = await state.get_data()
        list_answer = []
        list_answer.append(answer['var_type_of_property'])  # A --> ID
        list_answer.append(answer['var_district'])  # B --> Район
        list_answer.append(answer['var_reference_point'])  # C --> Ориентир
        list_answer.append(answer['var_street'])  # D --> Улица
        list_answer.append(answer['var_counter_room'])  # E --> Кол-во комнат
        list_answer.append(answer['var_floor'])  # F --> Этаж
        list_answer.append(answer['var_number_floor'])  # G --> Этажность
        list_answer.append(answer['var_commerce_area'])  # H --> S общ
        list_answer.append(answer['var_effective_area'])  # I --> S полезная
        list_answer.append(answer['var_type_repair'])  # J --> Ремонт
        list_answer.append(answer['var_type_of_building'])  # K --> Тип строения
        list_answer.append(answer['var_type_of_service'])  # L --> Тип недвижимости
        list_answer.append(answer['var_appointment'])  # M --> Назначение
        list_answer.append(answer['var_number_of_buildings'])  # N --> Кол-во строений
        list_answer.append(answer['var_land_area'])  # O --> Площадь земли
        list_answer.append(answer['var_non_residential'])  # P --> Переведено в нежилое
        list_answer.append(answer['var_ceiling_height'])  # Q --> Высота потолков
        list_answer.append(answer['var_description'])  # R --> Описание
        list_answer.append(answer['var_traffic_level'])  # S --> Проходимость
        list_answer.append(answer['var_add_territory'])  # T --> Доп.территория
        list_answer.append(answer['var_desc_territory'])  # U --> Описание территории
        list_answer.append(answer['var_completed_building'])  # V --> Завершено строительство
        list_answer.append(answer['var_type_parking'])  # W --> Парковка
        list_answer.append(answer['var_price'])  # X --> Стартовая цена
        list_answer.append(answer['var_full_price'])  # Y --> Цена
        list_answer.append(answer['var_owner'])  # Z --> Имя собственника
        list_answer.append(answer['var_number_phone'])  # AA --> Номер телефона
        list_answer.append(answer['var_additional_number_phone'])  # AB --> Доп.номер
        list_answer.append('')  # AC --> Зарубежный номер
        list_answer.append(answer['var_location_the_road'])  # AD --> Расположение от дороги61
        list_answer.append(answer['var_side_building'])  # AE --> Расположение в здании
        list_answer.append(answer['var_number_home'])  # AF --> Номер дома
        list_answer.append(answer['var_number_apartment'])  # AG --> Номер квартиры
        list_answer.append(answer['var_business'])  # AH --> Бизнес
        list_answer.append(answer['var_freestanding'])  # AI --> Здание
        list_answer.append(answer['var_tenants'])  # AG --> Арендаторы
        list_answer.append('')  # AK --> Заголовок
        list_answer.append('')  # AL --> Описание
        list_answer.append('')  # AM --> Заголовок UZB
        list_answer.append('')  # AN --> Описание UZB
        list_answer.append(user_name)  # AO --> Имя агента
        list_answer.append(dt_time)  # AP --> Дата создания
        list_answer.append(dt_time)  # AQ --> Дата обзвона
        list_answer.append(answer['var_informant'])  # AR --> Информатор
        list_answer.append(answer['var_infrastructures'])  # AS --> Инфраструктура
        list_answer.append(answer['var_distance_to_metro'])  # AT --> Метро
        list_answer.append(answer['var_system_heating'])  # AU --> Отопление
        list_answer.append(answer['var_sewerage'])  # AV --> ХВС
        list_answer.append(answer['var_power_supply'])  # AW --> Электрика
        list_answer.append(answer['var_system_gas'])  # AX --> Газ
        list_answer.append(answer['var_furniture'])  # AY --> Мебель
        list_answer.append(answer['var_technics'])  # AZ --> Техника
        list_answer.append(answer['var_add_technics'])  # BA --> Доп.оборудование
        list_answer.append(answer['var_security'])  # BB --> Безопасность
        list_answer.append(answer['var_exclusive'])  # BC --> Эксклюзив
        list_answer.append(answer['var_public'])  # BD --> Рекламировать
        await state.reset_state()
        await message.answer('Ваша объективка отправлена)', reply_markup=kb_main_menu)
        google_sendler('1-B80joNKTOSTIJRLiACOcfH1E3dH5yrNPbS-CU5Bvxc', 'Продажа коммерции!A', 'BD', list_answer)
    elif filled_in_correctly.lower() == 'нет':
        await state.reset_state()
        await message.answer('Вы отменили отправку', reply_markup=kb_main_menu)
    else:
        await message.answer('Отправлено не верное значение( Попробуйте снова')
