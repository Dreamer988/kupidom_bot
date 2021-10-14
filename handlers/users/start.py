from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types.chat import ChatType

from filters.user_access import UserAccess
from keyboards.default.send_by_apartment import kb_main_menu
from loader import dp


@dp.message_handler(CommandStart(), UserAccess(), state='*', chat_type=ChatType.PRIVATE)
async def bot_start(message: types.Message, state=FSMContext):
    print(message.from_user.id)
    await message.answer(f'Привет, {message.from_user.full_name}!\nДобро пожаловать в КупиДом бот!')
    await message.answer('Что тебе нужно?',
                         reply_markup=kb_main_menu)
    await state.reset_state()
