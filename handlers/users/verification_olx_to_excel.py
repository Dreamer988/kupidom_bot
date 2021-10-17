import os

import pandas as pd
from aiogram import types
from aiogram.dispatcher import FSMContext

from filters.manager_access import ManagerAccess
from keyboards.default.rent_apartment import kb_main_menu
from loader import dp
from sql.sql_query import SqlQuery


@dp.message_handler(ManagerAccess(), commands=['excel'])
async def create_excel(message: types.Message, state=FSMContext):
    verification_olx = SqlQuery().get_all_row(table_name="olx_verification")
    if verification_olx is not None:
        type_of_property = list()
        district = list()
        sector = list()
        phone = list()
        description = list()
        date = list()
        agent_name = list()
        agent_description = list()
        action = list()

        for row in verification_olx:
            type_of_property.append(row[1])
            district.append(row[2])
            sector.append(row[3])
            phone.append(row[4])
            description.append(row[5])
            date.append(row[6])
            agent_name.append(row[7])
            agent_description.append(row[8])
            action.append(row[9])

        df = pd.DataFrame({'Тип недвижимости': type_of_property,
                           'Район': district,
                           'Участок номер': sector,
                           'Номер телефона': phone,
                           'Описание OLX': description,
                           'Дата отправки': date,
                           'Имя агента': agent_name,
                           'Описание агента': agent_description,
                           'Действие': action})
        df.to_excel('./olx_verification.xlsx')
        with open('./olx_verification.xlsx', 'rb') as excel:
            await dp.bot.send_document(message.from_user.id, excel)
        os.remove('./olx_verification.xlsx')

        SqlQuery().delete_all_row(table_name="olx_verification")

        await state.reset_state()
        await message.answer('Файл отправлен', reply_markup=kb_main_menu)
    else:
        await message.answer('В таблице нету данных...')
