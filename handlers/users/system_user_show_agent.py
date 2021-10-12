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


@dp.message_handler(Text(equals='Агентов'), state=SystemState.UserShow)
async def get_first_name(message: types.Message):
    await message.answer('Хотите просмотреть список всех агентов ?', reply_markup=kb_yes_or_no)
    await SystemState.UserShowAgent_Select.set()


@dp.message_handler(Text(equals='Да'), state=SystemState.UserShowAgent_Select)
async def get_first_name(message: types.Message):
    await message.answer('Понял, сейчас отправлю вам полный список !', reply_markup=kb_yes_or_no)
    all_row = SqlQuery().get_all_row(table_name='agents')
    num = 0
    all_agents_param = '   Telegram ID   |   Ф.И.О   |   Номер телефона   \n\n'
    for row in all_row:
        value = f"{num + 1}.  <code>{row[1]}</code> | " \
                f"<i>{row[2].title()}</i>  " \
                f"<i>{row[3].title()}</i>  " \
                f"<i>{row[4].title()}</i> | " \
                f"{row[6]} \n\n"
        all_agents_param = all_agents_param + value
        num = num + 1

    await message.answer(all_agents_param)
    await message.answer('Данные пользователей отправлены, пожалуйста введите <b>пароль</b> чтобы продолжить',
                         reply_markup=ReplyKeyboardRemove())

    await SystemState.Start.set()


@dp.message_handler(Text(equals='Нет'), state=SystemState.UserShowAgent_Select)
async def get_first_name(message: types.Message):
    await message.answer('Понял, тогда мне нужен номер телефона пользователя', reply_markup=ReplyKeyboardRemove())
    await SystemState.UserShowAgent_CurrentUser.set()


@dp.message_handler(IsPhone(), state=SystemState.UserShowAgent_CurrentUser)
async def get_first_name(message: types.Message, state=FSMContext):
    number_object = message.text
    # Получаем с помощью регулярного выражения только числа
    decor_number = re.findall(r'\d+', number_object)
    # Получаем 9 чисел с правой стороны
    decor_number = int(''.join(decor_number)[-9:])
    # Добавляем код страны (988)
    decor_number = f'998{decor_number}'

    search_phone_to_db = SqlQuery().get_row(table_name='agents',
                                            search_param=[
                                                f"phone = '{decor_number}'"
                                            ])
    if search_phone_to_db:
        search_phone_to_db = search_phone_to_db[0]
        await message.answer('Вот информация на запрашиваемого вами агента:')
        await message.answer(f'Имя:  <code>{search_phone_to_db[2].title()}</code>\n'
                             f'Фамилия:  <code>{search_phone_to_db[3].title()}</code>\n'
                             f'Отчество:  <code>{search_phone_to_db[4].title()}</code>\n'
                             f'Дата рождения:  <code>{search_phone_to_db[5]}</code>\n'
                             f'Место проживания:  <code>{search_phone_to_db[7]}</code>\n'
                             f'Номер телефона:  <code>{search_phone_to_db[6]}</code>\n'
                             f'Телеграм ID:  <code>{search_phone_to_db[1]}</code>\n'
                             f'Недвижимость:  <code>{search_phone_to_db[8].title()}</code>\n'
                             f'Ранг:  <code>{search_phone_to_db[9].title()}</code>\n'
                             f'Участок:  <code>{search_phone_to_db[10]}</code>\n')
        await message.answer('Данные пользователя отправлены, пожалуйста введите <b>пароль</b> чтобы продолжить',
                             reply_markup=ReplyKeyboardRemove())

        await SystemState.Start.set()
    else:
        await message.answer('Пользователя с таким номером телефона не существует в базе данных')
