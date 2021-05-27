from aiogram import types
from loader import dp


@dp.message_handler()
async def bot_echo(message: types.Message):
    await message.answer(f"Просим извинения, но \nФункция {message.text} еще не добавлена в бот :(")
