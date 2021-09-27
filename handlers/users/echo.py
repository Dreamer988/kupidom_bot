from aiogram import types
from loader import dp


@dp.message_handler(commands='step_back', state='*')
async def bot_echo(message: types.Message):
    state = dp.current_state(chat=message.chat.id, user=message.from_user.id)
    await message.answer(f'Состояние:{state}')
