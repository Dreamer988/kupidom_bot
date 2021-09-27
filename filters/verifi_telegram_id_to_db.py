from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from sql.sql_query import SqlQuery


class VerificationTelegramIdToDB(BoundFilter):

    async def check(self, message: types.Message):
        telegram_id = message.text.strip()

        search_agent_to_db = SqlQuery().get_row(table_name='agents',
                                                search_param=[
                                                    f"telegram_id = '{telegram_id}'",
                                                ])
        if search_agent_to_db:
            await message.answer(
                f"Пользователь с Телеграм ID: <b>{telegram_id}</b>\n"
                f"Уже сушествует в базе данных\n"
                f"<b>Введите другой Телеграм ID</b>\n"
                f"Или перейдите в главное меню нажав на команду /system")
            return False

        else:
            return True
