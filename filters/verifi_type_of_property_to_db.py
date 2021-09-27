from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import BoundFilter

from sql.sql_query import SqlQuery


class VerificationTypeOfPropertyToDB(BoundFilter):

    async def check(self, message: types.Message, state=FSMContext):
        type_of_property = message.text.strip()
        try:
            values = await state.get_data()
            search_sector_to_db = SqlQuery().get_row(table_name='agents',
                                                     search_param=[
                                                         f"type_of_property = '{type_of_property}'",
                                                         f"sector = '{values['var_sector']}'",
                                                     ])
            if search_sector_to_db:
                await message.answer(f'Участок под номером <b>{values["var_sector"]}</b>'
                                     f' и видом недвижимости <b>{type_of_property.title()}</b>'
                                     f' уже присвоен другому агенту.\n'
                                     f'<b>Введите номер другого участка</b>\n'
                                     f'Или перейдите в главное меню нажав на команду /system')
                return False
            else:
                return True
        except:
            await message.answer('Ошибка проверки Участка и Вид недвижимости')
            return False
