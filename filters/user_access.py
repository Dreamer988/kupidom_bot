from data.config import users_access
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class UserAccess(BoundFilter):

    async def check(self, message: types.Message):
        id = str(message.from_user.id)
        for user in users_access:
            if user == id:
                return True
        await message.answer('Вас нету в базе данных:(')
        return False
