import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from keyboards.default.send_by_apartment import kb_main_menu
from keyboards.default.system import kb_olx_object
from loader import dp
from states import MenuState, OLXState
from sql.sql_query import SqlQuery


@dp.message_handler(state=MenuState.OLX)
async def start_take_olx(message: types.Message, state=FSMContext):
    if message.text.strip().lower() == 'да':
        user_id = message.from_user.id
        user_information = SqlQuery().get_row(
            table_name="agents",
            search_param=[
                f"telegram_id = {user_id}"
            ])
        user_type_of_property = user_information[0][8]
        user_sector = user_information[0][10]
        olx_object = SqlQuery().get_row_by_filters(
            table_name="olx",
            search_param=[
                f"type_of_property = '{user_type_of_property}'",
                f"sector = {user_sector}"
            ],
            filter_col="date")
        if olx_object is not None:
            await message.answer("Ваш OLX:")
            await message.answer(f"Тип недвижимости: {olx_object[0][1]}\n"
                                 f"Район: {olx_object[0][2]}\n"
                                 f"Участок номер: {olx_object[0][3]}\n"
                                 f"Номер телефона: {olx_object[0][4]}\n"
                                 f"Описание: {olx_object[0][5]}\n")
            await message.answer('Теперь:\n\n'
                                 '---  Если вы взяли OLX и отправили в бот нажмите на кнопку <b>Взял(-а)</b>\n\n'
                                 '---  Если объект продан или его передумали продавать нажмите на кнопку <b>Продан</b>\n\n'
                                 '---  Если вы не можете дозвониться нажмите на кнопку <b>Не могу дозвониться</b>\n\n'
                                 '---  Если номер телефона выключен, вне зоны доступа и т.п. нажмите на кнопку <b>Вне зоны доступа</b>',
                                 reply_markup=kb_olx_object)

            await state.update_data(var_olx_id=olx_object[0][0])
            await OLXState.OLX_Object.set()
        else:
            await message.answer('OLX-а больше не осталось в базе', reply_markup=kb_main_menu)
            await state.reset_state()

    elif message.text.strip().lower() == "нет":
        await state.reset_state()
        await message.answer('Вы отменили новый OLX', reply_markup=kb_main_menu)


@dp.message_handler(Text(equals='Взял(-а)'), state=OLXState.OLX_Object)
async def take_object(message: types.Message, state=FSMContext):
    values = await state.get_data()
    SqlQuery().delete_row(table_name="olx",
                          search_column_name="id",
                          search_value=values['var_olx_id'])
    await message.answer('Отлично, продолжайте в том же духе)', reply_markup=kb_main_menu)
    await state.reset_state()


@dp.message_handler(Text(equals='Продан'), state=OLXState.OLX_Object)
async def sell_object(message: types.Message, state=FSMContext):
    values = await state.get_data()
    SqlQuery().delete_row(table_name="olx",
                          search_column_name="id",
                          search_value=values['var_olx_id'])
    await message.answer('Отлично, продолжайте в том же духе)', reply_markup=kb_main_menu)
    await state.reset_state()


@dp.message_handler(Text(equals='Вне зоны доступа'), state=OLXState.OLX_Object)
async def zone_no_object(message: types.Message, state=FSMContext):
    values = await state.get_data()
    SqlQuery().delete_row(table_name="olx",
                          search_column_name="id",
                          search_value=values['var_olx_id'])
    await message.answer('Отлично, продолжайте в том же духе)', reply_markup=kb_main_menu)
    await state.reset_state()


@dp.message_handler(Text(equals='Не могу дозвониться'), state=OLXState.OLX_Object)
async def call_no_object(message: types.Message, state=FSMContext):
    date = datetime.datetime.today().isoformat(timespec='seconds')
    values = await state.get_data()
    SqlQuery().edit_row(table_name="olx",
                        search_column_name="id",
                        search_value=values['var_olx_id'],
                        edit_param=[
                            f"`date` = '{date}'"
                        ])
    await message.answer('Теперь этот OLX прийдет вам позже')
    await message.answer('Отлично, продолжайте в том же духе)', reply_markup=kb_main_menu)
    await state.reset_state()
