from datetime import date, timedelta

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from google_work.google_work import GoogleWork
from keyboards.default.calling import kb_calling
from keyboards.default.delete_object import kb_delete_type_of_property
from keyboards.default.rent_apartment import kb_main_menu
from loader import dp
from sql.sql_query import SqlQuery
from states import MenuState, ObjectState
from utils import activate


def search_call_object(user_full_name, values, num_col_date, num_col_user):
    new_date = date.today()
    call_object = None

    for row in values[1:]:
        object_date = str(row[num_col_date])
        old_date = date(int(object_date[-4:]), int(object_date[3:5]), int(object_date[:2]))
        if new_date > old_date and row[num_col_user].lower().strip() == user_full_name.lower().strip():
            new_date = old_date
            call_object = row
        else:
            pass

    if call_object is not None:
        return call_object
    else:
        return False


@dp.message_handler(state=MenuState.Calling)
async def get_menu(message: types.Message, state=FSMContext):
    user_full_name = message.from_user.full_name

    type_of_property_user = SqlQuery().get_column_by_param(table_name="agents",
                                                           get_column_name="type_of_property",
                                                           search_column_name="telegram_id",
                                                           search_value=message.from_user.id)
    try:
        type_of_property_user = type_of_property_user[0][0].lower().strip()
        await state.update_data(var_type_of_property_user=type_of_property_user)
    except:
        await message.answer("Вас нету в базе агентов или у вас не заполнено поле <b>Тип недвижимости</b>")

    if type_of_property_user == 'квартира':
        values = GoogleWork().google_get_values(sheet_id="1qu2vh3Wcp7gl8qFS9XQzR32ExzKc8-eVVC7v8wLlUxI",
                                                name_list="Лист обзвона квартир",
                                                start_col="A",
                                                end_col="AL",
                                                major_dimension="ROWS"
                                                )
        call_object = search_call_object(
            user_full_name=user_full_name,
            values=values,
            num_col_date=37,
            num_col_user=35
        )
        if call_object:
            await state.update_data(var_id_object=call_object[0])
            answer = f'<b>ID:</b>  <code>{call_object[0]}</code>\n' \
                     f'<b>Квартал:</b>  <code>{call_object[1]}</code>\n' \
                     f'<b>Ориентиры:</b>  <code>{call_object[2]}</code>\n' \
                     f'<b>Улица</b>:  <code>{call_object[3]}</code>\n' \
                     f'<b>Кол-во комнат:</b>  <code>{call_object[4]}</code>\n' \
                     f'<b>Этаж:</b>  <code>{call_object[5]}</code>\n' \
                     f'<b>Этаж-сть:</b>  <code>{call_object[6]}</code>\n' \
                     f'<b>S общая:</b>  <code>{call_object[7]}</code>\n' \
                     f'<b>Балкон:</b>  <code>{call_object[8]}</code>\n' \
                     f'<b>Сан.узел:</b>  <code>{call_object[9]}</code>\n' \
                     f'<b>Ремонт:</b>  <code>{call_object[10]}</code>\n' \
                     f'<b>Тип строения:</b>  <code>{call_object[11]}</code>\n' \
                     f'<b>Планировка:</b>  <code>{call_object[12]}</code>\n' \
                     f'<b>Тип постройки:</b>  <code>{call_object[13]}</code>\n' \
                     f'<b>Высота потолков:</b>  <code>{call_object[15]}</code>\n' \
                     f'<b>Мебель:</b>  <code>{call_object[16]}</code>\n' \
                     f'<b>Техника:</b>  <code>{call_object[17]}</code>\n' \
                     f'<b>Стартовая цена:</b>  <code>{call_object[21]}</code>\n' \
                     f'<b>Цена:</b>  <code>{call_object[22]}</code>\n' \
                     f'<b>Имя собственника:</b>  <code>{call_object[23]}</code>\n' \
                     f'<b>Номер телефона:</b>  {call_object[24]}\n' \
                     f'<b>Доп.номер телефона:</b>  {call_object[25]}\n' \
                     f'<b>Вариант:</b>  <code>{call_object[35]}</code>\n'
            await message.answer(answer, reply_markup=kb_calling)
            await MenuState.CallingMenu.set()
        else:
            await message.answer('Обзвона нету или он закончился')
            await state.reset_state()

    elif type_of_property_user == 'коммерция':
        values = GoogleWork().google_get_values(sheet_id="1qu2vh3Wcp7gl8qFS9XQzR32ExzKc8-eVVC7v8wLlUxI",
                                                name_list="Лист обзвона коммерции",
                                                start_col="A",
                                                end_col="AQ",
                                                major_dimension="ROWS"
                                                )
        call_object = search_call_object(
            user_full_name=user_full_name,
            values=values,
            num_col_date=42,
            num_col_user=40
        )
        if call_object:
            await state.update_data(var_id_object=call_object[0])
            answer = f'<b>ID:</b>  <code>{call_object[0]}</code>\n' \
                     f'<b>Район:</b>  <code>{call_object[1]}</code>\n' \
                     f'<b>Кол-во комнат:</b>  <code>{call_object[4]}</code>\n' \
                     f'<b>Этаж:</b>  <code>{call_object[5]}</code>\n' \
                     f'<b>Этаж-сть:</b>  <code>{call_object[6]}</code>\n' \
                     f'<b>S общая:</b>  <code>{call_object[7]}</code>\n' \
                     f'<b>S полезная:</b>  <code>{call_object[8]}</code>\n' \
                     f'<b>Площадь земли:</b>  <code>{call_object[14]}</code>\n' \
                     f'<b>Ремонт:</b>  <code>{call_object[9]}</code>\n' \
                     f'<b>Назначение:</b>  <code>{call_object[12]}</code>\n' \
                     f'<b>Тип строения:</b>  <code>{call_object[10]}</code>\n' \
                     f'<b>Тип недвижимости:</b>  <code>{call_object[11]}</code>\n' \
                     f'<b>Количество строений:</b>  <code>{call_object[13]}</code>\n' \
                     f'<b>Переведено в нежилое:</b>  <code>{call_object[15]}</code>\n' \
                     f'<b>Высота потолков:</b>  <code>{call_object[16]}</code>\n' \
                     f'<b>Проходимость:</b>  <code>{call_object[18]}</code>\n' \
                     f'<b>Завершенное строительство:</b>  <code>{call_object[21]}</code>\n' \
                     f'<b>Стартовая цена:</b>  <code>{call_object[23]}</code>\n' \
                     f'<b>Цена:</b>  <code>{call_object[24]}</code>\n' \
                     f'<b>Имя собственника:</b>  <code>{call_object[25]}</code>\n' \
                     f'<b>Номер телефона:</b>  {call_object[26]}\n' \
                     f'<b>Доп.номер телефона:</b>  {call_object[27]}\n' \
                     f'<b>Вариант:</b>  <code>{call_object[38]}</code>\n'
            await message.answer(answer, reply_markup=kb_calling)
            await MenuState.CallingMenu.set()
        else:
            await message.answer('Обзвона нету или он закончился')
            await state.reset_state()

    elif type_of_property_user == 'дом':
        values = GoogleWork().google_get_values(sheet_id="1qu2vh3Wcp7gl8qFS9XQzR32ExzKc8-eVVC7v8wLlUxI",
                                                name_list="Лист обзвона домов",
                                                start_col="A",
                                                end_col="AQ",
                                                major_dimension="ROWS"
                                                )
        call_object = search_call_object(
            user_full_name=user_full_name,
            values=values,
            num_col_date=36,
            num_col_user=34
        )
        if call_object:
            await state.update_data(var_id_object=call_object[0])
            answer = f'ID:  {call_object[0]}\n' \
                     f'Квартал:  {call_object[1]}\n' \
                     f'Кол-во комнат:  {call_object[2]}\n' \
                     f'Этаж:  {call_object[3]}\n' \
                     f'Этаж-сть:  {call_object[4]}\n' \
                     f'S общая:  {call_object[5]}\n' \
                     f'Сан.узел:  {call_object[6]}\n' \
                     f'Ремонт:  {call_object[7]}\n' \
                     f'Планировка:  {call_object[8]}\n' \
                     f'Тип постройки:  {call_object[9]}\n' \
                     f'Цена:  {call_object[10]}\n' \
                     f'Имя собственника:  {call_object[11]}\n' \
                     f'Номер телефона:  {call_object[12]}\n' \
                     f'Доп.номер телефона:  {call_object[13]}\n' \
                     f'Вариант:  {call_object[14]}'
            await message.answer(answer, reply_markup=kb_calling)
            await MenuState.CallingMenu.set()
        else:
            await message.answer('Обзвона нету или он закончился')
            await state.reset_state()

    else:
        await message.answer("Ошибка! У вас не заполнено поле <b>Тип недвижимости</b>")


@dp.message_handler(Text(equals="Удалить"), state=MenuState.CallingMenu)
async def delete(message: types.Message):
    await message.answer("Выберите тип недвижимости", reply_markup=kb_delete_type_of_property)
    await ObjectState.Delete.set()


@dp.message_handler(Text(equals="Изменить"), state=MenuState.CallingMenu)
async def delete(message: types.Message):
    await message.answer("Выберите тип недвижимости", reply_markup=kb_delete_type_of_property)
    await ObjectState.Edit.set()


@dp.message_handler(Text(equals="Активировать"), state=MenuState.CallingMenu)
async def delete(message: types.Message):
    await message.answer("Выберите тип недвижимости", reply_markup=kb_delete_type_of_property)
    await ObjectState.Activate.set()


@dp.message_handler(Text(equals="Не могу дозвониться"), state=MenuState.CallingMenu)
async def delete(message: types.Message, state=FSMContext):
    values_user = await state.get_data()
    type_of_property = values_user['var_type_of_property_user']
    id_object = values_user['var_id_object']

    if type_of_property == 'квартира':
        values = GoogleWork().google_get_values(sheet_id='1_OlIeV7jYMN5H6zXZOqVsKrfuDjlJwpkhGoIjOQIUkg',
                                                name_list='Общая база',
                                                start_col='A',
                                                end_col='AL',
                                                major_dimension='ROWS')
        num = 1
        for row in values:
            if row[0] == id_object:
                now_date = row[-1]
                now_date = date(int(now_date[-4:]), int(now_date[3:5]), int(now_date[:2]))
                new_date = now_date + timedelta(days=15)
                activate(type_of_property=type_of_property,
                         id_object=id_object,
                         date_enter=new_date)
                await message.answer('Объект перенесен, он прийдет к вам позже', reply_markup=kb_main_menu)
                await state.reset_state()
            else:
                num = num + 1
                pass

    if type_of_property == 'коммерция':
        values = GoogleWork().google_get_values(sheet_id='1Q2jSOeCYi2FPVs0gI7vLQVljw1DfYKBHdUq7HpZVz4k',
                                                name_list='Общая база',
                                                start_col='A',
                                                end_col='AQ',
                                                major_dimension='ROWS')
        num = 1
        for row in values:
            if row[0] == id_object:
                now_date = row[-1]
                now_date = date(int(now_date[-4:]), int(now_date[3:5]), int(now_date[:2]))
                new_date = now_date + timedelta(days=15)
                activate(type_of_property=type_of_property,
                         id_object=id_object,
                         date_enter=new_date)
                await message.answer('Объект перенесен, он прийдет к вам позже', reply_markup=kb_main_menu)
                await state.reset_state()
            else:
                num = num + 1
                pass

    if type_of_property == 'дом':
        values = GoogleWork().google_get_values(sheet_id='1zLwG9oJQU3wHSe0OQgOO27v7EDF_CCWrRVji1qr3dqs',
                                                name_list='Общая база',
                                                start_col='A',
                                                end_col='AK',
                                                major_dimension='ROWS')
        num = 1
        for row in values:
            if row[0] == id_object:
                now_date = row[-1]
                now_date = date(int(now_date[-4:]), int(now_date[3:5]), int(now_date[:2]))
                new_date = now_date + timedelta(days=15)
                activate(type_of_property=type_of_property,
                         id_object=id_object,
                         date_enter=new_date)
                await message.answer('Объект перенесен, он прийдет к вам позже', reply_markup=kb_main_menu)
                await state.reset_state()
            else:
                num = num + 1
                pass
