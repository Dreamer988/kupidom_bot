import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from filters.is_date import IsDate
from filters.is_digit import IsDigit
from filters.is_phone import IsPhone
from filters.verifi_phone_to_db import VerificationPhoneToDB
from filters.verifi_sector_to_db import VerificationSectorToDB
from filters.verifi_telegram_id_to_db import VerificationTelegramIdToDB
from keyboards.default.send_by_apartment import kb_yes_or_no
from keyboards.default.system import kb_users_rang, kb_users_type_of_property
from loader import dp
from sql.sql_query import SqlQuery
from states import SystemState


@dp.message_handler(Text(equals='Агент'), state=SystemState.UserAdd)
async def get_first_name(message: types.Message):
    await message.answer('🔴🔴🔴 Внимание.\nВсе данные заполняються на кириллице')
    await message.answer('Укажите имя', reply_markup=ReplyKeyboardRemove())
    await SystemState.UserAddAgent_Q1.set()


@dp.message_handler(state=SystemState.UserAddAgent_Q1)
async def get_last_name(message: types.Message, state=FSMContext):
    first_name = message.text.strip().lower()
    await state.update_data(var_first_name=first_name)

    await message.answer('Укажите фамилию', reply_markup=ReplyKeyboardRemove())
    await SystemState.UserAddAgent_Q2.set()


@dp.message_handler(state=SystemState.UserAddAgent_Q2)
async def get_patronymic(message: types.Message, state=FSMContext):
    last_name = message.text.strip().lower()
    await state.update_data(var_last_name=last_name)

    await message.answer('Укажите отчество', reply_markup=ReplyKeyboardRemove())
    await SystemState.UserAddAgent_Q3.set()


@dp.message_handler(state=SystemState.UserAddAgent_Q3)
async def get_date(message: types.Message, state=FSMContext):
    patronymic = message.text.strip().lower()
    await state.update_data(var_patronymic=patronymic)

    await message.answer('Укажите дату рождения в формате (ГГГГ-ММ-ДД)', reply_markup=ReplyKeyboardRemove())
    await SystemState.UserAddAgent_Q4.set()


@dp.message_handler(IsDate(), state=SystemState.UserAddAgent_Q4)
async def get_residence_area(message: types.Message, state=FSMContext):
    date = message.text.strip()
    await state.update_data(var_date=date)
    await message.answer('Укажите место проживания в формате (г.Ташкент, Сергелийский район, Сергели 7)',
                         reply_markup=ReplyKeyboardRemove())
    await SystemState.UserAddAgent_Q5.set()


@dp.message_handler(state=SystemState.UserAddAgent_Q5)
async def get_phone_number(message: types.Message, state=FSMContext):
    residence_area = message.text.strip().lower()
    await state.update_data(var_residence_area=residence_area)

    await message.answer('Укажите номер телефона (который выдала ему компания)', reply_markup=ReplyKeyboardRemove())
    await SystemState.UserAddAgent_Q6.set()


@dp.message_handler(IsPhone(), VerificationPhoneToDB(), state=SystemState.UserAddAgent_Q6)
async def get_telegram_id(message: types.Message, state=FSMContext):
    phone_number = message.text.strip()
    # Получаем с помощью регулярного выражения только числа
    decor_number = re.findall(r'\d+', phone_number)
    # Получаем 9 чисел с правой стороны
    decor_number = int(''.join(decor_number)[-9:])
    # Добавляем код страны 998
    decor_number = '998' + str(decor_number)

    await state.update_data(var_phone_number=decor_number)

    await message.answer('Укажите id телеграмма сотрудника', reply_markup=ReplyKeyboardRemove())
    await SystemState.UserAddAgent_Q7.set()


@dp.message_handler(IsDigit(), VerificationTelegramIdToDB(), state=SystemState.UserAddAgent_Q7)
async def get_type_of_property(message: types.Message, state=FSMContext):
    telegram_id = message.text.strip()

    await state.update_data(var_telegram_id=telegram_id)

    await message.answer('Выберите вид недвижимости', reply_markup=kb_users_type_of_property)
    await SystemState.UserAddAgent_Q8.set()


@dp.message_handler(state=SystemState.UserAddAgent_Q8)
async def get_rang(message: types.Message, state=FSMContext):
    type_of_property = message.text.strip().lower()

    await state.update_data(var_type_of_property=type_of_property)

    await message.answer('Выберите ранг сотрудника', reply_markup=kb_users_rang)
    await SystemState.UserAddAgent_Q9.set()


@dp.message_handler(state=SystemState.UserAddAgent_Q9)
async def get_sector(message: types.Message, state=FSMContext):
    rang = message.text.strip().lower()

    await state.update_data(var_rang=rang)

    await message.answer('Выберите участок за каторый отвечает сотрудник\n(Например: 1, 2, 3)\n'
                         'Участок должен быть только один!', reply_markup=ReplyKeyboardRemove())
    print(state.get_data())
    await SystemState.UserAddAgent_Q10.set()


@dp.message_handler(IsDigit(), VerificationSectorToDB(), state=SystemState.UserAddAgent_Q10)
async def verification(message: types.Message, state=FSMContext):
    sector = message.text.strip()
    await state.update_data(var_sector=sector)

    values = await state.get_data()

    await message.answer('🔴🔴🔴 ВНИМАТЕЛЬНО ПРОВЕРЬТЕ')
    await message.answer(f'Имя:  <code>{values["var_first_name"].title()}</code>\n'
                         f'Фамилия:  <code>{values["var_last_name"].title()}</code>\n'
                         f'Отчество:  <code>{values["var_patronymic"].title()}</code>\n'
                         f'Дата рождения:  <code>{values["var_date"]}</code>\n'
                         f'Место проживания:  <code>{values["var_residence_area"]}</code>\n'
                         f'Номер телефона:  <code>{values["var_phone_number"]}</code>\n'
                         f'Телеграм ID:  <code>{values["var_telegram_id"]}</code>\n'
                         f'Недвижимость:  <code>{values["var_type_of_property"].title()}</code>\n'
                         f'Ранг:  <code>{values["var_rang"].title()}</code>\n'
                         f'Участок:  <code>{values["var_sector"]}</code>\n')

    await message.answer('Вы все заполнили правильно?', reply_markup=kb_yes_or_no)
    await SystemState.UserAddAgent_Q11.set()


@dp.message_handler(state=SystemState.UserAddAgent_Q11)
async def send_agent_db(message: types.Message, state=FSMContext):
    if message.text.lower() == 'да':
        values = await state.get_data()
        SqlQuery().add_row(table_name='agents',
                           keys=[
                               'telegram_id',
                               'first_name',
                               'last_name',
                               'patronymic',
                               'date',
                               'phone',
                               'residence_area',
                               'type_of_property',
                               'class',
                               'sector'
                           ],
                           values=(
                               f'{values["var_telegram_id"]}',
                               f'{values["var_first_name"]}',
                               f'{values["var_last_name"]}',
                               f'{values["var_patronymic"]}',
                               f'{values["var_date"]}',
                               f'{values["var_phone_number"]}',
                               f'{values["var_residence_area"]}',
                               f'{values["var_type_of_property"]}',
                               f'{values["var_rang"]}',
                               f'{values["var_sector"]}',
                           ))
        SqlQuery().add_row(table_name='bot_timer',
                           keys=[
                               'telegram_id',
                               'count_day',
                               'count_hours',
                               'day',
                               'hour'
                           ],
                           values=(
                               f'{values["var_telegram_id"]}',
                               0,
                               0,
                               0,
                               0
                           ))
        await message.answer('Пользователь добавлен в базу данных')
        await message.answer('Мы перенаправили вас в Главное Меню\nПожалуйста введите пароль чтобы продолжить ...')
        await SystemState.Start.set()

    elif message.text.lower() == 'нет':
        await state.reset_data()
        await message.answer('Вы отменили добавление пользователя', reply_markup=ReplyKeyboardRemove())
        await message.answer(
            'Мы перенаправили вас в Главное Меню\nПожалуйста введите <b>пароль</b> чтобы продолжить ...')
        await SystemState.Start.set()
    else:
        await message.answer('Вы ввели не верное значение! Попробуйте снова')
