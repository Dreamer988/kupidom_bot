from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from data.config import user_access


class UserAccess(BoundFilter):

    async def check(self, message: types.Message):
        users_access = user_access()
        
        id = message.from_user.id

        for user in users_access:
            if int(user) == int(id):
                return True
        await message.answer('Вас нету в базе данных:(')
        return False
