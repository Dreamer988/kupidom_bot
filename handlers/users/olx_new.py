import datetime
import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from filters.is_digit import IsDigit
from google_work.google_work import GoogleWork
from keyboards.default.olx import kb_olx_new_object_param
from keyboards.default.send_by_apartment import kb_main_menu
from loader import dp
from sql.sql_query import SqlQuery
from states import OLXState


@dp.message_handler(state=OLXState.OLX_New)
async def start_take_olx(message: types.Message, state=FSMContext):
    if message.text.strip().lower() == "продолжить":
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
                                 '---  Если вы не можете дозвониться нажмите на кнопку <b>Не могу дозвониться</b>\n\n'
                                 '---  Если номер телефона выключен, вне зоны доступа и т.п. более 3-х дней нажмите на кнопку <b>Вне зоны доступа</b>\n\n'
                                 '---  Если участок указан не 0-ой и этот объект находиться не под вашим участком нажмите на кнопку <b>Не мой участок</b>\n\n'
                                 '---  Если вы не нашли общий язык, продавец не хочет работать с риелторами и т.п нажмите на кнопку <b>Не лояльный</b>\n\n'
                                 '---  Если объект не подходит под выше указанные параметры (Пример: объект находится в другом городе) нажмите на кнопку <b>Не лояльный</b>\n\n',
                                 reply_markup=kb_olx_new_object_param)

            await state.update_data(
                var_olx_id=olx_object[0][0],
                var_user_id=message.from_user.id,
                var_type_of_property=olx_object[0][1],
                var_district=olx_object[0][2],
                var_sector=olx_object[0][3],
                var_phone=olx_object[0][4],
                var_information=olx_object[0][5]
            )
            await OLXState.OLX_Object.set()
        else:
            await message.answer('OLX-а больше не осталось в базе', reply_markup=kb_main_menu)
            await state.reset_state()
    else:
        await message.answer(reply_markup=kb_main_menu)
        await state.reset_state()


@dp.message_handler(Text(equals='Взял(-а)'), state=OLXState.OLX_Object)
async def take_object(message: types.Message, state=FSMContext):
    await message.answer('Введите номер телефона который вы укажете в объективке и под фотографиями')
    await OLXState.OLX_Get.set()


@dp.message_handler(state=OLXState.OLX_Get)
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

    SqlQuery().delete_row(table_name="olx",
                          search_column_name="id",
                          search_value=values['var_olx_id'])

    await message.answer('Отлично, продолжайте в том же духе)', reply_markup=kb_main_menu)

    await dp.bot.send_message(chat_id='-1001546119458', text=f"Агент: <b>{message.from_user.full_name}</b> взял OLX:\n"
                                                             f"Тип недвижимости: <code>{values['var_type_of_property']}</code>\n"
                                                             f"Район: <code>{values['var_district']}</code>\n"
                                                             f"Участок номер: <code>{values['var_sector']}</code>\n"
                                                             f"Номер телефона: <code>{values['var_phone']}</code>\n"
                                                             f"Номер телефона(который заполнит агент): <code>{values['var_olx_phone']}</code>\n"
                                                             f"Описание: <code>{values['var_information']}</code>\n")
    await state.reset_state()


@dp.message_handler(Text(equals='Продан'), state=OLXState.OLX_Object)
async def sell_object(message: types.Message, state=FSMContext):
    action = message.text
    await state.update_data(var_action=action)
    await message.answer('Введие описание...')
    await OLXState.OLX_Sell.set()


@dp.message_handler(state=OLXState.OLX_Sell)
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

    SqlQuery().delete_row(table_name="olx",
                          search_column_name="id",
                          search_value=values['var_olx_id'])

    await message.answer('Отлично, продолжайте в том же духе)', reply_markup=kb_main_menu)
    await state.reset_state()


@dp.message_handler(Text(equals='Вне зоны доступа'), state=OLXState.OLX_Object)
async def zone_no_object(message: types.Message, state=FSMContext):
    action = message.text
    await state.update_data(var_action=action)
    await message.answer('Введие описание...')
    await OLXState.OLX_Zone.set()


@dp.message_handler(state=OLXState.OLX_Zone)
async def zone_no_object(message: types.Message, state=FSMContext):
    zone_desc = message.text
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
                               zone_desc,
                               values['var_action']))

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


@dp.message_handler(Text(equals='Не мой участок'), state=OLXState.OLX_Object)
async def call_no_object(message: types.Message, state=FSMContext):
    await message.answer('Укажите участок к которому относится этот OLX')
    await OLXState.OLX_Sector.set()


@dp.message_handler(IsDigit(), state=OLXState.OLX_Sector)
async def sector_edit(message: types.Message, state=FSMContext):
    sector = message.text.strip()
    values = await state.get_data()
    SqlQuery().edit_row(table_name="olx",
                        search_column_name="id",
                        search_value=values['var_olx_id'],
                        edit_param=[
                            f"`sector` = '{sector}'"
                        ])
    await message.answer('Участок изменен на другой.')
    await message.answer('Отлично, продолжайте в том же духе)', reply_markup=kb_main_menu)
    await state.reset_state()


@dp.message_handler(Text(equals='Удалить'), state=OLXState.OLX_Object)
async def call_no_object(message: types.Message, state=FSMContext):
    action = message.text
    await state.update_data(var_action=action)
    await message.answer('Введие описание...')
    await OLXState.OLX_Delete.set()


@dp.message_handler(state=OLXState.OLX_Delete)
async def call_no_object(message: types.Message, state=FSMContext):
    delete_desc = message.text
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
                               delete_desc,
                               values['var_action']))

    SqlQuery().delete_row(table_name="olx",
                          search_column_name="id",
                          search_value=values['var_olx_id'])

    await message.answer('Отлично, продолжайте в том же духе)', reply_markup=kb_main_menu)
    await state.reset_state()


@dp.message_handler(Text(equals='Не лояльный'), state=OLXState.OLX_Object)
async def call_no_object(message: types.Message, state=FSMContext):
    action = message.text
    await state.update_data(var_action=action)
    await message.answer('Введие описание...')
    await OLXState.OLX_NotLoyal.set()


@dp.message_handler(state=OLXState.OLX_NotLoyal)
async def call_no_object(message: types.Message, state=FSMContext):
    loyal_desc = message.text
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
                               loyal_desc,
                               values['var_action']))

    SqlQuery().delete_row(table_name="olx",
                          search_column_name="id",
                          search_value=values['var_olx_id'])

    await message.answer('Отлично, продолжайте в том же духе)', reply_markup=kb_main_menu)


@dp.message_handler(Text(equals='Маклер'), state=OLXState.OLX_Object)
async def call_no_object(message: types.Message, state=FSMContext):
    values = await state.get_data()
    GoogleWork().google_add_row(sheet_id='1o71IQm9tcRyDcYVApTig0Xx6zmEGv6lJq8c401lWW6c',
                                name_list='Маклера',
                                array_data=[values['var_phone']])
    await message.answer('Маклер добавлен в базу)', reply_markup=kb_main_menu)


@dp.message_handler(Text(equals='Ожидание'), state=OLXState.OLX_Object)
async def object_waiting(message: types.Message, state=FSMContext):
    values = await state.get_data()
    date = datetime.datetime.today().isoformat(timespec='seconds')

    count_waiting_object = SqlQuery().get_column_by_param(
        table_name="olx_waiting",
        get_column_name="id",
        search_column_name="sector",
        search_value=values['var_sector'],
    )
    if count_waiting_object is not None:
        if len(count_waiting_object) <= 7:

            SqlQuery().add_row(table_name="olx_waiting",
                               keys=['type_of_property',
                                     'district',
                                     'sector',
                                     'phone',
                                     'information',
                                     'date'],
                               values=(values['var_type_of_property'],
                                       values['var_district'],
                                       values['var_sector'],
                                       values['var_phone'],
                                       values['var_information'],
                                       date))

            SqlQuery().delete_row(table_name="olx",
                                  search_column_name="id",
                                  search_value=values['var_olx_id'])

            await message.answer('OLX добавлен в таблицу ожидания, теперь можете вернуться к этому OLX позже.',
                                 reply_markup=kb_main_menu)
            await state.reset_state()
        else:
            await message.answer('Вы превысили кол-во OLX в ожидании.\n'
                                 'Максимум в ожидании может находиться 7 OLX')
            await message.answer('Пожалуйста, очистите ожидание OLX!', reply_markup=kb_main_menu)
            await state.reset_state()
    else:

        SqlQuery().add_row(table_name="olx_waiting",
                           keys=['type_of_property',
                                 'district',
                                 'sector',
                                 'phone',
                                 'information',
                                 'date'],
                           values=(values['var_type_of_property'],
                                   values['var_district'],
                                   values['var_sector'],
                                   values['var_phone'],
                                   values['var_information'],
                                   date))

        SqlQuery().delete_row(table_name="olx",
                              search_column_name="id",
                              search_value=values['var_olx_id'])

        await message.answer('OLX добавлен в таблицу ожидания, теперь можете вернуться к этому OLX позже.',
                             reply_markup=kb_main_menu)
        await state.reset_state()
