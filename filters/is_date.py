from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from datetime import datetime


class IsDate(BoundFilter):

    async def check(self, message: types.Message):
        date = message.text.strip()
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return True
        except:
            await message.answer('Вы ввели не корректную дату, повторите попытку!')
            return False
