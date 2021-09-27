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


@dp.message_handler(Text(equals='Менеджер'), state=SystemState.UserAdd)
async def get_first_name(message: types.Message):
    await message.answer('🔴🔴🔴 Внимание.\nВсе данные заполняються на кириллице')
    await message.answer('Укажите имя', reply_markup=ReplyKeyboardRemove())
    await SystemState.UserAddManager_Q1.set()


@dp.message_handler(state=SystemState.UserAddManager_Q1)
async def get_last_name(message: types.Message, state=FSMContext):
    first_name = message.text.strip().lower()
    await state.update_data(var_first_name=first_name)

    await message.answer('Укажите фамилию', reply_markup=ReplyKeyboardRemove())
    await SystemState.UserAddManager_Q2.set()


@dp.message_handler(state=SystemState.UserAddManager_Q2)
async def get_patronymic(message: types.Message, state=FSMContext):
    last_name = message.text.strip().lower()
    await state.update_data(var_last_name=last_name)

    await message.answer('Укажите отчество', reply_markup=ReplyKeyboardRemove())
    await SystemState.UserAddManager_Q3.set()


@dp.message_handler(state=SystemState.UserAddManager_Q3)
async def get_date(message: types.Message, state=FSMContext):
    patronymic = message.text.strip().lower()
    await state.update_data(var_patronymic=patronymic)

    await message.answer('Укажите дату рождения в формате (ГГГГ-ММ-ДД)', reply_markup=ReplyKeyboardRemove())
    await SystemState.UserAddManager_Q4.set()


@dp.message_handler(IsDate(), state=SystemState.UserAddManager_Q4)
async def get_residence_area(message: types.Message, state=FSMContext):
    date = message.text.strip()
    await state.update_data(var_date=date)
    await message.answer('Укажите место проживания в формате (г.Ташкент, Сергелийский район, Сергели 7)',
                         reply_markup=ReplyKeyboardRemove())
    await SystemState.UserAddManager_Q5.set()


@dp.message_handler(state=SystemState.UserAddManager_Q5)
async def get_phone_number(message: types.Message, state=FSMContext):
    residence_area = message.text.strip().lower()
    await state.update_data(var_residence_area=residence_area)

    await message.answer('Укажите номер телефона (который выдала ему компания)', reply_markup=ReplyKeyboardRemove())
    await SystemState.UserAddManager_Q6.set()


@dp.message_handler(IsPhone(), VerificationPhoneToDB(), state=SystemState.UserAddManager_Q6)
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
    await SystemState.UserAddManager_Q7.set()


@dp.message_handler(IsDigit(), VerificationTelegramIdToDB(), state=SystemState.UserAddManager_Q7)
async def get_type_of_property(message: types.Message, state=FSMContext):
    telegram_id = message.text.strip()

    await state.update_data(var_telegram_id=telegram_id)
    values = await state.get_data()

    await message.answer('🔴🔴🔴 ВНИМАТЕЛЬНО ПРОВЕРЬТЕ')
    await message.answer(f'Имя:  <code>{values["var_first_name"].title()}</code>\n'
                         f'Фамилия:  <code>{values["var_last_name"].title()}</code>\n'
                         f'Отчество:  <code>{values["var_patronymic"].title()}</code>\n'
                         f'Дата рождения:  <code>{values["var_date"]}</code>\n'
                         f'Место проживания:  <code>{values["var_residence_area"]}</code>\n'
                         f'Номер телефона:  <code>{values["var_phone_number"]}</code>\n'
                         f'Телеграм ID:  <code>{values["var_telegram_id"]}</code>\n')

    await message.answer('Вы все заполнили правильно?', reply_markup=kb_yes_or_no)
    await SystemState.UserAddManager_Q8.set()


@dp.message_handler(state=SystemState.UserAddManager_Q8)
async def send_manager_db(message: types.Message, state=FSMContext):
    if message.text.lower() == 'да':
        values = await state.get_data()
        SqlQuery().add_row(table_name='managers',
                           keys=[
                               'telegram_id',
                               'first_name',
                               'last_name',
                               'patronymic',
                               'date',
                               'phone',
                               'position',
                               'residence_area',
                           ],
                           values=(
                               f'{values["var_telegram_id"]}',
                               f'{values["var_first_name"]}',
                               f'{values["var_last_name"]}',
                               f'{values["var_patronymic"]}',
                               f'{values["var_date"]}',
                               f'{values["var_phone_number"]}',
                               f'manager',
                               f'{values["var_residence_area"]}',
                           ))
        await message.answer('Пользователь добавлен в базу данных')
        await message.answer(
            'Мы перенаправили вас в Главное Меню\nПожалуйста введите <b>пароль</b> чтобы продолжить ...')
        await SystemState.Start.set()

    elif message.text.lower() == 'нет':
        await state.reset_data()
        await message.answer('Вы отменили добавление пользователя', reply_markup=ReplyKeyboardRemove())
        await message.answer(
            'Мы перенаправили вас в Главное Меню\nПожалуйста введите <b>пароль</b> чтобы продолжить ...')
        await SystemState.Start.set()
    else:
        await message.answer('Вы ввели не верное значение! Попробуйте снова')
