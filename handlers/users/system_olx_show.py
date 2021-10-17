from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from filters.is_digit import IsDigit
from keyboards.default.delete_object import kb_yes_or_no
from loader import dp
from sql.sql_query import SqlQuery
from states import SystemState


@dp.message_handler(Text(equals="Просмотреть"), state=SystemState.OlxStart)
async def start_system_olx(message: types.Message, state=FSMContext):
    await message.answer('Хотите просмотреть кол-во OLX во всех секторах ?', reply_markup=kb_yes_or_no)
    await SystemState.OLX_Show.set()


@dp.message_handler(Text(equals='Да'), state=SystemState.OLX_Show)
async def get_first_name(message: types.Message):
    await message.answer('Понял, сейчас отправлю вам полный список !', reply_markup=ReplyKeyboardRemove())
    unique_sector = SqlQuery().get_column_unique_values(table_name="olx",
                                                        get_column_name="sector")
    answer = 'Полный список:\n\n'

    for sector in unique_sector:
        count_sector = SqlQuery().get_count_by_param(table_name="olx",
                                                     search_column_name="sector",
                                                     search_value=sector[0])
        answer = answer + f"{sector[0]} сектор:  <code>{count_sector[0][0]} шт.</code>\n"
    await message.answer(answer)
    await message.answer('Данные отправлены, пожалуйста введите <b>пароль</b> чтобы продолжить',
                         reply_markup=ReplyKeyboardRemove())

    await SystemState.Start.set()


@dp.message_handler(Text(equals='Нет'), state=SystemState.OLX_Show)
async def get_first_name(message: types.Message):
    await message.answer('Понял, тогда мне нужен номер участка', reply_markup=ReplyKeyboardRemove())
    await SystemState.OLX_Show_CurrentSector.set()


@dp.message_handler(IsDigit(), state=SystemState.OLX_Show_CurrentSector)
async def get_first_name(message: types.Message):
    sector = message.text.strip()
    count_sector = SqlQuery().get_count_by_param(table_name="olx",
                                                 search_column_name="sector",
                                                 search_value=sector)
    await message.answer(f"{sector} сектор:  <code>{count_sector[0][0]} шт.</code>", reply_markup=ReplyKeyboardRemove())
    await message.answer('Данные отправлены, пожалуйста введите <b>пароль</b> чтобы продолжить',
                         reply_markup=ReplyKeyboardRemove())

    await SystemState.Start.set()
