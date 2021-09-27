from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.by_sell import kb_type_transaction
from loader import dp
from states import MenuState, BySell


@dp.message_handler(Text(equals='Задаток'), state=MenuState.BySell)
async def select_by_sell(message: types.Message):
    await message.answer('Выберите вид сделки', reply_markup=kb_type_transaction)
    await BySell.Deposit_Q1.set()


@dp.message_handler(Text(equals='Оформление'), state=MenuState.BySell)
async def select_by_sell(message: types.Message):
    await message.answer('Выберите вид сделки', reply_markup=kb_type_transaction)
    await BySell.Registration_Q1.set()


@dp.message_handler(Text(equals='Аванс'), state=MenuState.BySell)
async def select_by_sell(message: types.Message):
    await message.answer('Укажите сумму взятого вами аванса',
                         reply_markup=ReplyKeyboardRemove())
    await BySell.Prepayment_Q1.set()
