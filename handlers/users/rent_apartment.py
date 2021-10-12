from datetime import date

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from google_work.google_work import GoogleWork
from keyboards.default.rent_apartment import kb_district, kb_location_the_road_back, kb_infrastructure_back, \
    kb_type_of_building_back, kb_type_of_layout_back, kb_apartment_layout_back, kb_redevelopment_back, \
    kb_side_building_back, kb_entrance_back, kb_elevator_condition_back, kb_roof_condition_back, kb_type_parking_back, \
    kb_distance_to_metro_back, kb_number_room_back, kb_number_floor_back, kb_toilet_back, kb_ceiling_height_back, \
    kb_repair_back, kb_balcony_size_back, kb_furniture_back, kb_technics_back, kb_air_conditioning_back, \
    kb_prepayment_back, kb_main_menu, kb_yes_or_no, kb_yes_or_no_back
from keyboards.default.step_back import kb_back
from loader import dp
from states import ObjectState, RentApartmentState


# Отслеживаем сообщение по фильтру состояния ObjectState.Rent
@dp.message_handler(text="Квартира", state=ObjectState.Rent)
async def select_district(message: types.Message, state=FSMContext):
    # Получаем текст сообщения, а после записываем значение в переменную district
    type_of_service = message.text

    # Записываем полученное значение в словарь машины состояний под ключом var_type_of_service
    await state.update_data(var_type_of_service=type_of_service)
    # Отправляем сообщение и массив кнопок
    await message.answer("Выберите район", reply_markup=kb_district)
    # Переходим в машину состояний RentApartmentState
    await RentApartmentState.next()


# Состояние RentApartmentState.Q1  -->  Выберите район
@dp.message_handler(state=RentApartmentState.Q1)
async def select_district(message: types.Message, state=FSMContext):
    district = message.text

    await state.update_data(var_district=district)
    await message.answer("Укажите квартал или улицу на которой находится дом", reply_markup=kb_back)
    await RentApartmentState.next()


# Состояние RentApartmentState.Q2  -->  Укажите квартал или улицу на которой находится дом
@dp.message_handler(state=RentApartmentState.Q2)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q1.set()
        await message.answer("Выберите район", reply_markup=kb_district)
    else:
        quarter = message.text

        await state.update_data(var_quarter=quarter)
        await message.answer("Укажите ориентир", reply_markup=kb_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q3  -->  Укажите квартал или улицу на которой находится дом
@dp.message_handler(state=RentApartmentState.Q3)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q2.set()
        await message.answer("Укажите квартал или улицу на которой находится дом", reply_markup=kb_back)
    else:
        reference_point = message.text

        await state.update_data(var_reference_point=reference_point)
        await message.answer("Выберите инфраструктуру", reply_markup=kb_back)
        await RentApartmentState.next()


# Состояние CommerceState.Infrastructure  -->  Укажите инфраструктуру
@dp.message_handler(text="Готово ✅", state=RentApartmentState.Infrastructure)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q3.set()
        await message.answer("Укажите квартал или улицу на которой находится дом", reply_markup=kb_back)
    else:
        answer = await state.get_data()
        infrastructures = answer['var_infrastructures']
        separator = ','
        infrastructures = separator.join(infrastructures)

        await message.answer(f'Инфраструктура которую вы выбрали: {infrastructures}')
        await message.answer("/--/--/--/--/--/--/------/--/--/--/--/--/--/--/")
        await state.update_data(var_infrastructures=infrastructures)

        await message.answer("Выберите расположение от дороги", reply_markup=kb_location_the_road_back)
        await RentApartmentState.next()


# Состояние CommerceState.Q4  -->  Укажите инфраструктуру (дет.сад, магазин, больницы, транспортная развязка и т.д.)
@dp.message_handler(state=RentApartmentState.Q4)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q3.set()
        await message.answer("Укажите квартал или улицу на которой находится дом", reply_markup=kb_back)
    else:
        infrastructure = message.text
        infrastructures = list()
        infrastructures.append(infrastructure)
        await state.update_data(var_infrastructures=infrastructures)
        await message.answer("Выберите еще варианты или нажмите на кнопку 'Готово ✅",
                             reply_markup=kb_infrastructure_back)
        await RentApartmentState.Infrastructure.set()


# Состояние CommerceState.Infrastructure  -->  Повтор
@dp.message_handler(state=RentApartmentState.Infrastructure)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q3.set()
        await message.answer("Укажите квартал или улицу на которой находится дом", reply_markup=kb_back)
    else:
        infrastructure = message.text
        answer = await state.get_data()
        infrastructures = answer['var_infrastructures']
        infrastructures.append(infrastructure)
        await state.update_data(var_infrastructures=infrastructures)
        await message.answer(f"{infrastructures}", reply_markup=kb_infrastructure_back)


# Состояние RentApartmentState.Q5  -->  Выберите расположение от дороги
@dp.message_handler(state=RentApartmentState.Q5)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q4.set()
        await message.answer("Укажите инфраструктуру (дет.сад, магазин, больницы, транспортная развязка и т.д.)",
                             reply_markup=kb_infrastructure_back)
    else:
        location_the_road = message.text

        await state.update_data(var_location_the_road=location_the_road)
        await message.answer(f"Укажите номер дома", reply_markup=kb_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q6  -->  Укажите номер дома
@dp.message_handler(state=RentApartmentState.Q6)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q5.set()
        await message.answer("Выберите расположение от дороги", reply_markup=kb_location_the_road_back)
    else:
        number_home = message.text

        await state.update_data(var_number_home=number_home)
        await message.answer(f"Укажите номер квартиры", reply_markup=kb_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q7  -->  Укажите номер квартиры
@dp.message_handler(state=RentApartmentState.Q7)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q6.set()
        await message.answer(f"Укажите номер дома", reply_markup=kb_back)
    else:
        number_apartment = message.text

        await state.update_data(var_number_apartment=number_apartment)
        await message.answer(f"Выберите тип строения", reply_markup=kb_type_of_building_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q8  -->  Выберите тип строения
@dp.message_handler(state=RentApartmentState.Q8)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q7.set()
        await message.answer(f"Укажите номер квартиры", reply_markup=kb_back)
    else:
        type_building = message.text

        await state.update_data(var_type_building=type_building)
        await message.answer(f"Выберите тип планировки", reply_markup=kb_type_of_layout_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q9  -->  Выберите тип планировки
@dp.message_handler(state=RentApartmentState.Q9)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q8.set()
        await message.answer(f"Выберите тип строения", reply_markup=kb_type_of_building_back)
    else:
        type_layout = message.text

        await state.update_data(var_type_layout=type_layout)
        await message.answer(f"Выберите вид планировки", reply_markup=kb_apartment_layout_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q10  -->  Выберите вид планировки
@dp.message_handler(state=RentApartmentState.Q10)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q9.set()
        await message.answer(f"Выберите тип планировки", reply_markup=kb_type_of_layout_back)
    else:
        apartment_layout = message.text

        await state.update_data(var_apartment_layout=apartment_layout)
        await message.answer(f"Имеется ли перепланировка ?", reply_markup=kb_redevelopment_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q11  -->  Имеется ли перепланировка ?
@dp.message_handler(state=RentApartmentState.Q11)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q10.set()
        await message.answer(f"Выберите вид планировки", reply_markup=kb_apartment_layout_back)
    else:
        redevelopment = message.text

        await state.update_data(var_redevelopment=redevelopment)
        await message.answer(f"Выберите расположение квартиры в доме", reply_markup=kb_side_building_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q12  -->  Выберите расположение квартиры в доме
@dp.message_handler(state=RentApartmentState.Q12)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q11.set()
        await message.answer(f"Имеется ли перепланировка ?", reply_markup=kb_redevelopment_back)
    else:
        side_building = message.text

        await state.update_data(var_side_building=side_building)
        await message.answer(f"Выберите вариант состояния подъезда", reply_markup=kb_entrance_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q13  -->  Выберите вариант состояния подъезда
@dp.message_handler(state=RentApartmentState.Q13)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q12.set()
        await message.answer(f"Выберите расположение квартиры в доме", reply_markup=kb_side_building_back)
    else:
        entrance = message.text

        await state.update_data(var_entrance=entrance)
        await message.answer(f"Выберите состояние лифта", reply_markup=kb_elevator_condition_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q14  -->  Выберите состояние лифта
@dp.message_handler(state=RentApartmentState.Q14)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q13.set()
        await message.answer(f"Выберите вариант состояния подъезда", reply_markup=kb_entrance_back)
    else:
        elevator_condition = message.text

        await state.update_data(var_elevator_condition=elevator_condition)
        await message.answer(f"Выберите состояние крыши", reply_markup=kb_roof_condition_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q15  -->  Выберите состояние крыши
@dp.message_handler(state=RentApartmentState.Q15)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q14.set()
        await message.answer(f"Выберите состояние лифта", reply_markup=kb_elevator_condition_back)
    else:
        roof_condition = message.text

        await state.update_data(var_roof_condition=roof_condition)
        await message.answer(f"Выберите вариант парковки", reply_markup=kb_type_parking_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q16  -->  Выберите вариант парковки
@dp.message_handler(state=RentApartmentState.Q16)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q15.set()
        await message.answer(f"Выберите состояние крыши", reply_markup=kb_roof_condition_back)
    else:
        type_parking = message.text

        await state.update_data(var_type_parking=type_parking)
        await message.answer(f"Выберите расстояние до метро", reply_markup=kb_distance_to_metro_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q17  -->  Выберите расстояние до метро
@dp.message_handler(state=RentApartmentState.Q17)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q16.set()
        await message.answer(f"Выберите вариант парковки", reply_markup=kb_type_parking_back)
    else:
        distance_to_metro = message.text

        await state.update_data(var_distance_to_metro=distance_to_metro)
        await message.answer(f"Укажите количество комнат", reply_markup=kb_number_room_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q18  -->  Укажите количество комнат
@dp.message_handler(state=RentApartmentState.Q18)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q17.set()
        await message.answer(f"Выберите расстояние до метро", reply_markup=kb_distance_to_metro_back)
    else:
        counter_room = message.text

        await state.update_data(var_counter_room=counter_room)
        await message.answer(f"Укажите этаж", reply_markup=kb_number_floor_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q19  -->  Укажите этаж
@dp.message_handler(state=RentApartmentState.Q19)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q18.set()
        await message.answer(f"Укажите количество комнат", reply_markup=kb_number_room_back)
    else:
        floor = message.text

        await state.update_data(var_floor=floor)
        await message.answer(f"Укажите этажность", reply_markup=kb_number_floor_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q20  -->  Укажите этажность
@dp.message_handler(state=RentApartmentState.Q20)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q19.set()
        await message.answer(f"Укажите этаж", reply_markup=kb_number_floor_back)
    else:
        number_floor = message.text

        await state.update_data(var_number_floor=number_floor)
        await message.answer(f"Выберите тип сан. узла", reply_markup=kb_toilet_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q21  -->  Выберите тип сан. узла
@dp.message_handler(state=RentApartmentState.Q21)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q20.set()
        await message.answer(f"Укажите этажность", reply_markup=kb_number_floor_back)
    else:
        type_dress = message.text

        await state.update_data(var_type_dress=type_dress)
        await message.answer(f"Укажите высоту потолков", reply_markup=kb_ceiling_height_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q22  -->  Укажите высоту потолков
@dp.message_handler(state=RentApartmentState.Q22)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q21.set()
        await message.answer(f"Выберите тип сан. узла", reply_markup=kb_toilet_back)
    else:
        ceiling_height = message.text

        await state.update_data(var_ceiling_height=ceiling_height)
        await message.answer(f"Выберите состояние ремонта", reply_markup=kb_repair_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q23  -->  Выберите состояние ремонта
@dp.message_handler(state=RentApartmentState.Q23)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q22.set()
        await message.answer(f"Укажите высоту потолков", reply_markup=kb_ceiling_height_back)
    else:
        repair = message.text

        await state.update_data(var_repair=repair)
        await message.answer(f"Укажите общую площадь квартиры (м2)", reply_markup=kb_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q24  -->  Укажите общую площадь квартиры (м2)
@dp.message_handler(state=RentApartmentState.Q24)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q23.set()
        await message.answer(f"Выберите состояние ремонта", reply_markup=kb_repair_back)
    else:
        apartment_area = message.text

        await state.update_data(var_apartment_area=apartment_area)
        await message.answer(f"Укажите площадь кухни (м2)", reply_markup=kb_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q25  -->  Укажите площадь кухни (м2)
@dp.message_handler(state=RentApartmentState.Q25)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q24.set()
        await message.answer(f"Укажите общую площадь квартиры (м2)", reply_markup=kb_back)
    else:
        kitchen_area = message.text

        await state.update_data(var_kitchen_area=kitchen_area)
        await message.answer(f"Выберите габариты балкона", reply_markup=kb_balcony_size_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q26  -->  Выберите габариты балкона
@dp.message_handler(state=RentApartmentState.Q26)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q25.set()
        await message.answer(f"Укажите площадь кухни (м2)", reply_markup=kb_back)
    else:
        balcony_size = message.text

        await state.update_data(var_balcony_size=balcony_size)
        await message.answer(f"Выберите вариант мебелировки", reply_markup=kb_furniture_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q27  -->  Выберите вариант мебелировки
@dp.message_handler(state=RentApartmentState.Q27)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q26.set()
        await message.answer(f"Выберите габариты балкона", reply_markup=kb_balcony_size_back)
    else:
        furniture = message.text

        await state.update_data(var_furniture=furniture)
        await message.answer(f"Имеются ли техника ?", reply_markup=kb_technics_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q28  -->  Имеются ли техника ?
@dp.message_handler(state=RentApartmentState.Q28)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q27.set()
        await message.answer(f"Выберите вариант мебелировки", reply_markup=kb_furniture_back)
    else:
        technics = message.text

        await state.update_data(var_technics=technics)
        await message.answer(f"Имеется ли в наличии пластиковые окна?", reply_markup=kb_yes_or_no_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q29  -->  Имеются ли пластиковые окна ?
@dp.message_handler(state=RentApartmentState.Q29)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q28.set()
        await message.answer(f"Имеются ли техника ?", reply_markup=kb_technics_back)
    else:
        plastic_windows = message.text

        await state.update_data(var_plastic_windows=plastic_windows)
        await message.answer(f"Имеется ли в наличии кондиционер ?", reply_markup=kb_air_conditioning_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q30  -->  Имеется ли в наличии кондиционер ?
@dp.message_handler(state=RentApartmentState.Q30)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q29.set()
        await message.answer(f"Имеется ли в наличии пластиковые окна?", reply_markup=kb_yes_or_no_back)
    else:
        condition = message.text

        await state.update_data(var_condition=condition)
        await message.answer(f"Укажите имя собственника", reply_markup=kb_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q31  -->  Укажите имя собственника
@dp.message_handler(state=RentApartmentState.Q31)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q30.set()
        await message.answer(f"Имеется ли в наличии кондиционер ?", reply_markup=kb_air_conditioning_back)
    else:
        owner = message.text

        await state.update_data(var_owner=owner)
        await message.answer(f"Введите контактный номер телефона собственника. \nПример ввода  987777777",
                             reply_markup=kb_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q32  -->  Введите контактный номер телефона собственника. Пример ввода  987777777
@dp.message_handler(state=RentApartmentState.Q32)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q31.set()
        await message.answer(f"Укажите имя собственника", reply_markup=kb_back)
    else:
        number_phone = message.text

        await state.update_data(var_number_phone=number_phone)
        await message.answer(f"Если имеется дополнительный номер телефона, введите его",
                             reply_markup=kb_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q33  -->  Если имеется дополнительный номер телефона, введите его
@dp.message_handler(state=RentApartmentState.Q33)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q32.set()
        await message.answer(f"Введите контактный номер телефона собственника. \nПример ввода  987777777",
                             reply_markup=kb_back)
    else:
        additional_number_phone = message.text

        await state.update_data(var_additional_number_phone=additional_number_phone)
        await message.answer(f"Имеется ли информатор ?", reply_markup=kb_yes_or_no_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q34  -->  Имеется ли информатор ?
@dp.message_handler(state=RentApartmentState.Q34)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q33.set()
        await message.answer(f"Если имеется дополнительный номер телефона, введите его",
                             reply_markup=kb_back)
    else:
        informant = message.text

        await state.update_data(var_informant=informant)
        await message.answer(f"Дайте описание соседей", reply_markup=kb_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q35  -->  Дайте описание соседей
@dp.message_handler(state=RentApartmentState.Q35)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q34.set()
        await message.answer(f"Имеется ли информатор ?", reply_markup=kb_yes_or_no_back)
    else:
        neighbors_description = message.text

        await state.update_data(var_neighbors_description=neighbors_description)
        await message.answer(f"Дайте описание арендаторов которых хочет собственник", reply_markup=kb_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q36  -->  Дайте описание арендаторов которых хочет собственник
@dp.message_handler(state=RentApartmentState.Q36)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q35.set()
        await message.answer(f"Дайте описание соседей", reply_markup=kb_back)
    else:
        tenant_description = message.text

        await state.update_data(var_tenant_description=tenant_description)
        await message.answer(f"Укажите цену за месяц ( $ )", reply_markup=kb_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q37  -->  Укажите цену за месяц ( $ )
@dp.message_handler(state=RentApartmentState.Q37)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q36.set()
        await message.answer(f"Дайте описание арендаторов которых хочет собственник", reply_markup=kb_back)
    else:
        month_price = message.text

        await state.update_data(var_month_price=month_price)
        await message.answer(f"Укажите сумму депозита", reply_markup=kb_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q38  -->  Укажите сумму депозита
@dp.message_handler(state=RentApartmentState.Q38)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q37.set()
        await message.answer(f"Укажите цену за месяц ( $ )", reply_markup=kb_back)
    else:
        deposit = message.text

        await state.update_data(var_deposit=deposit)
        await message.answer(f"Выберите за какой срок нужно внести предоплату", reply_markup=kb_prepayment_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q39  -->  Выберите за какой срок нужно внести предоплату
@dp.message_handler(state=RentApartmentState.Q39)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q38.set()
        await message.answer(f"Укажите сумму депозита", reply_markup=kb_back)
    else:
        prepayment = message.text

        await state.update_data(var_prepayment=prepayment)
        await message.answer(f"Входят ли коммунальные услуги в стоимость", reply_markup=kb_yes_or_no_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q40  -->  Входят ли коммунальные услуги в стоимость
@dp.message_handler(state=RentApartmentState.Q40)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q39.set()
        await message.answer(f"Выберите за какой срок нужно внести предоплату", reply_markup=kb_prepayment_back)
    else:
        camunal = message.text

        await state.update_data(var_camunal=camunal)
        await message.answer(f"Введите срок на который сдается квартира", reply_markup=kb_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q41  -->  Введите срок на который сдается квартира
@dp.message_handler(state=RentApartmentState.Q41)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q40.set()
        await message.answer(f"Входят ли коммунальные услуги в стоимость", reply_markup=kb_yes_or_no_back)
    else:
        apartment_completion = message.text

        await state.update_data(var_apartment_completion=apartment_completion)
        await message.answer(f"Эксклюзив ?", reply_markup=kb_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q42  -->  Эксклюзив ?
@dp.message_handler(state=RentApartmentState.Q42)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q41.set()
        await message.answer(f"Введите срок на который сдается квартира", reply_markup=kb_back)
    else:
        exclusive = message.text

        await state.update_data(var_exclusive=exclusive)
        await message.answer(f"Напишите полное описание квартиры", reply_markup=kb_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q43  -->  Напишите полное описание квартиры
@dp.message_handler(state=RentApartmentState.Q43)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q42.set()
        await message.answer(f"Эксклюзив ?", reply_markup=kb_yes_or_no_back)
    else:
        description = message.text

        await state.update_data(var_description=description)
        await message.answer(f"Рекламировать на торговых площадках ?", reply_markup=kb_yes_or_no_back)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q44  -->  Рекламировать на торговых площадках ?
@dp.message_handler(state=RentApartmentState.Q44)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await RentApartmentState.Q43.set()
        await message.answer(f"Напишите полное описание квартиры", reply_markup=kb_back)
    else:
        public = message.text

        await state.update_data(var_public=public)
        await message.answer(f"Все заполнил(-а) правильно ?", reply_markup=kb_yes_or_no)
        await RentApartmentState.next()


# Состояние RentApartmentState.Q45  -->  Все заполнил(-а) правильно ?
@dp.message_handler(state=RentApartmentState.Q45)
async def select_district(message: types.Message, state=FSMContext):
    filled_in_correctly = message.text
    answer = await state.get_data()

    if filled_in_correctly.lower() == 'да':
        answer = await state.get_data()
        await state.reset_state()
        await message.answer('Ваша объективка отправлена)', reply_markup=kb_main_menu)
        GoogleWork().google_add_row(sheet_id='1-B80joNKTOSTIJRLiACOcfH1E3dH5yrNPbS-CU5Bvxc',
                                    name_list='Аренда квартиры',
                                    array_data=[
                                        answer['var_type_of_property'],
                                        answer['var_district'],
                                        answer['var_quarter'],
                                        answer['var_reference_point'],
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
                                        answer['var_furniture'],
                                        answer['var_technics'],
                                        answer['var_condition'],
                                        answer['var_tenant_description'],
                                        answer['var_apartment_completion'],
                                        answer['var_month_price'],
                                        answer['var_deposit'],
                                        answer['var_prepayment'],
                                        answer['var_apartment_completion'],
                                        answer['var_camunal'],
                                        answer['var_owner'],
                                        answer['var_number_phone'],
                                        answer['var_additional_number_phone'],
                                        '0',
                                        answer['var_ceiling_height'],
                                        answer['var_kitchen_area'],
                                        answer['var_plastic_windows'],
                                        answer['var_location_the_road'],
                                        answer['var_distance_to_metro'],
                                        answer['var_number_home'],
                                        answer['var_number_apartment'],
                                        '0',
                                        '0',
                                        '0',
                                        '0',
                                        message.from_user.full_name,
                                        str(date.today()),
                                        str(date.today()),
                                        answer['var_informant'],
                                        answer['var_infrastructures'],
                                        answer['var_redevelopment'],
                                        answer['var_type_parking'],
                                        answer['var_entrance'],
                                        answer['var_elevator_condition'],
                                        answer['var_roof_condition'],
                                        answer['var_neighbors_description'],
                                        answer['var_exclusive']
                                    ])
    elif filled_in_correctly.lower() == 'нет':
        await state.reset_state()
        await message.answer('Вы отменили отправку', reply_markup=kb_main_menu)
    else:
        await message.answer('Отправлено не верное значение( Попробуйте снова')
