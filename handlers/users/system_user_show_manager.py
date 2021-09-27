import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from filters.is_phone import IsPhone
from keyboards.default.delete_object import kb_yes_or_no
from loader import dp
from sql.sql_query import SqlQuery
from states import SystemState


def array(values):
    result = []
    for value in values:
        result.append(value[0])
    return result


@dp.message_handler(Text(equals='Менеджеров'), state=SystemState.UserShow)
async def get_first_name(message: types.Message):
    await message.answer('Хотите просмотреть список всех менеджеров ?', reply_markup=kb_yes_or_no)
    await SystemState.UserShowManager_Select.set()


@dp.message_handler(Text(equals='Да'), state=SystemState.UserShowManager_Select)
async def get_first_name(message: types.Message):
    await message.answer('Понял, сейчас отправлю вам полный список !', reply_markup=kb_yes_or_no)
    managers_telegram_id = array(SqlQuery().get_column(
        table_name='managers',
        get_column_name='telegram_id'))
    managers_first_name = array(SqlQuery().get_column(
        table_name='managers',
        get_column_name='first_name'))
    managers_last_name = array(SqlQuery().get_column(
        table_name='managers',
        get_column_name='last_name'))
    managers_patronymic = array(SqlQuery().get_column(
        table_name='managers',
        get_column_name='patronymic'))
    managers_number_phone = array(SqlQuery().get_column(
        table_name='managers',
        get_column_name='phone'))
    all_managers_param = '   Telegram ID   |   Ф.И.О   |   Номер телефона   \n\n'
    for num in range(len(managers_telegram_id)):
        value = f"{num + 1}.  <code>{managers_telegram_id[num]}</code> | " \
                f"<i>{managers_last_name[num].title()}</i>  " \
                f"<i>{managers_first_name[num].title()}</i>  " \
                f"<i>{managers_patronymic[num].title()}</i> | " \
                f"{managers_number_phone[num]} \n\n"
        all_managers_param = all_managers_param + value

    await message.answer(all_managers_param)
    await message.answer('Данные пользователей отправлены, пожалуйста введите <b>пароль</b> чтобы продолжить',
                         reply_markup=ReplyKeyboardRemove())

    await SystemState.Start.set()


@dp.message_handler(Text(equals='Нет'), state=SystemState.UserShowManager_Select)
async def get_first_name(message: types.Message):
    await message.answer('Понял, тогда мне нужен номер телефона пользователя', reply_markup=ReplyKeyboardRemove())
    await SystemState.UserShowManager_CurrentUser.set()


@dp.message_handler(IsPhone(), state=SystemState.UserShowManager_CurrentUser)
async def get_first_name(message: types.Message, state=FSMContext):
    number_object = message.text
    # Получаем с помощью регулярного выражения только числа
    decor_number = re.findall(r'\d+', number_object)
    # Получаем 9 чисел с правой стороны
    decor_number = int(''.join(decor_number)[-9:])
    # Добавляем код страны (988)
    decor_number = f'998{decor_number}'

    search_phone_to_db = SqlQuery().get_row(table_name='managers',
                                            search_param=[
                                                f"phone = '{decor_number}'"
                                            ])
    if search_phone_to_db:
        search_phone_to_db = search_phone_to_db[0]
        await message.answer('Вот информация на запрашиваемого вами агента:')
        print(search_phone_to_db)
        await message.answer(f'Имя:  <code>{search_phone_to_db[2].title()}</code>\n'
                             f'Фамилия:  <code>{search_phone_to_db[3].title()}</code>\n'
                             f'Отчество:  <code>{search_phone_to_db[4].title()}</code>\n'
                             f'Дата рождения:  <code>{search_phone_to_db[5]}</code>\n'
                             f'Место проживания:  <code>{search_phone_to_db[8]}</code>\n'
                             f'Номер телефона:  <code>{search_phone_to_db[6]}</code>\n'
                             f'Телеграм ID:  <code>{search_phone_to_db[1]}</code>\n'
                             f'Должность:  <code>{search_phone_to_db[7].title()}</code>\n')
        await message.answer('Данные пользователя отправлены, пожалуйста введите <b>пароль</b> чтобы продолжить',
                             reply_markup=ReplyKeyboardRemove())

        await SystemState.Start.set()
    else:
        await message.answer('Пользователя с таким номером телефона не существует в базе данных')
