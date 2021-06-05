from aiogram import types

from filters.is_phone import IsPhone
from keyboards.default.by_sell import kb_type_transaction
from loader import dp
from states import MenuState, BySell


@dp.message_handler(IsPhone(),state=MenuState.Broker)
async def select_by_sell(message: types.Message):
    broker = message.text
    broker
    await message.answer('Выберите вид сделки', reply_markup=kb_type_transaction)
    await BySell.Deposit_Q1.set()
