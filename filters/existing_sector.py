from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from datetime import datetime

from sql.sql_query import SqlQuery


class ExistingSector(BoundFilter):

    async def check(self, message: types.Message):
        sector = message.text.strip().lower()
        all_unique_sectors = SqlQuery().get_column_unique_values(table_name="agents",
                                                                 get_column_name="sector",
                                                                 filter_col="sector")
        for row in all_unique_sectors:
            if int(row[0]) == int(sector):
                return True
            else:
                continue

        await message.answer("Колышек забей, травку жуй! \n"
                             "Введите другой участок или перейдите меню")
        return False
