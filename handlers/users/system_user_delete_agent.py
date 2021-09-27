import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from filters.is_phone import IsPhone
from keyboards.default.send_by_apartment import kb_yes_or_no
from loader import dp
from sql.sql_query import SqlQuery
from states import SystemState


@dp.message_handler(Text(equals='Агент'), state=SystemState.UserDelete)
async def delete_start(message: types.Message):
    await message.answer('🔴🔴🔴 Внимание.\nБудьте очень внимательны при удалении!')
    await message.answer('Введите номер телефона пользователя \nу которого вы удалить из базы данных.')
    await SystemState.UserDeleteAgent_Q1.set()


@dp.message_handler(IsPhone(), state=SystemState.UserDeleteAgent_Q1)
async def search_by_number(message: types.Message, state=FSMContext):
    phone_number = message.text.strip()
    # Получаем с помощью регулярного выражения только числа
    decor_number = re.findall(r'\d+', phone_number)
    # Получаем 9 чисел с правой стороны
    decor_number = int(''.join(decor_number)[-9:])
    # Добавляем код страны 998
    decor_number = '998' + str(decor_number)

    await state.update_data(var_delete_phone=decor_number)

    search_phone_to_db = SqlQuery().get_row(table_name='agents',
                                            search_param=[
                                                f"phone = '{decor_number}'"
                                            ])

    if search_phone_to_db:
        search_phone_to_db = search_phone_to_db[0]
        await state.update_data(db_value=search_phone_to_db)
        await message.answer(f'Данные пользователя по этому номеру телефона:  <b>{decor_number}</b>')

        await message.answer(f'Имя:  <code>{search_phone_to_db[2].title()}</code>\n'
                             f'Фамилия:  <code>{search_phone_to_db[3].title()}</code>\n'
                             f'Отчество:  <code>{search_phone_to_db[4].title()}</code>\n'
                             f'Дата рождения:  <code>{search_phone_to_db[5]}</code>\n'
                             f'Место проживания:  <code>{search_phone_to_db[7]}</code>\n'
                             f'Номер телефона:  <code>{search_phone_to_db[6]}</code>\n'
                             f'Телеграм ID:  <code>{search_phone_to_db[1]}</code>\n'
                             f'Недвижимость:  <code>{search_phone_to_db[8].title()}</code>\n'
                             f'Ранг:  <code>{search_phone_to_db[9].title()}</code>\n'
                             f'Участок:  <code>{search_phone_to_db[10]}</code>\n')

        await message.answer('Вы уверены что хотите удалить этого пользователя?',
                             reply_markup=kb_yes_or_no)

        await SystemState.UserDeleteAgent_Q2.set()
    else:
        await message.answer(f'Данного номера: <b>{decor_number}</b> нету в базе данных')
        await message.answer(f'<b>Введите другой номер телефона</b>\n'
                             f'Или перейдите в главное меню нажав на команду /system', reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state=SystemState.UserDeleteAgent_Q2)
async def delete_agent_to_db(message: types.Message, state=FSMContext):
    values = await state.get_data()
    del_phone = values['var_delete_phone']
    if message.text.strip().lower() == 'да':
        SqlQuery().delete_row(table_name='agents',
                              search_column_name='phone',
                              search_value=del_phone,
                              )
        await message.answer('Пользователь удален')
        await message.answer('Пожалуйста введите <b>пароль</b> чтобы продолжить ...', reply_markup=ReplyKeyboardRemove())
        await SystemState.Start.set()
    elif message.text.strip().lower() == 'нет':
        await message.answer('Вы отменили удаление')
        await message.answer('Пожалуйста введите <b>пароль</b> чтобы продолжить ...', reply_markup=ReplyKeyboardRemove())
        await SystemState.Start.set()
    else:
        await message.answer('Вы ввели не верное значение!\nПожалуйста попробуйте снова.')
