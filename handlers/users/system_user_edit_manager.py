import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from filters.is_date import IsDate
from filters.is_phone import IsPhone
from filters.verifi_phone_to_db import VerificationPhoneToDB
from filters.verifi_telegram_id_to_db import VerificationTelegramIdToDB
from keyboards.default.send_by_apartment import kb_yes_or_no
from keyboards.default.system import kb_users_edit_exit, kb_users_edit_manager_menu
from loader import dp
from sql.sql_query import SqlQuery
from states import SystemState


@dp.message_handler(Text(equals='Менеджер'), state=SystemState.UserEdit)
async def start_edit_agent(message: types.Message):
    await message.answer('🔴🔴🔴 Внимание.\nВсе данные заполняються на кириллице')
    await message.answer('Введите номер телефона пользователя \nу которого вы хотите изменить персональные данные.',
                         reply_markup=ReplyKeyboardRemove())
    await SystemState.UserEditManager.set()


@dp.message_handler(IsPhone(), state=SystemState.UserEditManager)
async def search_by_number(message: types.Message, state=FSMContext):
    phone_number = message.text.strip()
    # Получаем с помощью регулярного выражения только числа
    decor_number = re.findall(r'\d+', phone_number)
    # Получаем 9 чисел с правой стороны
    decor_number = int(''.join(decor_number)[-9:])
    # Добавляем код страны 998
    decor_number = '998' + str(decor_number)

    search_phone_to_db = SqlQuery().get_row(table_name='managers',
                                            search_param=[
                                                f"phone = '{decor_number}'"
                                            ])

    if search_phone_to_db:
        search_phone_to_db = search_phone_to_db[0]
        await state.update_data(db_value=search_phone_to_db)
        await message.answer(f'Данные пользователя по этому номеру телефона:  <b>{decor_number}</b>')

        await message.answer(f'Имя:  <code>{search_phone_to_db[2].title()}</code>\n'
                             f'Фамилия:  <code>{search_phone_to_db[3].title()}</code>\n'
                             f'Отчество:  <code>{search_phone_to_db[4].title()}</code>\n'
                             f'Дата рождения:  <code>{search_phone_to_db[5]}</code>\n'
                             f'Место проживания:  <code>{search_phone_to_db[8]}</code>\n'
                             f'Номер телефона:  <code>{search_phone_to_db[6]}</code>\n'
                             f'Телеграм ID:  <code>{search_phone_to_db[1]}</code>\n')

        await message.answer('Выберите параметр который надо изменить\n'
                             'Или нажмите на команду /system чтобы перейти в главное меню',
                             reply_markup=kb_users_edit_manager_menu)

        await SystemState.UserEditManager_EditParam.set()
    else:
        await message.answer(f'Данного номера: <b>{decor_number}</b> нету в базе данных')
        await message.answer(f'<b>Введите другой номер телефона</b>\n'
                             f'Или перейдите в главное меню нажав на команду /system')


# Edit First Name
@dp.message_handler(Text(equals='Имя'), state=SystemState.UserEditManager_EditParam)
async def edit_first_name(message: types.Message, state=FSMContext):
    await message.answer('Введите имя')
    await SystemState.UserEditManager_FirstName_Q1.set()


@dp.message_handler(state=SystemState.UserEditManager_FirstName_Q1)
async def edit_first_name(message: types.Message, state=FSMContext):
    first_name = message.text.strip().lower()
    await state.update_data(edit_first_name=first_name)
    value = await state.get_data()
    db_values = value['db_value']
    await message.answer(f'Вы хотите изменить имя с <b>{db_values[2].title()}</b> на <b>{first_name.title()}</b>?',
                         reply_markup=kb_yes_or_no)
    await SystemState.UserEditManager_FirstName_Q2.set()


@dp.message_handler(state=SystemState.UserEditManager_FirstName_Q2)
async def edit_first_name(message: types.Message, state=FSMContext):
    values = await state.get_data()
    db_values = values['db_value']
    first_name = values['edit_first_name']
    if message.text.strip().lower() == 'да':
        SqlQuery().edit_row(table_name='managers',
                            search_column_name='phone',
                            search_value=db_values[6],
                            edit_param=[
                                f"`first_name` = '{first_name}'"
                            ])
        await message.answer('Имя изменено')
        await message.answer('Вы можете продолжить изменения\nнажав на кнопку <b>Изменить ещё</b>\n'
                             'Либо перейти в <b>Главное Меню</b>', reply_markup=kb_users_edit_exit)
        await SystemState.UserEditExit.set()
    elif message.text.strip().lower() == 'нет':
        await message.answer('Вы отменили изменение')
        await message.answer('Вы можете измененить другие параметры\nнажав на кнопку <b>Изменить ещё</b>\n'
                             'Либо перейти в <b>Главное Меню</b>', reply_markup=kb_users_edit_exit)
        await SystemState.UserEditExit.set()
    else:
        await message.answer('Вы ввели не верное значение!\nПожалуйста попробуйте снова.')


# Edit Last Name
@dp.message_handler(Text(equals='Фамилия'), state=SystemState.UserEditManager_EditParam)
async def edit_last_name(message: types.Message, state=FSMContext):
    await message.answer('Введите фамилию')
    await SystemState.UserEditManager_LastName_Q1.set()


@dp.message_handler(state=SystemState.UserEditManager_LastName_Q1)
async def edit_last_name(message: types.Message, state=FSMContext):
    first_name = message.text.strip().lower()
    await state.update_data(edit_last_name=first_name)
    value = await state.get_data()
    db_values = value['db_value']
    await message.answer(f'Вы хотите изменить фамилию с <b>{db_values[3].title()}</b> на <b>{first_name.title()}</b>?',
                         reply_markup=kb_yes_or_no)
    await SystemState.UserEditManager_LastName_Q2.set()


@dp.message_handler(state=SystemState.UserEditManager_LastName_Q2)
async def edit_last_name(message: types.Message, state=FSMContext):
    values = await state.get_data()
    db_values = values['db_value']
    last_name = values['edit_last_name']
    if message.text.strip().lower() == 'да':
        SqlQuery().edit_row(table_name='managers',
                            search_column_name='phone',
                            search_value=db_values[6],
                            edit_param=[
                                f"`last_name` = '{last_name}'"
                            ])
        await message.answer('Фамилия изменена')
        await message.answer('Вы можете продолжить изменения\nнажав на кнопку <b>Изменить ещё</b>\n'
                             'Либо перейти в <b>Главное Меню</b>', reply_markup=kb_users_edit_exit)
        await SystemState.UserEditExit.set()
    elif message.text.strip().lower() == 'нет':
        await message.answer('Вы отменили изменение')
        await message.answer('Вы можете измененить другие параметры\nнажав на кнопку <b>Изменить ещё</b>\n'
                             'Либо перейти в <b>Главное Меню</b>', reply_markup=kb_users_edit_exit)
        await SystemState.UserEditExit.set()
    else:
        await message.answer('Вы ввели не верное значение!\nПожалуйста попробуйте снова.')


# Edit Patronymic
@dp.message_handler(Text(equals='Отчество'), state=SystemState.UserEditManager_EditParam)
async def edit_patronymic(message: types.Message, state=FSMContext):
    await message.answer('Введите отчество')
    await SystemState.UserEditManager_Patronymic_Q1.set()


@dp.message_handler(state=SystemState.UserEditManager_Patronymic_Q1)
async def edit_patronymic(message: types.Message, state=FSMContext):
    patronymic = message.text.strip().lower()
    await state.update_data(edit_patronymic=patronymic)
    value = await state.get_data()
    db_values = value['db_value']
    await message.answer(f'Вы хотите изменить отчество с <b>{db_values[4].title()}</b> на <b>{patronymic.title()}</b>?',
                         reply_markup=kb_yes_or_no)
    await SystemState.UserEditManager_Patronymic_Q2.set()


@dp.message_handler(state=SystemState.UserEditManager_Patronymic_Q2)
async def edit_patronymic(message: types.Message, state=FSMContext):
    values = await state.get_data()
    db_values = values['db_value']
    patronymic = values['edit_patronymic']
    if message.text.strip().lower() == 'да':
        SqlQuery().edit_row(table_name='managers',
                            search_column_name='phone',
                            search_value=db_values[6],
                            edit_param=[
                                f"`patronymic` = '{patronymic}'"
                            ])
        await message.answer('Отчество изменено')
        await message.answer('Вы можете продолжить изменения\nнажав на кнопку <b>Изменить ещё</b>\n'
                             'Либо перейти в <b>Главное Меню</b>', reply_markup=kb_users_edit_exit)
        await SystemState.UserEditExit.set()
    elif message.text.strip().lower() == 'нет':
        await message.answer('Вы отменили изменение')
        await message.answer('Вы можете измененить другие параметры\nнажав на кнопку <b>Изменить ещё</b>\n'
                             'Либо перейти в <b>Главное Меню</b>', reply_markup=kb_users_edit_exit)
        await SystemState.UserEditExit.set()
    else:
        await message.answer('Вы ввели не верное значение!\nПожалуйста попробуйте снова.')


# Edit Date
@dp.message_handler(Text(equals='Дата рождения'), state=SystemState.UserEditManager_EditParam)
async def edit_date(message: types.Message, state=FSMContext):
    await message.answer('Введите дату в формате (ГГГГ-ММ-ДД)')
    await SystemState.UserEditManager_Date_Q1.set()


@dp.message_handler(IsDate(), state=SystemState.UserEditManager_Date_Q1)
async def edit_date(message: types.Message, state=FSMContext):
    date = message.text.strip().lower()
    await state.update_data(edit_date=date)
    value = await state.get_data()
    db_values = value['db_value']
    await message.answer(f'Вы хотите изменить дату с <b>{db_values[5]}</b> на <b>{date}</b>?',
                         reply_markup=kb_yes_or_no)
    await SystemState.UserEditManager_Date_Q2.set()


@dp.message_handler(state=SystemState.UserEditManager_Date_Q2)
async def edit_date(message: types.Message, state=FSMContext):
    values = await state.get_data()
    db_values = values['db_value']
    date = values['edit_date']
    if message.text.strip().lower() == 'да':
        SqlQuery().edit_row(table_name='managers',
                            search_column_name='phone',
                            search_value=db_values[6],
                            edit_param=[
                                f"`date` = '{date}'"
                            ])
        await message.answer('Дата изменена')
        await message.answer('Вы можете продолжить изменения\nнажав на кнопку <b>Изменить ещё</b>\n'
                             'Либо перейти в <b>Главное Меню</b>', reply_markup=kb_users_edit_exit)
        await SystemState.UserEditExit.set()
    elif message.text.strip().lower() == 'нет':
        await message.answer('Вы отменили изменение')
        await message.answer('Вы можете измененить другие параметры\nнажав на кнопку <b>Изменить ещё</b>\n'
                             'Либо перейти в <b>Главное Меню</b>', reply_markup=kb_users_edit_exit)
        await SystemState.UserEditExit.set()
    else:
        await message.answer('Вы ввели не верное значение!\nПожалуйста попробуйте снова.')


# Edit Residence Area
@dp.message_handler(Text(equals='Место проживания'), state=SystemState.UserEditManager_EditParam)
async def edit_residence_area(message: types.Message, state=FSMContext):
    await message.answer('Введите место проживания в формате (г.Ташкент, Сергелийский район, Сергели 7)')
    await SystemState.UserEditManager_ResidenceArea_Q1.set()


@dp.message_handler(state=SystemState.UserEditManager_ResidenceArea_Q1)
async def edit_residence_area(message: types.Message, state=FSMContext):
    residence_area = message.text.strip().lower()
    await state.update_data(edit_residence_area=residence_area)
    value = await state.get_data()
    db_values = value['db_value']
    await message.answer(f'Вы хотите изменить место проживания с <b>{db_values[7]}</b> на <b>{residence_area}</b>?',
                         reply_markup=kb_yes_or_no)
    await SystemState.UserEditManager_ResidenceArea_Q2.set()


@dp.message_handler(state=SystemState.UserEditManager_ResidenceArea_Q2)
async def edit_residence_area(message: types.Message, state=FSMContext):
    values = await state.get_data()
    db_values = values['db_value']
    residence_area = values['edit_residence_area']
    if message.text.strip().lower() == 'да':
        SqlQuery().edit_row(table_name='managers',
                            search_column_name='phone',
                            search_value=db_values[6],
                            edit_param=[
                                f"`residence_area` = '{residence_area}'"
                            ])
        await message.answer('Место проживания изменено')
        await message.answer('Вы можете продолжить изменения\nнажав на кнопку <b>Изменить ещё</b>\n'
                             'Либо перейти в <b>Главное Меню</b>', reply_markup=kb_users_edit_exit)
        await SystemState.UserEditExit.set()
    elif message.text.strip().lower() == 'нет':
        await message.answer('Вы отменили изменение')
        await message.answer('Вы можете измененить другие параметры\nнажав на кнопку <b>Изменить ещё</b>\n'
                             'Либо перейти в <b>Главное Меню</b>', reply_markup=kb_users_edit_exit)
        await SystemState.UserEditExit.set()
    else:
        await message.answer('Вы ввели не верное значение!\nПожалуйста попробуйте снова.')


# Edit Phone
@dp.message_handler(Text(equals='Номер телефона'), state=SystemState.UserEditManager_EditParam)
async def edit_phone(message: types.Message, state=FSMContext):
    await message.answer('Введите номер телефона')
    await SystemState.UserEditManager_Phone_Q1.set()


@dp.message_handler(VerificationPhoneToDB(), state=SystemState.UserEditManager_Phone_Q1)
async def edit_phone(message: types.Message, state=FSMContext):
    phone_number = message.text.strip()
    # Получаем с помощью регулярного выражения только числа
    decor_number = re.findall(r'\d+', phone_number)
    # Получаем 9 чисел с правой стороны
    decor_number = int(''.join(decor_number)[-9:])
    # Добавляем код страны 998
    decor_number = '998' + str(decor_number)

    await state.update_data(edit_phone=decor_number)
    value = await state.get_data()
    db_values = value['db_value']
    await message.answer(f'Вы хотите изменить номер телефона с <b>{db_values[6]}</b> на <b>{decor_number}</b>?',
                         reply_markup=kb_yes_or_no)
    await SystemState.UserEditManager_Phone_Q2.set()


@dp.message_handler(state=SystemState.UserEditManager_Phone_Q2)
async def edit_phone(message: types.Message, state=FSMContext):
    values = await state.get_data()
    db_values = values['db_value']
    decor_number = values['edit_phone']
    if message.text.strip().lower() == 'да':
        SqlQuery().edit_row(table_name='managers',
                            search_column_name='phone',
                            search_value=db_values[6],
                            edit_param=[
                                f"`phone` = '{decor_number}'"
                            ])
        await message.answer('Номер телефона изменен')
        await message.answer('Вы можете продолжить изменения\nнажав на кнопку <b>Изменить ещё</b>\n'
                             'Либо перейти в <b>Главное Меню</b>', reply_markup=kb_users_edit_exit)
        await SystemState.UserEditExit.set()
    elif message.text.strip().lower() == 'нет':
        await message.answer('Вы отменили изменение')
        await message.answer('Вы можете измененить другие параметры\nнажав на кнопку <b>Изменить ещё</b>\n'
                             'Либо перейти в <b>Главное Меню</b>', reply_markup=kb_users_edit_exit)
        await SystemState.UserEditExit.set()
    else:
        await message.answer('Вы ввели не верное значение!\nПожалуйста попробуйте снова.')


# Edit Telegram ID
@dp.message_handler(Text(equals='Телеграм ID'), state=SystemState.UserEditManager_EditParam)
async def edit_telegram_id(message: types.Message, state=FSMContext):
    await message.answer('Введите телеграм ID')
    await SystemState.UserEditManager_TelegramID_Q1.set()


@dp.message_handler(VerificationTelegramIdToDB(), state=SystemState.UserEditManager_TelegramID_Q1)
async def edit_telegram_id(message: types.Message, state=FSMContext):
    telegram_id = message.text.strip()

    await state.update_data(edit_telegram_id=telegram_id)
    value = await state.get_data()
    db_values = value['db_value']
    await message.answer(f'Вы хотите изменить телеграм ID с <b>{db_values[1]}</b> на <b>{telegram_id}</b>?',
                         reply_markup=kb_yes_or_no)
    await SystemState.UserEditManager_TelegramID_Q2.set()


@dp.message_handler(state=SystemState.UserEditManager_TelegramID_Q2)
async def edit_telegram_id(message: types.Message, state=FSMContext):
    values = await state.get_data()
    db_values = values['db_value']
    telegram_id = values['edit_telegram_id']
    if message.text.strip().lower() == 'да':
        SqlQuery().edit_row(table_name='managers',
                            search_column_name='phone',
                            search_value=db_values[6],
                            edit_param=[
                                f"`telegram_id` = '{telegram_id}'"
                            ])
        await message.answer('Телеграм ID изменен')
        await message.answer('Вы можете продолжить изменения\nнажав на кнопку <b>Изменить ещё</b>\n'
                             'Либо перейти в <b>Главное Меню</b>', reply_markup=kb_users_edit_exit)
        await SystemState.UserEditExit.set()
    elif message.text.strip().lower() == 'нет':
        await message.answer('Вы отменили изменение')
        await message.answer('Вы можете измененить другие параметры\nнажав на кнопку <b>Изменить ещё</b>\n'
                             'Либо перейти в <b>Главное Меню</b>', reply_markup=kb_users_edit_exit)
        await SystemState.UserEditExit.set()
    else:
        await message.answer('Вы ввели не верное значение!\nПожалуйста попробуйте снова.')


# Edit Exit
@dp.message_handler(Text(equals='Главное меню'), state=SystemState.UserEditExit)
async def exit_edit_agent(message: types.Message):
    await message.answer('Пожалуйста введите <b>пароль</b> чтобы продолжить ...')
    await SystemState.Start.set()


@dp.message_handler(Text(equals='Изменить ещё'), state=SystemState.UserEditExit)
async def exit_edit_agent(message: types.Message):
    await message.answer('🔴🔴🔴 Внимание.\nВсе данные заполняються на кириллице')
    await message.answer('Введите номер телефона пользователя \nу которого вы хотите изменить персональные данные.',
                         reply_markup=ReplyKeyboardRemove())
    await SystemState.UserEditAgent.set()
