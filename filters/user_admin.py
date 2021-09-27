from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from data.config import user_admin


class UserAdmin(BoundFilter):

    async def check(self, message: types.Message):
        admins = user_admin()
        id = str(message.from_user.id)
        for user in admins:
            if user == id:
                return True
        await message.answer('Вас нету в базе данных:(')
        return False
