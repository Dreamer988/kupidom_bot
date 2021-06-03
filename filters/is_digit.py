from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsDigit(BoundFilter):

    async def check(self, message: types.Message):
        msg = message.text
        try:
            int(msg)
            return True
        except:
            await message.answer('Введено не число!\nПожалуйста повторите попытку')
            return False
