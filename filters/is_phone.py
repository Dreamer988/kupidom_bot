from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsPhone(BoundFilter):

    async def check(self, message: types.Message):
        msg = message.text
        try:
            if len(msg) < 7:
                await message.answer('В номере не достаночно цифр.\nПожалуйста повторите')
                return False
            else:
                int(msg)
                return True
        except:
            await message.answer('Введите релевантный номер телефона!')
            return False
