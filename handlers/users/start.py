from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from filters.user_access import UserAccess
from keyboards.default.apartment import kb_main_menu

from loader import dp


@dp.message_handler(CommandStart(), UserAccess(), state='*')
async def bot_start(message: types.Message, state=FSMContext):
    message_id = message.message_id - 3333
    chat_id = message.chat.id
    diapason = range(1000)
    await message.answer(f'Привет, {message.from_user.full_name}!\nДобро пожаловать в КупиДом бот!')
    await message.answer('Что тебе нужно?',
                         reply_markup=kb_main_menu)
    await state.reset_state()
    if message_id <= 0:
        pass
    else:
        for num in diapason:
            try:
                delete_message_id = message_id - num
            except:
                delete_message_id = message_id - num - 1
            await dp.bot.delete_message(chat_id, delete_message_id)
