from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from sql.sql_query import SqlQuery


class SuperManagerAccess(BoundFilter):

    async def check(self, message: types.Message):
        super_managers_db = SqlQuery().get_column_by_param(
            table_name='managers',
            get_column_name='telegram_id',
            search_column_name="position",
            search_value="super manager"
        )
        all_super_managers = []

        if super_managers_db:
            for manager in super_managers_db:
                all_super_managers.append(manager[0])
        else:
            pass
        super_manager_access = tuple(all_super_managers)

        id = message.from_user.id

        for user in super_manager_access:
            if int(user) == int(id):
                return True
        await message.answer('У вас не достаточно полномочий для перехода в эту стадию!\n'
                             'Чтобы перейти в системное меню нажмите команду /system')
        return False
