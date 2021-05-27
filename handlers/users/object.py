from aiogram import types

from keyboards.default import kb_type_of_property
from loader import dp


@dp.message_handler(text="Объект")
async def get_kb_type_of_property(message: types.Message):
    await message.answer("Выберите вид недвижимости", reply_markup=kb_type_of_property)
