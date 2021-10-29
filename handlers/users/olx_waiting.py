import datetime
import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from filters.is_phone import IsPhone
from keyboards.default.olx import kb_olx_waiting_object_param
from keyboards.default.send_by_apartment import kb_main_menu
from loader import dp
from sql.sql_query import SqlQuery
from states import OLXState, SearchState


@dp.message_handler(state=OLXState.OLX_Waiting)
async def start_take_olx(message: types.Message, state=FSMContext):
    user_id = message.from_user.id

    user_information = SqlQuery().get_row(
        table_name="agents",
        search_param=[
            f"telegram_id = {user_id}"
        ])

    if message.text.strip().lower() == 'продолжить' and user_information is not None:

        user_type_of_property = user_information[0][8]
        user_sector = user_information[0][10]

        olx_object = SqlQuery().get_row_by_filters(
            table_name="olx_waiting",
            search_param=[
                f"type_of_property = '{user_type_of_property}'",
                f"sector = {user_sector}"
            ],
            filter_sort="ASC",
            filter_col="date")

        if olx_object is not None:
            await message.answer("Ваш OLX:")
            await message.answer(f"<b>Тип недвижимости:</b> {olx_object[0][1]}\n"
                                 f"<b>Район:</b> {olx_object[0][2]}\n"
                                 f"<b>Участок номер:</b> {olx_object[0][3]}\n"
                                 f"<b>Номер телефона:</b> {olx_object[0][4]}\n"
                                 f"<b>Описание:</b> {olx_object[0][5]}\n")
            await message.answer('Теперь:\n\n'
                                 '---  Если вы взяли OLX и отправили в бот нажмите на кнопку <b>Взял(-а)</b>\n\n'
                                 '---  Если объект продан или его передумали продавать нажмите на кнопку <b>Продан</b>\n\n'
                                 '---  Если вы хотите пропустить OLX нажмите на кнопку <b>Пропустить</b>\n\n',
                                 reply_markup=kb_olx_waiting_object_param)

            await state.update_data(
                var_olx_id=olx_object[0][0],
                var_user_id=message.from_user.id,
                var_type_of_property=olx_object[0][1],
                var_district=olx_object[0][2],
                var_sector=olx_object[0][3],
                var_phone=olx_object[0][4],
                var_information=olx_object[0][5]
            )
            await OLXState.OLX_Object_Waiting.set()
        else:
            await message.answer('OLX-а больше не осталось в базе', reply_markup=kb_main_menu)
            await state.reset_state()
    elif user_information is None:
        await message.answer("Вас нету в базе данных агентов", reply_markup=kb_main_menu)
        await state.reset_state()
    else:
        await message.answer("Переходим в главное меню", reply_markup=kb_main_menu)
        await state.reset_state()


@dp.message_handler(Text(equals='Взял(-а)'), state=OLXState.OLX_Object_Waiting)
async def take_object(message: types.Message, state=FSMContext):
    await message.answer('Введите номер телефона который вы укажете в объективке и под фотографиями')
    await OLXState.OLX_Get_Waiting.set()


@dp.message_handler(IsPhone(), state=OLXState.OLX_Get_Waiting)
async def take_object(message: types.Message, state=FSMContext):
    number_object = message.text
    # Получаем с помощью регулярного выражения только числа
    decor_number = re.findall(r'\d+', number_object)
    # Получаем 9 чисел с правой стороны
    decor_number = int(''.join(decor_number)[-9:])
    # Добавляем код страны 998
    decor_number = '998' + str(decor_number)

    await state.update_data(var_olx_phone=decor_number)

    values = await state.get_data()

    SqlQuery().delete_row(table_name="olx_waiting",
                          search_column_name="id",
                          search_value=values['var_olx_id'])

    await dp.bot.send_message(chat_id='-1001546119458', text=f"Агент: <b>{message.from_user.full_name}</b>\n"
                                                             f"Взял OLX:\n"
                                                             f"Тип недвижимости: <code>{values['var_type_of_property']}</code>\n"
                                                             f"Район: <code>{values['var_district']}</code>\n"
                                                             f"Участок номер: <code>{values['var_sector']}</code>\n"
                                                             f"Номер телефона: <code>{values['var_phone']}</code>\n"
                                                             f"Номер телефона(который заполнит агент): <code>{values['var_olx_phone']}</code>\n"
                                                             f"Описание: <code>{values['var_information']}</code>\n")

    await message.answer('Отлично, продолжайте в том же духе)', reply_markup=kb_main_menu)
    await state.reset_state()


@dp.message_handler(Text(equals='Продан'), state=OLXState.OLX_Object_Waiting)
async def sell_object(message: types.Message, state=FSMContext):
    action = message.text
    await state.update_data(var_action=action)
    await message.answer('Введие описание...')
    await OLXState.OLX_Sell_Waiting.set()


@dp.message_handler(state=OLXState.OLX_Sell_Waiting)
async def sell_object(message: types.Message, state=FSMContext):
    sell_desc = message.text
    values = await state.get_data()
    date = datetime.datetime.today().isoformat(timespec='seconds')

    SqlQuery().add_row(table_name="olx_verification",
                       keys=['type_of_property',
                             'district',
                             'sector',
                             'phone',
                             'information',
                             'date',
                             'agent',
                             'description_agent',
                             'action'],
                       values=(values['var_type_of_property'],
                               values['var_district'],
                               values['var_sector'],
                               values['var_phone'],
                               values['var_information'],
                               date,
                               message.from_user.full_name,
                               sell_desc,
                               values['var_action']))

    SqlQuery().delete_row(table_name="olx_waiting",
                          search_column_name="id",
                          search_value=values['var_olx_id'])

    await message.answer('Отлично, продолжайте в том же духе)', reply_markup=kb_main_menu)
    await state.reset_state()


@dp.message_handler(Text(equals='Пропустить'), state=OLXState.OLX_Object_Waiting)
async def skip(message: types.Message, state=FSMContext):
    date = datetime.datetime.today().isoformat(timespec='seconds')
    values = await state.get_data()
    SqlQuery().edit_row(table_name="olx_waiting",
                        search_column_name="id",
                        search_value=values['var_olx_id'],
                        edit_param=[
                            f"`date` = '{date}'"
                        ])
    await message.answer('Вы пропустили этот OLX')
    user_id = message.from_user.id

    user_information = SqlQuery().get_row(
        table_name="agents",
        search_param=[
            f"telegram_id = {user_id}"
        ])

    user_type_of_property = user_information[0][8]
    user_sector = user_information[0][10]

    olx_object = SqlQuery().get_row_by_filters(
        table_name="olx_waiting",
        search_param=[
            f"type_of_property = '{user_type_of_property}'",
            f"sector = {user_sector}"
        ],
        filter_sort="ASC",
        filter_col="date")

    if olx_object is not None:
        await message.answer("Ваш новый OLX:")
        await message.answer(f"<b>Тип недвижимости:</b> {olx_object[0][1]}\n"
                             f"<b>Район:</b> {olx_object[0][2]}\n"
                             f"<b>Участок номер:</b> {olx_object[0][3]}\n"
                             f"<b>Номер телефона:</b> {olx_object[0][4]}\n"
                             f"<b>Описание:</b> {olx_object[0][5]}\n")
        await message.answer('Теперь:\n\n'
                             '---  Если вы взяли OLX и отправили в бот нажмите на кнопку <b>Взял(-а)</b>\n\n'
                             '---  Если объект продан или его передумали продавать нажмите на кнопку <b>Продан</b>\n\n'
                             '---  Если вы хотите пропустить OLX нажмите на кнопку <b>Пропустить</b>\n\n',
                             reply_markup=kb_olx_waiting_object_param)

        await state.update_data(
            var_olx_id=olx_object[0][0],
            var_user_id=message.from_user.id,
            var_type_of_property=olx_object[0][1],
            var_district=olx_object[0][2],
            var_sector=olx_object[0][3],
            var_phone=olx_object[0][4],
            var_information=olx_object[0][5]
        )
        await OLXState.OLX_Object_Waiting.set()
    else:
        await message.answer('OLX-а больше не осталось в базе', reply_markup=kb_main_menu)
        await state.reset_state()


@dp.message_handler(Text(equals='Главное меню'), state=OLXState.OLX_Object_Waiting)
async def object_waiting(message: types.Message, state=FSMContext):
    await message.answer('Главное меню в вашем распоряжении',
                         reply_markup=kb_main_menu)
    await state.reset_state()


@dp.message_handler(Text(equals='Поиск по номеру'), state=OLXState.OLX_Object_Waiting)
async def object_waiting(message: types.Message, state=FSMContext):
    await message.answer('Введите номер телфона', reply_markup=ReplyKeyboardRemove())
    await SearchState.SearchNumber_Q1.set()
