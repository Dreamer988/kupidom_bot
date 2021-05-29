from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from keyboards.default.apartment import kb_main_menu

from loader import dp


@dp.message_handler(Command("state"), state='*')
async def bot_start(message: types.Message, state=FSMContext):
    user_state = await state.get_state()
    await message.answer(f'Ты находишься в состоянии {user_state}')

