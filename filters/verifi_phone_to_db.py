import re

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from sql.sql_query import SqlQuery


class VerificationPhoneToDB(BoundFilter):

    async def check(self, message: types.Message):
        phone_number = message.text.strip()
        # Получаем с помощью регулярного выражения только числа
        decor_number = re.findall(r'\d+', phone_number)
        # Получаем 9 чисел с правой стороны
        decor_number = int(''.join(decor_number)[-9:])
        # Добавляем код страны 998
        decor_number = '998' + str(decor_number)

        search_number_to_db = SqlQuery().get_row(table_name='agents',
                                                 search_param=[
                                                     f"phone = '{decor_number}'",
                                                 ])
        if search_number_to_db:
            await message.answer(f'Пользователь с номером телефона <b>{decor_number}</b>\n'
                                 f'Уже существует в базе данных\n'
                                 f'<b>Введите другой номер телефона</b>\n'
                                 f'Или перейдите в главное меню нажав на команду /system')
            return False
        else:
            return True
