import os

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import kb_district, kb_location_the_road, kb_type_of_building, kb_type_of_layout, \
    kb_apartment_layout, kb_redevelopment, kb_side_building, kb_elevator_condition, kb_roof_condition, kb_type_parking, \
    kb_distance_to_metro, kb_yes_or_no, kb_registration_date, kb_furniture, kb_balcony_size, kb_repair, kb_toilet, \
    kb_technics, kb_air_conditioning
from keyboards.default import kb_main_menu
from loader import dp
from states import MenuState, ApartmentState
from datetime import date

from pprint import pprint

import googleapiclient.discovery
import httplib2
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()


def google_sendler(sheet_id, start_col, end_col, array_data):

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        os.getenv('credentails_file'),
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
@dp.message_handler(state=MenuState.Q3)
async def select_district(message: types.Message, state=FSMContext):
    # Получаем текст сообщения, а после записываем значение в переменную district
    type_of_service = message.text

    # Записываем полученное значение в словарь машины состояний под ключом var_type_of_service
    await state.update_data(var_type_of_service=type_of_service)
    # Отправляем сообщение и массив кнопок
    await message.answer("Выберите район", reply_markup=kb_district)
    # Переходим в машину состояний ApartmentState
    await ApartmentState.first()


# Состояние ApartmentState.Q1  -->  Выберите район
@dp.message_handler(state=ApartmentState.Q1)
async def select_district(message: types.Message, state=FSMContext):
    district = message.text

    await state.update_data(var_district=district)
    await message.answer("Укажите квартал", reply_markup=ReplyKeyboardRemove())
    await ApartmentState.next()


# Состояние ApartmentState.Q2  -->  Укажите квартал
@dp.message_handler(state=ApartmentState.Q2)
async def select_district(message: types.Message, state=FSMContext):
    quarter = message.text

    await state.update_data(var_quarter=quarter)
    await message.answer("Укажите улицу на которой находится дом")
    await ApartmentState.next()


# Состояние ApartmentState.Q3  -->  Укажите улицу на которой находится дом
@dp.message_handler(state=ApartmentState.Q3)
async def select_district(message: types.Message, state=FSMContext):
    street = message.text

    await state.update_data(var_street=street)
    await message.answer("Укажите ориентир")
    await ApartmentState.next()


# Состояние ApartmentState.Q4  -->  Укажите ориентир
@dp.message_handler(state=ApartmentState.Q4)
async def select_district(message: types.Message, state=FSMContext):
    reference_point = message.text

    await state.update_data(var_reference_point=reference_point)
    await message.answer("Укажите инфраструктуру (дет.сад, магазин, больницы, транспортная развязка и т.д.)")
    await ApartmentState.next()


# Состояние ApartmentState.Q5  -->  Укажите инфраструктуру
@dp.message_handler(state=ApartmentState.Q5)
async def select_district(message: types.Message, state=FSMContext):
    infrastructure = message.text

    await state.update_data(var_infrastructure=infrastructure)
    await message.answer("Выберите расположение от дороги", reply_markup=kb_location_the_road)
    await ApartmentState.next()


# Состояние ApartmentState.Q6  -->  Выберите расположение от дороги
@dp.message_handler(state=ApartmentState.Q6)
async def select_district(message: types.Message, state=FSMContext):
    location_the_road = message.text

    await state.update_data(var_location_the_road=location_the_road)
    await message.answer(f"Укажите номер дома")
    await ApartmentState.next()


# Состояние ApartmentState.Q7  -->  Укажите номер дома
@dp.message_handler(state=ApartmentState.Q7)
async def select_district(message: types.Message, state=FSMContext):
    number_home = message.text

    await state.update_data(var_number_home=number_home)
    await message.answer(f"Укажите номер квартиры")
    await ApartmentState.next()


# Состояние ApartmentState.Q8  -->  Укажите номер квартиры
@dp.message_handler(state=ApartmentState.Q8)
async def select_district(message: types.Message, state=FSMContext):
    number_apartment = message.text

    await state.update_data(var_number_apartment=number_apartment)
    await message.answer(f"Выберите тип строения", reply_markup=kb_type_of_building)
    await ApartmentState.next()


# Состояние ApartmentState.Q9  -->  Выберите тип строения
@dp.message_handler(state=ApartmentState.Q9)
async def select_district(message: types.Message, state=FSMContext):
    type_building = message.text

    await state.update_data(var_type_building=type_building)
    await message.answer(f"Выберите тип планировки", reply_markup=kb_type_of_layout)
    await ApartmentState.next()


# Состояние ApartmentState.Q10  -->  Выберите тип планировки
@dp.message_handler(state=ApartmentState.Q10)
async def select_district(message: types.Message, state=FSMContext):
    type_layout = message.text

    await state.update_data(var_type_layout=type_layout)
    await message.answer(f"Выберите вид планировки", reply_markup=kb_apartment_layout)
    await ApartmentState.next()


# Состояние ApartmentState.Q11  -->  Выберите вид планировки
@dp.message_handler(state=ApartmentState.Q11)
async def select_district(message: types.Message, state=FSMContext):
    apartment_layout = message.text

    await state.update_data(var_apartment_layout=apartment_layout)
    await message.answer(f"Имеется ли перепланировка ?", reply_markup=kb_redevelopment)
    await ApartmentState.next()


# Состояние ApartmentState.Q12  -->  Имеется ли перепланировка ?
@dp.message_handler(state=ApartmentState.Q12)
async def select_district(message: types.Message, state=FSMContext):
    redevelopment = message.text

    await state.update_data(var_redevelopment=redevelopment)
    await message.answer(f"Выберите расположение квартиры в доме", reply_markup=kb_side_building)
    await ApartmentState.next()


# Состояние ApartmentState.Q13  -->  Выберите расположение квартиры в доме
@dp.message_handler(state=ApartmentState.Q13)
async def select_district(message: types.Message, state=FSMContext):
    side_building = message.text

    await state.update_data(var_side_building=side_building)
    await message.answer(f"Выберите состояние лифта", reply_markup=kb_elevator_condition)
    await ApartmentState.next()


# Состояние ApartmentState.Q14  -->  Выберите состояние лифта
@dp.message_handler(state=ApartmentState.Q14)
async def select_district(message: types.Message, state=FSMContext):
    elevator_condition = message.text

    await state.update_data(var_elevator_condition=elevator_condition)
    await message.answer(f"Выберите состояние крыши", reply_markup=kb_roof_condition)
    await ApartmentState.next()


# Состояние ApartmentState.Q15  -->  Выберите состояние крыши
@dp.message_handler(state=ApartmentState.Q15)
async def select_district(message: types.Message, state=FSMContext):
    roof_condition = message.text

    await state.update_data(var_roof_condition=roof_condition)
    await message.answer(f"Выберите вариант парковки", reply_markup=kb_type_parking)
    await ApartmentState.next()


# Состояние ApartmentState.Q16  -->  Выберите вариант парковки
@dp.message_handler(state=ApartmentState.Q16)
async def select_district(message: types.Message, state=FSMContext):
    type_parking = message.text

    await state.update_data(var_type_parking=type_parking)
    await message.answer(f"Выберите расстояние до метро", reply_markup=kb_distance_to_metro)
    await ApartmentState.next()


# Состояние ApartmentState.Q17  -->  Выберите расстояние до метро
@dp.message_handler(state=ApartmentState.Q17)
async def select_district(message: types.Message, state=FSMContext):
    distance_to_metro = message.text

    await state.update_data(var_distance_to_metro=distance_to_metro)
    await message.answer(f"Укажите количество комнат")
    await ApartmentState.next()


# Состояние ApartmentState.Q18  -->  Укажите количество комнат
@dp.message_handler(state=ApartmentState.Q18)
async def select_district(message: types.Message, state=FSMContext):
    counter_room = message.text

    await state.update_data(var_counter_room=counter_room)
    await message.answer(f"Укажите этаж")
    await ApartmentState.next()


# Состояние ApartmentState.Q19  -->  Укажите этаж
@dp.message_handler(state=ApartmentState.Q19)
async def select_district(message: types.Message, state=FSMContext):
    floor = message.text

    await state.update_data(var_floor=floor)
    await message.answer(f"Укажите этажность")
    await ApartmentState.next()


# Состояние ApartmentState.Q20  -->  Укажите этажность
@dp.message_handler(state=ApartmentState.Q20)
async def select_district(message: types.Message, state=FSMContext):
    number_floor = message.text

    await state.update_data(var_number_floor=number_floor)
    await message.answer(f"Выберите тип сан. узла", reply_markup=kb_toilet)
    await ApartmentState.next()


# Состояние ApartmentState.Q21  -->  Выберите тип сан. узла
@dp.message_handler(state=ApartmentState.Q21)
async def select_district(message: types.Message, state=FSMContext):
    type_dress = message.text

    await state.update_data(var_type_dress=type_dress)
    await message.answer(f"Укажите высоту потолков")
    await ApartmentState.next()


# Состояние ApartmentState.Q22  -->  Укажите высоту потолков
@dp.message_handler(state=ApartmentState.Q22)
async def select_district(message: types.Message, state=FSMContext):
    ceiling_height = message.text

    await state.update_data(var_ceiling_height=ceiling_height)
    await message.answer(f"Выберите состояние ремонта", reply_markup=kb_repair)
    await ApartmentState.next()


# Состояние ApartmentState.Q23  -->  Выберите состояние ремонта
@dp.message_handler(state=ApartmentState.Q23)
async def select_district(message: types.Message, state=FSMContext):
    repair = message.text

    await state.update_data(var_repair=repair)
    await message.answer(f"Укажите общую площадь квартиры (м2)")
    await ApartmentState.next()


# Состояние ApartmentState.Q24  -->  Укажите общую площадь квартиры (м2)
@dp.message_handler(state=ApartmentState.Q24)
async def select_district(message: types.Message, state=FSMContext):
    apartment_area = message.text

    await state.update_data(var_apartment_area=apartment_area)
    await message.answer(f"Укажите площадь кухни (м2)")
    await ApartmentState.next()


# Состояние ApartmentState.Q25  -->  Укажите площадь кухни (м2)
@dp.message_handler(state=ApartmentState.Q25)
async def select_district(message: types.Message, state=FSMContext):
    kitchen_area = message.text

    await state.update_data(var_kitchen_area=kitchen_area)
    await message.answer(f"Выберите габариты балкона", reply_markup=kb_balcony_size)
    await ApartmentState.next()


# Состояние ApartmentState.Q26  -->  Выберите габариты балкона
@dp.message_handler(state=ApartmentState.Q26)
async def select_district(message: types.Message, state=FSMContext):
    balcony_size = message.text

    await state.update_data(var_balcony_size=balcony_size)
    await message.answer(f"Выберите вариант мебелировки", reply_markup=kb_furniture)
    await ApartmentState.next()


# Состояние ApartmentState.Q27  -->  Выберите вариант мебелировки
@dp.message_handler(state=ApartmentState.Q27)
async def select_district(message: types.Message, state=FSMContext):
    furniture = message.text

    await state.update_data(var_furniture=furniture)
    await message.answer(f"Имеются ли техника ?", reply_markup=kb_technics)
    await ApartmentState.next()


# Состояние ApartmentState.Q28  -->  Имеются ли техника ?
@dp.message_handler(state=ApartmentState.Q28)
async def select_district(message: types.Message, state=FSMContext):
    technics = message.text

    await state.update_data(var_technics=technics)
    await message.answer(f"Имеется ли в наличии пластиковые окна?", reply_markup=kb_yes_or_no)
    await ApartmentState.next()


# Состояние ApartmentState.Q29  -->  Имеются ли пластиковые окна ?
@dp.message_handler(state=ApartmentState.Q29)
async def select_district(message: types.Message, state=FSMContext):
    plastic_windows = message.text

    await state.update_data(var_plastic_windows=plastic_windows)
    await message.answer(f"Имеется ли в наличии кондиционер ?", reply_markup=kb_air_conditioning)
    await ApartmentState.next()


# Состояние ApartmentState.Q30  -->  Имеется ли в наличии кондиционер ?
@dp.message_handler(state=ApartmentState.Q30)
async def select_district(message: types.Message, state=FSMContext):
    condition = message.text

    await state.update_data(var_condition=condition)
    await message.answer(f"Укажите имя собственника")
    await ApartmentState.next()


# Состояние ApartmentState.Q31  -->  Укажите имя собственника
@dp.message_handler(state=ApartmentState.Q31)
async def select_district(message: types.Message, state=FSMContext):
    owner = message.text

    await state.update_data(var_owner=owner)
    await message.answer(f"Введите контактный номер телефона собственника. \nПример ввода  987777777")
    await ApartmentState.next()


# Состояние ApartmentState.Q32  -->  Введите контактный номер телефона собственника. Пример ввода  987777777
@dp.message_handler(state=ApartmentState.Q32)
async def select_district(message: types.Message, state=FSMContext):
    number_phone = message.text

    await state.update_data(var_number_phone=number_phone)
    await message.answer(f"Если имеется дополнительный номер телефона, введите его")
    await ApartmentState.next()


# Состояние ApartmentState.Q33  -->  Если имеется дополнительный номер телефона, введите его
@dp.message_handler(state=ApartmentState.Q33)
async def select_district(message: types.Message, state=FSMContext):
    additional_number_phone = message.text

    await state.update_data(var_additional_number_phone=additional_number_phone)
    await message.answer(f"Имеется ли информатор ?", reply_markup=kb_yes_or_no)
    await ApartmentState.next()


# Состояние ApartmentState.Q34  -->  Имеется ли информатор ?
@dp.message_handler(state=ApartmentState.Q34)
async def select_district(message: types.Message, state=FSMContext):
    informant = message.text

    await state.update_data(var_informant=informant)
    await message.answer(f"Укажите стартовую цену ( $ )")
    await ApartmentState.next()


# Состояние ApartmentState.Q35  -->  Укажите стартовую цену ( $ )
@dp.message_handler(state=ApartmentState.Q35)
async def select_district(message: types.Message, state=FSMContext):
    price = message.text

    await state.update_data(var_price=price)
    await message.answer(f"Стартовая\nС процентами\nЦена на руки")
    await ApartmentState.next()


# Состояние ApartmentState.Q36  -->  Стартовая С процентами Цена на руки
@dp.message_handler(state=ApartmentState.Q36)
async def select_district(message: types.Message, state=FSMContext):
    full_price = message.text

    await state.update_data(var_full_price=full_price)
    await message.answer(f"Укажите количество прописанных человек")
    await ApartmentState.next()


# Состояние ApartmentState.Q37  -->  Укажите количество прописанных человек
@dp.message_handler(state=ApartmentState.Q37)
async def select_district(message: types.Message, state=FSMContext):
    scribed_people = message.text

    await state.update_data(var_scribed_people=scribed_people)
    await message.answer(f"Выберите время которое прошло с последнего оформления", reply_markup=kb_registration_date)
    await ApartmentState.next()


# Состояние ApartmentState.Q38  -->  Выберите время которое прошло с последнего оформления
@dp.message_handler(state=ApartmentState.Q38)
async def select_district(message: types.Message, state=FSMContext):
    checkout_time = message.text

    await state.update_data(var_checkout_time=checkout_time)
    await message.answer(f"Подойдет ли под офис ?", reply_markup=kb_yes_or_no)
    await ApartmentState.next()


# Состояние ApartmentState.Q39  -->  "Подойдет ли под офис ?
@dp.message_handler(state=ApartmentState.Q39)
async def select_district(message: types.Message, state=FSMContext):
    under_to_office = message.text

    await state.update_data(var_under_to_office=under_to_office)
    await message.answer(f"Эксклюзив ?", reply_markup=kb_yes_or_no)
    await ApartmentState.next()


# Состояние ApartmentState.Q40  -->  Эксклюзив ?
@dp.message_handler(state=ApartmentState.Q40)
async def select_district(message: types.Message, state=FSMContext):
    exclusive = message.text

    await state.update_data(var_exclusive=exclusive)
    await message.answer(f"Напишите полное описание квартиры")
    await ApartmentState.next()


# Состояние ApartmentState.Q41  -->  Напишите полное описание квартиры
@dp.message_handler(state=ApartmentState.Q41)
async def select_district(message: types.Message, state=FSMContext):
    description = message.text

    await state.update_data(var_description=description)
    await message.answer(f"Рекламировать на торговых площадках ?", reply_markup=kb_yes_or_no)
    await ApartmentState.next()


# Состояние ApartmentState.Q42  -->  Рекламировать на торговых площадках ?
@dp.message_handler(state=ApartmentState.Q42)
async def select_district(message: types.Message, state=FSMContext):
    public = message.text

    await state.update_data(var_public=public)
    await message.answer(f"Все заполнил(-а) правильно ?", reply_markup=kb_yes_or_no)
    await ApartmentState.next()


# Состояние ApartmentState.Q43  -->  Все заполнил(-а) правильно ?
@dp.message_handler(state=ApartmentState.Q43)
async def select_district(message: types.Message, state=FSMContext):
    filled_in_correctly = message.text
    answer = await state.get_data()
    user_name = message.from_user.first_name

    if filled_in_correctly.lower() == 'да':
        dt_time = str(date.today())
        answer = await state.get_data()
        list_answer = []
        list_answer.append(answer['var_type_of_property'])
        list_answer.append(answer['var_quarter'])
        list_answer.append(answer['var_reference_point'])
        list_answer.append(answer['var_street'])
        list_answer.append(answer['var_counter_room'])
        list_answer.append(answer['var_floor'])
        list_answer.append(answer['var_number_floor'])
        list_answer.append(answer['var_apartment_area'])
        list_answer.append(answer['var_balcony_size'])
        list_answer.append(answer['var_type_dress'])
        list_answer.append(answer['var_repair'])
        list_answer.append(answer['var_type_building'])
        list_answer.append(answer['var_apartment_layout'])
        list_answer.append(answer['var_type_layout'])
        list_answer.append(answer['var_side_building'])
        list_answer.append(answer['var_ceiling_height'])
        list_answer.append(answer['var_furniture'])
        list_answer.append(answer['var_technics'])
        list_answer.append(answer['var_condition'])
        list_answer.append(answer['var_kitchen_area'])
        list_answer.append(answer['var_plastic_windows'])
        list_answer.append(answer['var_price'])
        list_answer.append(answer['var_full_price'])
        list_answer.append(answer['var_owner'])
        list_answer.append(answer['var_number_phone'])
        list_answer.append(answer['var_additional_number_phone'])
        list_answer.append(' ')
        list_answer.append(answer['var_location_the_road'])
        list_answer.append(answer['var_distance_to_metro'])
        list_answer.append(answer['var_number_apartment'])
        list_answer.append(answer['var_number_home'])
        list_answer.append(' ')
        list_answer.append(' ')
        list_answer.append(user_name)
        list_answer.append(dt_time)
        list_answer.append(dt_time)
        list_answer.append(answer['var_informant'])
        list_answer.append(' ')
        list_answer.append(answer['var_district'])
        list_answer.append(answer['var_infrastructure'])
        list_answer.append(answer['var_redevelopment'])
        list_answer.append(answer['var_type_parking'])
        list_answer.append(answer['var_description'])
        list_answer.append(answer['var_elevator_condition'])
        list_answer.append(answer['var_roof_condition'])
        list_answer.append(answer['var_checkout_time'])
        list_answer.append(answer['var_scribed_people'])
        list_answer.append(answer['var_under_to_office'])
        list_answer.append(answer['var_exclusive'])
        list_answer.append(answer['var_public'])
        google_sendler('1-B80joNKTOSTIJRLiACOcfH1E3dH5yrNPbS-CU5Bvxc', 'A', 'AX', list_answer)
        await message.answer('Ваша объективка отправлена)', reply_markup=kb_main_menu)
        await state.reset_state()
    elif filled_in_correctly.lower() == 'нет':
        await state.update_data(var_filled_in_correctly=filled_in_correctly)
    else:
        await message.answer('Отправлено не верное значение( Попробуйте снова')
