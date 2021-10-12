from datetime import date

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from dotenv import load_dotenv

from google_work.google_work import GoogleWork
from keyboards.default.send_by_apartment import kb_district, kb_infrastructure_back, \
    kb_location_the_road_back, kb_type_of_building_back, kb_type_of_layout_back, kb_apartment_layout_back, \
    kb_redevelopment_back, kb_side_building_back, kb_elevator_condition_back, kb_roof_condition_back, \
    kb_type_parking_back, kb_distance_to_metro_back, kb_number_room_back, kb_number_floor_back, kb_toilet_back, \
    kb_ceiling_height_back, kb_repair_back, kb_balcony_size_back, kb_furniture_back, kb_technics_back, \
    kb_yes_or_no_back, kb_air_conditioning_back, kb_registration_date_back, kb_yes_or_no
from keyboards.default.send_by_apartment import kb_main_menu
from keyboards.default.step_back import kb_back
from loader import dp
from states import ObjectState, ApartmentState

load_dotenv()


# Отслеживаем сообщение по фильтру состояния MenuState.Sale
@dp.message_handler(text="Квартира", state=ObjectState.Sale)
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
    await message.answer("Укажите квартал", reply_markup=kb_back)
    await ApartmentState.next()


# Состояние ApartmentState.Q2  -->  Укажите квартал
@dp.message_handler(state=ApartmentState.Q2)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q1.set()
        await message.answer("Выберите район", reply_markup=kb_district)
    else:
        quarter = message.text

        await state.update_data(var_quarter=quarter)
        await message.answer("Укажите улицу на которой находится дом", reply_markup=kb_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q3  -->  Укажите улицу на которой находится дом
@dp.message_handler(state=ApartmentState.Q3)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q2.set()
        await message.answer("Укажите квартал", reply_markup=kb_back)
    else:
        street = message.text

        await state.update_data(var_street=street)
        await message.answer("Укажите ориентир", reply_markup=kb_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q4  -->  Укажите ориентир
@dp.message_handler(state=ApartmentState.Q4)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q3.set()
        await message.answer("Укажите улицу на которой находится дом", reply_markup=kb_back)
    else:
        reference_point = message.text

        await state.update_data(var_reference_point=reference_point)
        await message.answer("Укажите инфраструктуру (дет.сад, магазин, больницы, транспортная развязка и т.д.)",
                             reply_markup=kb_infrastructure_back)
        await ApartmentState.next()


# Состояние CommerceState.Infrastructure  -->  Укажите инфраструктуру
@dp.message_handler(text="Готово ✅", state=ApartmentState.Infrastructure)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q4.set()
        await message.answer("Укажите ориентир", reply_markup=kb_back)
    else:
        answer = await state.get_data()
        infrastructures = answer['var_infrastructures']
        separator = ','
        infrastructures = separator.join(infrastructures)

        await message.answer(f'Инфраструктура которую вы выбрали: {infrastructures}')
        await message.answer("/--/--/--/--/--/--/------/--/--/--/--/--/--/--/")
        await state.update_data(var_infrastructures=infrastructures)

        await message.answer("Выберите расположение от дороги", reply_markup=kb_location_the_road_back)
        await ApartmentState.next()


# Состояние CommerceState.Q5  -->  Укажите инфраструктуру (дет.сад, магазин, больницы, транспортная развязка и т.д.)
@dp.message_handler(state=ApartmentState.Q5)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q4.set()
        await message.answer("Укажите ориентир", reply_markup=kb_back)
    else:
        infrastructure = message.text
        infrastructures = list()
        infrastructures.append(infrastructure)
        await state.update_data(var_infrastructures=infrastructures)
        await message.answer("Выберите еще варианты или нажмите на кнопку 'Готово ✅",
                             reply_markup=kb_infrastructure_back)
        await ApartmentState.Infrastructure.set()


# Состояние CommerceState.Infrastructure  -->  Повтор
@dp.message_handler(state=ApartmentState.Infrastructure)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q4.set()
        await message.answer("Укажите ориентир", reply_markup=kb_back)
    else:
        infrastructure = message.text
        answer = await state.get_data()
        infrastructures = answer['var_infrastructures']
        infrastructures.append(infrastructure)
        await state.update_data(var_infrastructures=infrastructures)
        await message.answer(f"{infrastructures}", reply_markup=kb_infrastructure_back)


# Состояние ApartmentState.Q6  -->  Выберите расположение от дороги
@dp.message_handler(state=ApartmentState.Q6)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q5.set()
        await message.answer("Укажите инфраструктуру (дет.сад, магазин, больницы, транспортная развязка и т.д.)",
                             reply_markup=kb_infrastructure_back)
    else:
        location_the_road = message.text

        await state.update_data(var_location_the_road=location_the_road)
        await message.answer(f"Укажите номер дома", reply_markup=kb_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q7  -->  Укажите номер дома
@dp.message_handler(state=ApartmentState.Q7)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q6.set()
        await message.answer("Выберите расположение от дороги", reply_markup=kb_location_the_road_back)
    else:
        number_home = message.text

        await state.update_data(var_number_home=number_home)
        await message.answer(f"Укажите номер квартиры", reply_markup=kb_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q8  -->  Укажите номер квартиры
@dp.message_handler(state=ApartmentState.Q8)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q7.set()
        await message.answer(f"Укажите номер дома", reply_markup=kb_back)
    else:
        number_apartment = message.text

        await state.update_data(var_number_apartment=number_apartment)
        await message.answer(f"Выберите тип строения", reply_markup=kb_type_of_building_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q9  -->  Выберите тип строения
@dp.message_handler(state=ApartmentState.Q9)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q8.set()
        await message.answer(f"Укажите номер квартиры", reply_markup=kb_back)
    else:
        type_building = message.text

        await state.update_data(var_type_building=type_building)
        await message.answer(f"Выберите тип планировки", reply_markup=kb_type_of_layout_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q10  -->  Выберите тип планировки
@dp.message_handler(state=ApartmentState.Q10)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q9.set()
        await message.answer(f"Выберите тип строения", reply_markup=kb_type_of_building_back)
    else:
        type_layout = message.text

        await state.update_data(var_type_layout=type_layout)
        await message.answer(f"Выберите вид планировки", reply_markup=kb_apartment_layout_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q11  -->  Выберите вид планировки
@dp.message_handler(state=ApartmentState.Q11)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q10.set()
        await message.answer(f"Выберите тип планировки", reply_markup=kb_type_of_layout_back)
    else:
        apartment_layout = message.text

        await state.update_data(var_apartment_layout=apartment_layout)
        await message.answer(f"Имеется ли перепланировка ?", reply_markup=kb_redevelopment_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q12  -->  Имеется ли перепланировка ?
@dp.message_handler(state=ApartmentState.Q12)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q11.set()
        await message.answer(f"Выберите вид планировки", reply_markup=kb_apartment_layout_back)
    else:
        redevelopment = message.text

        await state.update_data(var_redevelopment=redevelopment)
        await message.answer(f"Выберите расположение квартиры в доме", reply_markup=kb_side_building_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q13  -->  Выберите расположение квартиры в доме
@dp.message_handler(state=ApartmentState.Q13)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q12.set()
        await message.answer(f"Имеется ли перепланировка ?", reply_markup=kb_redevelopment_back)
    else:
        side_building = message.text

        await state.update_data(var_side_building=side_building)
        await message.answer(f"Выберите состояние лифта", reply_markup=kb_elevator_condition_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q14  -->  Выберите состояние лифта
@dp.message_handler(state=ApartmentState.Q14)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q13.set()
        await message.answer(f"Выберите расположение квартиры в доме", reply_markup=kb_side_building_back)
    else:
        elevator_condition = message.text

        await state.update_data(var_elevator_condition=elevator_condition)
        await message.answer(f"Выберите состояние крыши", reply_markup=kb_roof_condition_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q15  -->  Выберите состояние крыши
@dp.message_handler(state=ApartmentState.Q15)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q14.set()
        await message.answer(f"Выберите состояние лифта", reply_markup=kb_elevator_condition_back)
    else:
        roof_condition = message.text

        await state.update_data(var_roof_condition=roof_condition)
        await message.answer(f"Выберите вариант парковки", reply_markup=kb_type_parking_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q16  -->  Выберите вариант парковки
@dp.message_handler(state=ApartmentState.Q16)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q15.set()
        await message.answer(f"Выберите состояние крыши", reply_markup=kb_roof_condition_back)
    else:
        type_parking = message.text

        await state.update_data(var_type_parking=type_parking)
        await message.answer(f"Выберите расстояние до метро", reply_markup=kb_distance_to_metro_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q17  -->  Выберите расстояние до метро
@dp.message_handler(state=ApartmentState.Q17)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q16.set()
        await message.answer(f"Выберите вариант парковки", reply_markup=kb_type_parking_back)
    else:
        distance_to_metro = message.text

        await state.update_data(var_distance_to_metro=distance_to_metro)
        await message.answer(f"Укажите количество комнат", reply_markup=kb_number_room_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q18  -->  Укажите количество комнат
@dp.message_handler(state=ApartmentState.Q18)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q17.set()
        await message.answer(f"Выберите расстояние до метро", reply_markup=kb_distance_to_metro_back)
    else:
        counter_room = message.text

        await state.update_data(var_counter_room=counter_room)
        await message.answer(f"Укажите этаж", reply_markup=kb_number_floor_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q19  -->  Укажите этаж
@dp.message_handler(state=ApartmentState.Q19)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q18.set()
        await message.answer(f"Укажите количество комнат", reply_markup=kb_number_room_back)
    else:
        floor = message.text

        await state.update_data(var_floor=floor)
        await message.answer(f"Укажите этажность", reply_markup=kb_number_floor_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q20  -->  Укажите этажность
@dp.message_handler(state=ApartmentState.Q20)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q19.set()
        await message.answer(f"Укажите этаж", reply_markup=kb_number_floor_back)
    else:
        number_floor = message.text

        await state.update_data(var_number_floor=number_floor)
        await message.answer(f"Выберите тип сан. узла", reply_markup=kb_toilet_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q21  -->  Выберите тип сан. узла
@dp.message_handler(state=ApartmentState.Q21)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q20.set()
        await message.answer(f"Укажите этажность", reply_markup=kb_number_floor_back)
    else:
        type_dress = message.text

        await state.update_data(var_type_dress=type_dress)
        await message.answer(f"Укажите высоту потолков", reply_markup=kb_ceiling_height_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q22  -->  Укажите высоту потолков
@dp.message_handler(state=ApartmentState.Q22)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q21.set()
        await message.answer(f"Выберите тип сан. узла", reply_markup=kb_toilet_back)
    else:
        ceiling_height = message.text

        await state.update_data(var_ceiling_height=ceiling_height)
        await message.answer(f"Выберите состояние ремонта", reply_markup=kb_repair_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q23  -->  Выберите состояние ремонта
@dp.message_handler(state=ApartmentState.Q23)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q22.set()
        await message.answer(f"Укажите высоту потолков", reply_markup=kb_ceiling_height_back)
    else:
        repair = message.text

        await state.update_data(var_repair=repair)
        await message.answer(f"Укажите общую площадь квартиры (м2)", reply_markup=kb_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q24  -->  Укажите общую площадь квартиры (м2)
@dp.message_handler(state=ApartmentState.Q24)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q23.set()
        await message.answer(f"Выберите состояние ремонта", reply_markup=kb_repair_back)
    else:
        apartment_area = message.text

        await state.update_data(var_apartment_area=apartment_area)
        await message.answer(f"Укажите площадь кухни (м2)", reply_markup=kb_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q25  -->  Укажите площадь кухни (м2)
@dp.message_handler(state=ApartmentState.Q25)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q24.set()
        await message.answer(f"Укажите общую площадь квартиры (м2)", reply_markup=kb_back)
    else:
        kitchen_area = message.text

        await state.update_data(var_kitchen_area=kitchen_area)
        await message.answer(f"Выберите габариты балкона", reply_markup=kb_balcony_size_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q26  -->  Выберите габариты балкона
@dp.message_handler(state=ApartmentState.Q26)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q25.set()
        await message.answer(f"Укажите площадь кухни (м2)", reply_markup=kb_back)
    else:
        balcony_size = message.text

        await state.update_data(var_balcony_size=balcony_size)
        await message.answer(f"Выберите вариант мебелировки", reply_markup=kb_furniture_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q27  -->  Выберите вариант мебелировки
@dp.message_handler(state=ApartmentState.Q27)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q26.set()
        await message.answer(f"Выберите габариты балкона", reply_markup=kb_balcony_size_back)
    else:
        furniture = message.text

        await state.update_data(var_furniture=furniture)
        await message.answer(f"Имеются ли техника ?", reply_markup=kb_technics_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q28  -->  Имеются ли техника ?
@dp.message_handler(state=ApartmentState.Q28)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q27.set()
        await message.answer(f"Выберите вариант мебелировки", reply_markup=kb_furniture_back)
    else:
        technics = message.text

        await state.update_data(var_technics=technics)
        await message.answer(f"Имеется ли в наличии пластиковые окна?", reply_markup=kb_yes_or_no_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q29  -->  Имеются ли пластиковые окна ?
@dp.message_handler(state=ApartmentState.Q29)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q28.set()
        await message.answer(f"Имеются ли техника ?", reply_markup=kb_technics_back)
    else:
        plastic_windows = message.text

        await state.update_data(var_plastic_windows=plastic_windows)
        await message.answer(f"Имеется ли в наличии кондиционер ?", reply_markup=kb_air_conditioning_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q30  -->  Имеется ли в наличии кондиционер ?
@dp.message_handler(state=ApartmentState.Q30)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q29.set()
        await message.answer(f"Имеется ли в наличии пластиковые окна?", reply_markup=kb_yes_or_no_back)
    else:
        condition = message.text

        await state.update_data(var_condition=condition)
        await message.answer(f"Укажите имя собственника", reply_markup=kb_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q31  -->  Укажите имя собственника
@dp.message_handler(state=ApartmentState.Q31)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q30.set()
        await message.answer(f"Имеется ли в наличии кондиционер ?", reply_markup=kb_air_conditioning_back)
    else:
        owner = message.text

        await state.update_data(var_owner=owner)
        await message.answer(f"Введите контактный номер телефона собственника. \nПример ввода  987777777",
                             reply_markup=kb_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q32  -->  Введите контактный номер телефона собственника. Пример ввода  987777777
@dp.message_handler(state=ApartmentState.Q32)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q31.set()
        await message.answer(f"Укажите имя собственника", reply_markup=kb_back)
    else:
        number_phone = message.text

        await state.update_data(var_number_phone=number_phone)
        await message.answer(f"Если имеется дополнительный номер телефона, введите его",
                             reply_markup=kb_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q33  -->  Если имеется дополнительный номер телефона, введите его
@dp.message_handler(state=ApartmentState.Q33)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q32.set()
        await message.answer(f"Введите контактный номер телефона собственника. \nПример ввода  987777777",
                             reply_markup=kb_back)
    else:
        additional_number_phone = message.text

        await state.update_data(var_additional_number_phone=additional_number_phone)
        await message.answer(f"Имеется ли информатор ?", reply_markup=kb_yes_or_no_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q34  -->  Имеется ли информатор ?
@dp.message_handler(state=ApartmentState.Q34)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q33.set()
        await message.answer(f"Если имеется дополнительный номер телефона, введите его",
                             reply_markup=kb_back)
    else:
        informant = message.text

        await state.update_data(var_informant=informant)
        await message.answer(f"Укажите стартовую цену ( $ )", reply_markup=kb_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q35  -->  Укажите стартовую цену ( $ )
@dp.message_handler(state=ApartmentState.Q35)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q34.set()
        await message.answer(f"Имеется ли информатор ?", reply_markup=kb_yes_or_no_back)
    else:
        price = message.text

        await state.update_data(var_price=price)
        await message.answer(f"Стартовая\nС процентами\nЦена на руки", reply_markup=kb_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q36  -->  Стартовая С процентами Цена на руки
@dp.message_handler(state=ApartmentState.Q36)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q35.set()
        await message.answer(f"Укажите стартовую цену ( $ )", reply_markup=kb_back)
    else:
        full_price = message.text

        await state.update_data(var_full_price=full_price)
        await message.answer(f"Укажите количество прописанных человек", reply_markup=kb_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q37  -->  Укажите количество прописанных человек
@dp.message_handler(state=ApartmentState.Q37)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q36.set()
        await message.answer(f"Стартовая\nС процентами\nЦена на руки", reply_markup=kb_back)
    else:
        scribed_people = message.text

        await state.update_data(var_scribed_people=scribed_people)
        await message.answer(f"Выберите время которое прошло с последнего оформления",
                             reply_markup=kb_registration_date_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q38  -->  Выберите время которое прошло с последнего оформления
@dp.message_handler(state=ApartmentState.Q38)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q37.set()
        await message.answer(f"Укажите количество прописанных человек", reply_markup=kb_back)
    else:
        checkout_time = message.text

        await state.update_data(var_checkout_time=checkout_time)
        await message.answer(f"Подойдет ли под офис ?", reply_markup=kb_yes_or_no_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q39  -->  "Подойдет ли под офис ?
@dp.message_handler(state=ApartmentState.Q39)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q38.set()
        await message.answer(f"Выберите время которое прошло с последнего оформления",
                             reply_markup=kb_registration_date_back)
    else:
        under_to_office = message.text

        await state.update_data(var_under_to_office=under_to_office)
        await message.answer(f"Эксклюзив ?", reply_markup=kb_yes_or_no_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q40  -->  Эксклюзив ?
@dp.message_handler(state=ApartmentState.Q40)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q39.set()
        await message.answer(f"Подойдет ли под офис ?", reply_markup=kb_yes_or_no_back)
    else:
        exclusive = message.text

        await state.update_data(var_exclusive=exclusive)
        await message.answer(f"Напишите полное описание квартиры", reply_markup=kb_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q41  -->  Напишите полное описание квартиры
@dp.message_handler(state=ApartmentState.Q41)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q40.set()
        await message.answer(f"Эксклюзив ?", reply_markup=kb_yes_or_no_back)
    else:
        description = message.text

        await state.update_data(var_description=description)
        await message.answer(f"Рекламировать на торговых площадках ?", reply_markup=kb_yes_or_no_back)
        await ApartmentState.next()


# Состояние ApartmentState.Q42  -->  Рекламировать на торговых площадках ?
@dp.message_handler(state=ApartmentState.Q42)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await ApartmentState.Q41.set()
        await message.answer(f"Напишите полное описание квартиры", reply_markup=kb_back)
    else:
        public = message.text

        await state.update_data(var_public=public)
        await message.answer(f"Все заполнил(-а) правильно ?", reply_markup=kb_yes_or_no)
        await ApartmentState.next()


# Состояние ApartmentState.Q43  -->  Все заполнил(-а) правильно ?
@dp.message_handler(state=ApartmentState.Q43)
async def select_district(message: types.Message, state=FSMContext):
    filled_in_correctly = message.text
    answer = await state.get_data()
    user_name = message.from_user.full_name

    if filled_in_correctly.lower() == 'да':
        answer = await state.get_data()
        await state.reset_state()
        await message.answer('Ваша объективка отправлена)', reply_markup=kb_main_menu)
        GoogleWork().google_add_row(sheet_id='1-B80joNKTOSTIJRLiACOcfH1E3dH5yrNPbS-CU5Bvxc',
                                    name_list='Продажа квартиры',
                                    array_data=[answer['var_type_of_property'],
                                                answer['var_quarter'],
                                                answer['var_reference_point'],
                                                answer['var_street'],
                                                answer['var_counter_room'],
                                                answer['var_floor'],
                                                answer['var_number_floor'],
                                                answer['var_apartment_area'],
                                                answer['var_balcony_size'],
                                                answer['var_type_dress'],
                                                answer['var_repair'],
                                                answer['var_type_building'],
                                                answer['var_apartment_layout'],
                                                answer['var_type_layout'],
                                                answer['var_side_building'],
                                                answer['var_ceiling_height'],
                                                answer['var_furniture'],
                                                answer['var_technics'],
                                                answer['var_condition'],
                                                answer['var_kitchen_area'],
                                                answer['var_plastic_windows'],
                                                answer['var_price'],
                                                answer['var_full_price'],
                                                answer['var_owner'],
                                                answer['var_number_phone'],
                                                answer['var_additional_number_phone'],
                                                '0',
                                                answer['var_location_the_road'],
                                                answer['var_distance_to_metro'],
                                                answer['var_number_home'],
                                                answer['var_number_apartment'],
                                                '0',
                                                '0',
                                                '0',
                                                '0',
                                                user_name,
                                                str(date.today()),
                                                str(date.today()),
                                                answer['var_informant'],
                                                answer['var_district'],
                                                answer['var_infrastructures'],
                                                answer['var_redevelopment'],
                                                answer['var_type_parking'],
                                                answer['var_description'],
                                                answer['var_elevator_condition'],
                                                answer['var_roof_condition'],
                                                answer['var_checkout_time'],
                                                answer['var_scribed_people'],
                                                answer['var_under_to_office'],
                                                answer['var_exclusive'],
                                                answer['var_public']]
                                    )
    elif filled_in_correctly.lower() == 'нет':
        await state.reset_state()
        await message.answer('Вы отменили отправку', reply_markup=kb_main_menu)
    else:
        await message.answer('Отправлено не верное значение( Попробуйте снова')
