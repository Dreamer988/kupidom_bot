from aiogram import types

from keyboards.default.system import kb_system_menu
from loader import dp
from states import SystemState


@dp.message_handler(state=SystemState.OlxMenu)
async def verification_password(message: types.Message):
    await message.answer('Добро пожаловать в системную часть бота !')
    await message.answer('Выберите что вам нужно.', reply_markup=kb_system_menu)
    await SystemState.MainMenu.set()
