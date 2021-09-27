from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import BoundFilter

from sql.sql_query import SqlQuery


class VerificationSectorToDB(BoundFilter):

    async def check(self, message: types.Message, state=FSMContext):
        try:
            sector = message.text.strip()
            search_sector_to_db = SqlQuery().get_row(table_name='agents',
                                                     search_param=[
                                                         f"sector = '{sector}'"
                                                     ])
            if search_sector_to_db:
                await message.answer(f'Участок под номером <b>{sector}</b>'
                                     f' уже присвоен другому агенту.\n'
                                     f'<b>Введите номер другого участка</b>\n'
                                     f'Или перейдите в главное меню нажав на команду /system')
                return False
            else:
                return True
        except:
            await message.answer('Ошибка проверки Участка и Вида недвижимости')
            return False
