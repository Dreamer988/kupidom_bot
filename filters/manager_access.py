from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from sql.sql_query import SqlQuery


class ManagerAccess(BoundFilter):

    async def check(self, message: types.Message):
        managers_db = SqlQuery().get_column(
            table_name='managers',
            get_column_name='telegram_id',
        )
        all_managers = []

        if managers_db:
            for manager in managers_db:
                all_managers.append(manager[0])
        else:
            pass
        manager_access = tuple(all_managers)

        id = message.from_user.id

        for user in manager_access:
            if int(user) == int(id):
                return True
        await message.answer('Вас нету в базе данных менеджеров :(')
        return False
