from data.config import admins
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class UserAdmin(BoundFilter):

    async def check(self, message: types.Message):
        id = str(message.from_user.id)
        for user in admins:
            if user == id:
                return True
        await message.answer('Вас нету в базе данных:(')
        return False
