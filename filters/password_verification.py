import os

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from dotenv import load_dotenv

load_dotenv()


class PasswordVerification(BoundFilter):

    async def check(self, message: types.Message):
        password = os.getenv('SYSTEM_BOT_PASSWORD')
        if str(message.text) == str(password):
            await message.answer('Пароль верный')
            return True
        else:
            await message.answer('Не верный пароль')
            return False


