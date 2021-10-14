from aiogram import types

from keyboards.default.olx import kb_olx_next
from loader import dp
from states import MenuState
from states import OLXState


@dp.message_handler(state=MenuState.OLX)
async def get_menu(message: types.Message):
    if message.text.strip().lower() == "новый":
        await OLXState.OLX_New.set()
        await message.answer("Продолжить или вернуться в главное меню?", reply_markup=kb_olx_next)
    else:
        await OLXState.OLX_Waiting.set()
        await message.answer("Продолжить или вернуться в главное меню?", reply_markup=kb_olx_next)
