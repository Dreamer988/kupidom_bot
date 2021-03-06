from datetime import date

from aiogram import types
from aiogram.dispatcher import FSMContext

from google_work.google_work import GoogleWork
from keyboards.default.rent_commerce import kb_district, kb_location_the_road_back, kb_traffic_level_back, \
    kb_distance_to_metro_back, kb_infrastructure_back, kb_number_room_back, kb_number_floor_back, kb_toilet_back, \
    kb_furniture_back, kb_technics_back, kb_side_building_back, kb_type_parking_back, kb_security_back, \
    kb_repair_back, kb_type_of_building_back, kb_redevelopment_back, kb_freestanding_back, kb_appointment_back, \
    kb_power_supply_back, kb_prepayment_back, kb_yes_or_no, kb_sewerage_back, kb_system_gas_back, \
    kb_system_heating_back, kb_tenants_back, kb_main_menu, kb_yes_or_no_back
from keyboards.default.step_back import kb_back
from loader import dp
from states import ObjectState, RentCommerceState


# Отслеживаем сообщение по фильтру состояния MenuState.Rent
@dp.message_handler(text="Коммерция", state=ObjectState.Rent)
async def select_district(message: types.Message, state=FSMContext):
    # Получаем текст сообщения, а после записываем значение в переменную district
    type_of_service = message.text

    # Записываем полученное значение в словарь машины состояний под ключом var_type_of_service
    await state.update_data(var_type_of_service=type_of_service)
    # Отправляем сообщение и массив кнопок
    await message.answer("Выберите район", reply_markup=kb_district)
    # Переходим в машину состояний ApartmentState
    await RentCommerceState.first()


# Состояние RentCommerceState.Q1  -->  Выберите район
@dp.message_handler(state=RentCommerceState.Q1)
async def select_district(message: types.Message, state=FSMContext):
    district = message.text

    await state.update_data(var_district=district)
    await message.answer("Укажите ориентир", reply_markup=kb_back)
    await RentCommerceState.next()


# Состояние RentCommerceState.Q2  -->  Укажите ориентир
@dp.message_handler(state=RentCommerceState.Q2)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q1.set()
        await message.answer("Выберите район", reply_markup=kb_district)
    else:
        reference_point = message.text

        await state.update_data(var_reference_point=reference_point)
        await message.answer("Укажите улицу на которой находится объект", reply_markup=kb_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q3  -->  Укажите улицу на которой находится объект
@dp.message_handler(state=RentCommerceState.Q3)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q2.set()
        await message.answer("Укажите ориентир", reply_markup=kb_back)
    else:
        street = message.text

        await state.update_data(var_street=street)
        await message.answer("Укажите номер дома", reply_markup=kb_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q4  -->  Укажите номер дома
@dp.message_handler(state=RentCommerceState.Q4)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q3.set()
        await message.answer("Укажите улицу на которой находится объект", reply_markup=kb_back)
    else:
        number_home = message.text

        await state.update_data(var_number_home=number_home)
        await message.answer("Укажите номер квартиры", reply_markup=kb_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q5  -->  Укажите номер квартиры
@dp.message_handler(state=RentCommerceState.Q5)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q4.set()
        await message.answer("Укажите номер дома", reply_markup=kb_back)
    else:
        number_apartment = message.text

        await state.update_data(var_number_apartment=number_apartment)
        await message.answer("Выберите расположение от дороги", reply_markup=kb_location_the_road_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q6  -->  Выберите расположение от дороги
@dp.message_handler(state=RentCommerceState.Q6)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q5.set()
        await message.answer("Укажите номер квартиры", reply_markup=kb_back)
    else:
        location_the_road = message.text

        await state.update_data(var_location_the_road=location_the_road)
        await message.answer("Выберите уровень проходимости", reply_markup=kb_traffic_level_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q7  -->  Выберите уровень проходимости
@dp.message_handler(state=RentCommerceState.Q7)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q6.set()
        await message.answer("Выберите расположение от дороги", reply_markup=kb_location_the_road_back)
    else:
        traffic_level = message.text

        await state.update_data(var_traffic_level=traffic_level)
        await message.answer("Выберите расстояние до метро", reply_markup=kb_distance_to_metro_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q8  -->  Выберите расстояние до метро
@dp.message_handler(state=RentCommerceState.Q8)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q7.set()
        await message.answer("Выберите уровень проходимости", reply_markup=kb_traffic_level_back)
    else:
        distance_to_metro = message.text

        await state.update_data(var_distance_to_metro=distance_to_metro)
        await message.answer("Укажите инфраструктуру (дет.сад, магазин, больницы, транспортная развязка и т.д.)",
                             reply_markup=kb_infrastructure_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Infrastructure  -->  Укажите инфраструктуру
@dp.message_handler(text="Готово ✅", state=RentCommerceState.Infrastructure)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q8.set()
        await message.answer("Выберите расстояние до метро", reply_markup=kb_distance_to_metro_back)
    else:
        answer = await state.get_data()
        infrastructures = answer['var_infrastructures']
        separator = ','
        infrastructures = separator.join(infrastructures)

        await message.answer(f'Инфраструктура которую вы выбрали: {infrastructures}')
        await message.answer("/--/--/--/--/--/--/------/--/--/--/--/--/--/--/")
        await state.update_data(var_infrastructures=infrastructures)

        await message.answer("Укажите количество комнат", reply_markup=kb_number_room_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q9  -->  Укажите инфраструктуру (дет.сад, магазин, больницы, транспортная развязка и т.д.)
@dp.message_handler(state=RentCommerceState.Q9)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q8.set()
        await message.answer("Выберите расстояние до метро", reply_markup=kb_distance_to_metro_back)
    else:
        infrastructure = message.text
        infrastructures = list()
        infrastructures.append(infrastructure)
        await state.update_data(var_infrastructures=infrastructures)
        await message.answer("Выберите еще варианты или нажмите на кнопку 'Готово ✅",
                             reply_markup=kb_infrastructure_back)
        await RentCommerceState.Infrastructure.set()


# Состояние RentCommerceState.Infrastructure  -->  Повтор
@dp.message_handler(state=RentCommerceState.Infrastructure)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q8.set()
        await message.answer("Выберите расстояние до метро", reply_markup=kb_distance_to_metro_back)
    else:
        infrastructure = message.text
        answer = await state.get_data()
        infrastructures = answer['var_infrastructures']
        infrastructures.append(infrastructure)
        await state.update_data(var_infrastructures=infrastructures)
    await message.answer(f"{infrastructures}", reply_markup=kb_infrastructure_back)


# Состояние RentCommerceState.Q10  -->  Укажите количество комнат
@dp.message_handler(state=RentCommerceState.Q10)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q9.set()
        await message.answer("Укажите инфраструктуру (дет.сад, магазин, больницы, транспортная развязка и т.д.)",
                             reply_markup=kb_infrastructure_back)
    else:
        counter_room = message.text

        await state.update_data(var_counter_room=counter_room)
        await message.answer("Укажите этаж", reply_markup=kb_number_floor_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q11  -->  Укажите этаж
@dp.message_handler(state=RentCommerceState.Q11)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q10.set()
        await message.answer("Укажите количество комнат", reply_markup=kb_number_room_back)
    else:
        floor = message.text

        await state.update_data(var_floor=floor)
        await message.answer("Укажите этажность", reply_markup=kb_number_floor_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q12  -->  Укажите этажность
@dp.message_handler(state=RentCommerceState.Q12)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q11.set()
        await message.answer("Укажите этаж", reply_markup=kb_number_floor_back)
    else:
        number_floor = message.text

        await state.update_data(var_number_floor=number_floor)
        await message.answer("Выберите количество сан. узлов", reply_markup=kb_toilet_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q13  -->  Выберите количество сан. узлов
@dp.message_handler(state=RentCommerceState.Q13)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q12.set()
        await message.answer("Укажите этажность", reply_markup=kb_number_floor_back)
    else:
        counter_dress = message.text

        await state.update_data(var_counter_dress=counter_dress)
        await message.answer("Укажите высоту потолков", reply_markup=kb_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q14  -->  Укажите высоту потолков
@dp.message_handler(state=RentCommerceState.Q14)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q13.set()
        await message.answer("Выберите количество сан. узлов", reply_markup=kb_toilet_back)
    else:
        ceiling_height = message.text

        await state.update_data(var_ceiling_height=ceiling_height)
        await message.answer("Выберите вариант мебелировки", reply_markup=kb_furniture_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q15  -->  Выберите вариант мебелировки
@dp.message_handler(state=RentCommerceState.Q15)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q14.set()
        await message.answer("Укажите высоту потолков", reply_markup=kb_back)
    else:
        furniture = message.text

        await state.update_data(var_furniture=furniture)
        await message.answer("Имеется ли наличие техники или оборудования ?", reply_markup=kb_technics_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q16  -->  Имеется ли наличие техники или оборудования ?
@dp.message_handler(state=RentCommerceState.Q16)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q15.set()
        await message.answer("Выберите вариант мебелировки", reply_markup=kb_furniture_back)
    else:
        technics = message.text

        await state.update_data(var_technics=technics)
        await message.answer("Укажите дополнительное оборудование если оно имеется", reply_markup=kb_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q17  -->  Укажите дополнительное оборудование если оно имеется
@dp.message_handler(state=RentCommerceState.Q17)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q16.set()
        await message.answer("Имеется ли наличие техники или оборудования ?", reply_markup=kb_technics_back)
    else:
        add_technics = message.text

        await state.update_data(var_add_technics=add_technics)
        await message.answer("Укажите общую площадь (м2)", reply_markup=kb_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q18  -->  Укажите общую площадь (м2)
@dp.message_handler(state=RentCommerceState.Q18)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q17.set()
        await message.answer("Укажите дополнительное оборудование если оно имеется", reply_markup=kb_back)
    else:
        commerce_area = message.text

        await state.update_data(var_commerce_area=commerce_area)
        await message.answer("Укажите полезную площадь (м2)", reply_markup=kb_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q19  -->  Укажите полезную площадь (м2)
@dp.message_handler(state=RentCommerceState.Q19)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q18.set()
        await message.answer("Укажите общую площадь (м2)", reply_markup=kb_back)
    else:
        effective_area = message.text

        await state.update_data(var_effective_area=effective_area)
        await message.answer("Укажите общую площадь земли (м2)", reply_markup=kb_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q20  -->  Укажите общую площадь земли (м2)
@dp.message_handler(state=RentCommerceState.Q20)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q19.set()
        await message.answer("Укажите полезную площадь (м2)", reply_markup=kb_back)
    else:
        land_area = message.text

        await state.update_data(var_land_area=land_area)
        await message.answer("Опишите территорию", reply_markup=kb_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q21  -->  Опишите территорию
@dp.message_handler(state=RentCommerceState.Q21)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q20.set()
        await message.answer("Укажите общую площадь земли (м2)", reply_markup=kb_back)
    else:
        desc_territory = message.text

        await state.update_data(var_desc_territory=desc_territory)
        await message.answer("Выберите расположение", reply_markup=kb_side_building_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q22  -->  Выберите расположение
@dp.message_handler(state=RentCommerceState.Q22)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q21.set()
        await message.answer("Опишите территорию", reply_markup=kb_back)
    else:
        side_building = message.text

        await state.update_data(var_side_building=side_building)
        await message.answer("Выберите вариант парковки", reply_markup=kb_type_parking_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q23  -->  Выберите вариант парковки
@dp.message_handler(state=RentCommerceState.Q23)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q22.set()
        await message.answer("Выберите расположение", reply_markup=kb_side_building_back)
    else:
        type_parking = message.text

        await state.update_data(var_type_parking=type_parking)
        await message.answer("Выберите уровень безопасности", reply_markup=kb_security_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q24  -->  Выберите уровень безопасности
@dp.message_handler(state=RentCommerceState.Q24)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q23.set()
        await message.answer("Выберите вариант парковки", reply_markup=kb_type_parking_back)
    else:
        security = message.text

        await state.update_data(var_security=security)
        await message.answer("Выберите состояние ремонта", reply_markup=kb_repair_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q25  -->  Выберите состояние ремонта
@dp.message_handler(state=RentCommerceState.Q25)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q24.set()
        await message.answer("Выберите уровень безопасности", reply_markup=kb_security_back)
    else:
        type_repair = message.text

        await state.update_data(var_type_repair=type_repair)
        await message.answer("Выберите тип строения", reply_markup=kb_type_of_building_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q26  -->  Выберите тип строения
@dp.message_handler(state=RentCommerceState.Q26)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q25.set()
        await message.answer("Выберите состояние ремонта", reply_markup=kb_repair_back)
    else:
        type_of_building = message.text

        await state.update_data(var_type_of_building=type_of_building)
        await message.answer("Перепланировка / Пристройка", reply_markup=kb_redevelopment_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q27  -->  Перепланировка / Пристройка
@dp.message_handler(state=RentCommerceState.Q27)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q26.set()
        await message.answer("Выберите тип строения", reply_markup=kb_type_of_building_back)
    else:
        redevelopment = message.text

    await state.update_data(var_redevelopment=redevelopment)
    await message.answer("Здание", reply_markup=kb_freestanding_back)
    await RentCommerceState.next()


# Состояние RentCommerceState.Q28  -->  Здание
@dp.message_handler(state=RentCommerceState.Q28)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q27.set()
        await message.answer("Перепланировка / Пристройка", reply_markup=kb_redevelopment_back)
    else:
        freestanding = message.text

        await state.update_data(var_freestanding=freestanding)
        await message.answer("Сейчас вам надо будет выбрать под какие назначения подходит коммерческое помещение.")
        await message.answer("Выберите назначение", reply_markup=kb_appointment_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q29  -->  Выберите назначение
@dp.message_handler(state=RentCommerceState.Q29)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q28.set()
        await message.answer("Здание", reply_markup=kb_freestanding_back)
    else:
        appointments = list()
        appointments.append(message.text)
        await message.answer(f"Назначения: {appointments}")

        await state.update_data(var_appointment=appointments)
        await message.answer("Выберите еще назначение или нажмите на кнопку 'Готово ✅'",
                             reply_markup=kb_appointment_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q30  ->  Выберите назначение --> Готово ✅
@dp.message_handler(text="Готово ✅", state=RentCommerceState.Q30)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q28.set()
        await message.answer("Здание", reply_markup=kb_freestanding_back)
    else:
        answer = await state.get_data()
        appointments = answer['var_appointment']
        separator = ','
        appointments = separator.join(appointments)

        await state.update_data(var_appointment=appointments)
        await message.answer(f"Выбранные вами назначения {appointments}")
        await message.answer("/--/--/--/--/--/--/------/--/--/--/--/--/--/--/")
        await message.answer("Эксклюзив ?", reply_markup=kb_yes_or_no_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q30  -->  Выберите назначение --> Повтор
@dp.message_handler(state=RentCommerceState.Q30)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q29.set()
        await message.answer("Здание", reply_markup=kb_freestanding_back)
    else:
        answer = await state.get_data()
        appointments = answer['var_appointment']
        appointments.append(message.text)
        await message.answer(f"{appointments}")

        await state.update_data(var_appointment=appointments)
        await message.answer(f"Назначение '{message.text}' добавлено", reply_markup=kb_appointment_back)


# Состояние RentCommerceState.Q31  -->  Эксклюзив ?
@dp.message_handler(state=RentCommerceState.Q31)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q30.set()
        await message.answer("Выберите назначение", reply_markup=kb_appointment_back)
    else:
        exclusive = message.text

        await state.update_data(var_exclusive=exclusive)
        await message.answer("Выберите систему электроснабжения", reply_markup=kb_power_supply_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q32  -->  Выберите систему электроснабжения
@dp.message_handler(state=RentCommerceState.Q32)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q31.set()
        await message.answer("Эксклюзив ?", reply_markup=kb_yes_or_no_back)
    else:
        power_supply = message.text

        await state.update_data(var_power_supply=power_supply)
        await message.answer("Выберите холодную воду и канализацию", reply_markup=kb_sewerage_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q33  -->  Выберите холодную воду и канализацию
@dp.message_handler(state=RentCommerceState.Q33)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q32.set()
        await message.answer("Выберите систему электроснабжения", reply_markup=kb_power_supply_back)
    else:
        sewerage = message.text

        await state.update_data(var_sewerage=sewerage)
        await message.answer("Выберите систему газового снабжения", reply_markup=kb_system_gas_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q34  -->  Выберите систему газового снабжения
@dp.message_handler(state=RentCommerceState.Q34)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q33.set()
        await message.answer("Выберите холодную воду и канализацию", reply_markup=kb_sewerage_back)
    else:
        system_gas = message.text

        await state.update_data(var_system_gas=system_gas)
        await message.answer("Выберите систему отопления и ГВС", reply_markup=kb_system_heating_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q35  -->  Выберите систему отопления и ГВС
@dp.message_handler(state=RentCommerceState.Q35)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q34.set()
        await message.answer("Выберите систему газового снабжения", reply_markup=kb_system_gas_back)
    else:
        system_heating = message.text

        await state.update_data(var_system_heating=system_heating)
        await message.answer(f"Дайте описание арендаторов которых хочет собственник", reply_markup=kb_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q36  -->  Дайте описание арендаторов которых хочет собственник
@dp.message_handler(state=RentCommerceState.Q36)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q35.set()
        await message.answer("Выберите систему отопления и ГВС", reply_markup=kb_system_heating_back)
    else:
        tenant_description = message.text

        await state.update_data(var_tenant_description=tenant_description)
        await message.answer(f"Укажите цену за месяц ( $ )", reply_markup=kb_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q37  -->  Укажите цену за месяц ( $ )
@dp.message_handler(state=RentCommerceState.Q37)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q36.set()
        await message.answer(f"Дайте описание арендаторов которых хочет собственник", reply_markup=kb_back)
    else:
        month_price = message.text

        await state.update_data(var_month_price=month_price)
        await message.answer(f"Укажите сумму депозита", reply_markup=kb_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q38  -->  Укажите сумму депозита
@dp.message_handler(state=RentCommerceState.Q38)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q37.set()
        await message.answer(f"Укажите цену за месяц ( $ )", reply_markup=kb_back)
    else:
        deposit = message.text

        await state.update_data(var_deposit=deposit)
        await message.answer(f"Выберите за какой срок нужно внести предоплату", reply_markup=kb_prepayment_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q39  -->  Выберите за какой срок нужно внести предоплату
@dp.message_handler(state=RentCommerceState.Q39)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q38.set()
        await message.answer(f"Укажите сумму депозита", reply_markup=kb_back)
    else:
        prepayment = message.text

        await state.update_data(var_prepayment=prepayment)
        await message.answer(f"Входят ли коммунальные услуги в стоимость", reply_markup=kb_yes_or_no_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q40  -->  Входят ли коммунальные услуги в стоимость
@dp.message_handler(state=RentCommerceState.Q40)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q39.set()
        await message.answer(f"Выберите за какой срок нужно внести предоплату", reply_markup=kb_prepayment_back)
    else:
        camunal = message.text

        await state.update_data(var_camunal=camunal)
        await message.answer(f"Введите срок на который сдается квартира", reply_markup=kb_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q41  -->  Введите срок на который сдается квартира
@dp.message_handler(state=RentCommerceState.Q41)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q40.set()
        await message.answer(f"Входят ли коммунальные услуги в стоимость", reply_markup=kb_yes_or_no_back)
    else:
        apartment_completion = message.text

        await state.update_data(var_apartment_completion=apartment_completion)
        await message.answer(f"Укажите имя собственника", reply_markup=kb_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q42  -->  Укажите имя собственника
@dp.message_handler(state=RentCommerceState.Q42)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q41.set()
        await message.answer(f"Введите срок на который сдается квартира", reply_markup=kb_back)
    else:
        owner = message.text

        await state.update_data(var_owner=owner)
        await message.answer(f"Введите контактный номер телефона собственника. \nПример ввода  987777777",
                             reply_markup=kb_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q43  -->  Введите контактный номер телефона собственника. Пример ввода  987777777
@dp.message_handler(state=RentCommerceState.Q43)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q42.set()
        await message.answer(f"Укажите имя собственника", reply_markup=kb_back)
    else:
        number_phone = message.text

        await state.update_data(var_number_phone=number_phone)
        await message.answer(f"Если имеется дополнительный номер телефона, введите его",
                             reply_markup=kb_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q44  -->  Если имеется дополнительный номер телефона, введите его
@dp.message_handler(state=RentCommerceState.Q44)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q43.set()
        await message.answer(f"Введите контактный номер телефона собственника. \nПример ввода  987777777",
                             reply_markup=kb_back)
    else:
        additional_number_phone = message.text

        await state.update_data(var_additional_number_phone=additional_number_phone)
        await message.answer(f"Имеется ли информатор ?", reply_markup=kb_yes_or_no_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q45  -->  Имеется ли информатор ?
@dp.message_handler(state=RentCommerceState.Q45)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q44.set()
        await message.answer(f"Если имеется дополнительный номер телефона, введите его",
                             reply_markup=kb_back)
    else:
        informant = message.text

        await state.update_data(var_informant=informant)
        await message.answer(f"Напишите полное описание квартиры", reply_markup=kb_back)
        await RentCommerceState.next()


# Состояние RentCommerceState.Q46  -->  Напишите полное описание квартиры
@dp.message_handler(state=RentCommerceState.Q46)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q45.set()
        await message.answer(f"Имеется ли информатор ?", reply_markup=kb_yes_or_no_back)
    else:
        description = message.text

        await state.update_data(var_description=description)
        await message.answer(f"Рекламировать на торговых площадках ?", reply_markup=kb_yes_or_no_back)
        await RentCommerceState.next()


# Состояние ApartmentState.Q47  -->  Рекламировать на торговых площадках ?
@dp.message_handler(state=RentCommerceState.Q47)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentCommerceState.Q46.set()
        await message.answer(f"Напишите полное описание квартиры", reply_markup=kb_back)
    else:
        public = message.text

        await state.update_data(var_public=public)
        await message.answer(f"Все заполнил(-а) правильно ?", reply_markup=kb_yes_or_no)
        await RentCommerceState.next()


# Состояние ApartmentState.Q48  -->  Все заполнил(-а) правильно ?
@dp.message_handler(state=RentCommerceState.Q48)
async def select_district(message: types.Message, state=FSMContext):
    filled_in_correctly = message.text

    if filled_in_correctly.lower() == 'да':
        answer = await state.get_data()
        await state.reset_state()
        await message.answer('Ваша объективка отправлена)', reply_markup=kb_main_menu)
        GoogleWork().google_add_row(sheet_id='1-B80joNKTOSTIJRLiACOcfH1E3dH5yrNPbS-CU5Bvxc',
                                    name_list='Аренда коммерция',
                                    array_data=[
                                        answer['var_type_of_property'],  # --> ID
                                        answer['var_district'],  # --> Район
                                        answer['var_street'],  # --> Улица
                                        answer['var_reference_point'],  # --> Ориентир
                                        answer['var_counter_room'],  # --> Кол-во комнат
                                        answer['var_floor'],  # --> Этаж
                                        answer['var_number_floor'],  # --> Этажность
                                        answer['var_counter_dress'],  # --> Кол-во санузлов
                                        answer['var_commerce_area'],  # --> S общ
                                        answer['var_effective_area'],  # --> S полезная
                                        answer['var_land_area'],  # --> S земли
                                        answer['var_type_repair'],  # --> Ремонт
                                        answer['var_type_of_building'],  # --> Тип строения
                                        answer['var_freestanding'],  # --> Здание
                                        answer['var_tenant_description'],  # --> Описание арендатора
                                        answer['var_appointment'],  # --> Назначение
                                        answer['var_ceiling_height'],  # --> Высота потолков
                                        answer['var_redevelopment'],  # --> Перепиланировка
                                        answer['var_traffic_level'],  # --> Проходимость
                                        answer['var_desc_territory'],  # --> Описание территории
                                        answer['var_type_parking'],  # --> Парковка
                                        answer['var_side_building'],  # --> Расположение в здании
                                        answer['var_month_price'],  # --> Ежемесячная цена
                                        answer['var_deposit'],  # --> Депозит
                                        answer['var_prepayment'],  # --> Предоплата
                                        answer['var_camunal'],  # --> Комунальные услуги
                                        answer['var_apartment_completion'],  # --> Срок на который сдается
                                        answer['var_owner'],  # --> Имя собственника
                                        answer['var_number_phone'],  # --> Номер телефона
                                        answer['var_additional_number_phone'],  # AB --> Доп.номер
                                        '0',  # --> Зарубежный номер
                                        answer['var_location_the_road'],  # --> Расположение от дороги
                                        answer['var_number_home'],  # --> Номер дома
                                        answer['var_number_apartment'],  # --> Номер квартиры
                                        '0',  # --> Заголовок
                                        answer['var_description'],  # --> Описание
                                        '0',  # --> Заголовок UZB
                                        '0',  # --> Описание UZB
                                        message.from_user.full_name,  # --> Имя агента
                                        str(date.today()),  # --> Дата создания
                                        str(date.today()),  # --> Дата обзвона
                                        answer['var_informant'],  # --> Информатор
                                        answer['var_infrastructures'],  # --> Инфраструктура
                                        answer['var_distance_to_metro'],  # --> Метро
                                        answer['var_system_heating'],  # --> Отопление
                                        answer['var_sewerage'],  # --> ХВС
                                        answer['var_power_supply'],  # --> Электрика
                                        answer['var_system_gas'],  # --> Газ
                                        answer['var_furniture'],  # --> Мебель
                                        answer['var_technics'],  # --> Техника
                                        answer['var_add_technics'],  # --> Доп.оборудование
                                        answer['var_security'],  # --> Безопасность
                                        answer['var_exclusive'],  # --> Эксклюзив
                                    ])
    elif filled_in_correctly.lower() == 'нет':
        await state.reset_state()
        await message.answer('Вы отменили отправку', reply_markup=kb_main_menu)
    else:
        await message.answer('Отправлено не верное значение( Попробуйте снова')
