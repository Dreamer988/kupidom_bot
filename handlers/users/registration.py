import os
from datetime import date

import googleapiclient
import httplib2
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from googleapiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials

from filters.is_phone import IsPhone
from keyboards.default.apartment import kb_back, kb_yes_or_no, kb_main_menu
from keyboards.default.by_sell import kb_type_transaction, kb_contract, kb_reference
from loader import dp
from states import BySell


def google_sendler(sheet_id, start_col, end_col, array_data):
    CREDENTAILS_FILE = os.getenv('CREDENTAILS_FILE')
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTAILS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)
    spreadsheet_id = sheet_id

    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=f"{start_col}:{end_col}",
        majorDimension="COLUMNS"
    ).execute()
    start_range = len(values['values'][0]) + 1
    sheet_range = f"{start_col}{start_range}:{end_col}{start_range}"

    values = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=f"{start_col}{start_range}",
        valueInputOption="USER_ENTERED",
        body={
            "values": [['']]
        }
    ).execute()

    values = service.spreadsheets().values().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body={
            "valueInputOption": "USER_ENTERED",
            "data": [
                {
                    "range": sheet_range,
                    "majorDimension": "ROWS",
                    "values": [array_data]
                }
            ]
        }
    ).execute()


@dp.message_handler(state=BySell.Registration_Q1)
async def set_registration(message: types.Message, state=FSMContext):
    type_transaction = message.text
    await state.update_data(var_type_transaction=type_transaction)
    await message.answer('Введите ID объекта:', reply_markup=ReplyKeyboardRemove())
    await BySell.Registration_Q2.set()


@dp.message_handler(state=BySell.Registration_Q2)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Registration_Q1.set()
        await message.answer('Выберите вид сделки', reply_markup=kb_type_transaction)
    else:
        id = message.text
        await state.update_data(var_id=id)
        await message.answer('Введите адрес объекта:', reply_markup=kb_back)
        await BySell.Registration_Q3.set()


@dp.message_handler(state=BySell.Registration_Q3)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Registration_Q2.set()
        await message.answer('Введите ID объекта:', reply_markup=ReplyKeyboardRemove())
    else:
        address = message.text
        await state.update_data(var_address=address)
        await message.answer('Укажите имя агента или агентов который принес этот объект', reply_markup=kb_back)
        await BySell.Registration_Q4.set()


@dp.message_handler(state=BySell.Registration_Q4)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Registration_Q3.set()
        await message.answer('Введите адрес объекта:', reply_markup=kb_back)
    else:
        agent_name_take_object = message.text
        await state.update_data(var_agent_name_take_object=agent_name_take_object)
        await message.answer('Укажите имя агента или агентов кто продал этот объект', reply_markup=kb_back)
        await BySell.Registration_Q5.set()


@dp.message_handler(state=BySell.Registration_Q5)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Registration_Q4.set()
        await message.answer('Укажите имя агента или агентов который принес этот объект', reply_markup=kb_back)
    else:
        agent_name_sell_object = message.text
        await state.update_data(var_agent_name_sell_object=agent_name_sell_object)
        await message.answer('Укажите имя агента или агентов кто оформил этот объект', reply_markup=kb_back)
        await BySell.Registration_Q6.set()


@dp.message_handler(state=BySell.Registration_Q6)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Registration_Q5.set()
        await message.answer('Укажите имя агента или агентов кто продал этот объект', reply_markup=kb_back)
    else:
        agent_name_reg_object = message.text
        await state.update_data(var_agent_name_reg_object=agent_name_reg_object)
        await message.answer('Введите имя покупателя', reply_markup=kb_back)
        await BySell.Registration_Q7.set()


@dp.message_handler(state=BySell.Registration_Q7)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Registration_Q6.set()
        await message.answer('Укажите имя агента или агентов кто оформил этот объект', reply_markup=kb_back)
    else:
        buyer_name = message.text
        await state.update_data(var_buyer_name=buyer_name)
        await message.answer('Введите номер телефона покупателя', reply_markup=kb_back)
        await BySell.Registration_Q8.set()


@dp.message_handler(IsPhone(), state=BySell.Registration_Q8)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Registration_Q7.set()
        await message.answer('Введите имя покупателя', reply_markup=kb_back)
    else:
        buyer_phone = message.text
        await state.update_data(var_buyer_phone=buyer_phone)
        await message.answer('Введите имя продавца', reply_markup=kb_back)
        await BySell.Registration_Q9.set()


@dp.message_handler(state=BySell.Registration_Q9)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Registration_Q8.set()
        await message.answer('Введите номер телефона покупателя', reply_markup=kb_back)
    else:
        seller_name = message.text
        await state.update_data(var_seller_name=seller_name)
        await message.answer('Введите номер телефона продавца', reply_markup=kb_back)
        await BySell.Registration_Q10.set()


@dp.message_handler(IsPhone(), state=BySell.Registration_Q10)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Registration_Q9.set()
        await message.answer('Введите имя продавца', reply_markup=kb_back)
    else:
        seller_phone = message.text
        await state.update_data(var_seller_phone=seller_phone)
        await message.answer('Укажите дату оформления (Пример : 01.12.2020)', reply_markup=kb_back)
        await BySell.Registration_Q11.set()


@dp.message_handler(state=BySell.Registration_Q11)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Registration_Q10.set()
        await message.answer('Введите номер телефона продавца', reply_markup=kb_back)
    else:
        date_registration = message.text
        await state.update_data(var_date_registration=date_registration)
        await message.answer('Укажите итоговую стоимость квартиры ($)', reply_markup=kb_back)
        await BySell.Registration_Q12.set()


@dp.message_handler(state=BySell.Registration_Q12)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Registration_Q11.set()
        await message.answer('Укажите дату оформления (Пример : 01.12.2020)', reply_markup=kb_back)
    else:
        total_cost = message.text
        await state.update_data(var_total_cost=total_cost)
        await message.answer('Укажите сумму нашей комиссии ($)', reply_markup=kb_back)
        await BySell.Registration_Q13.set()


@dp.message_handler(state=BySell.Registration_Q13)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Registration_Q12.set()
        await message.answer('Укажите итоговую стоимость квартиры ($)', reply_markup=kb_back)
    else:
        commission = message.text
        await state.update_data(var_commission=commission)
        await message.answer('Укажите информатора', reply_markup=kb_back)
        await BySell.Registration_Q14.set()


@dp.message_handler(state=BySell.Registration_Q14)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Registration_Q13.set()
        await message.answer('Укажите сумму нашей комиссии ($)', reply_markup=kb_back)
    else:
        informant = message.text
        await state.update_data(var_informant=informant)
        await message.answer('Укажите номер информатора', reply_markup=kb_back)
        await BySell.Registration_Q15.set()


@dp.message_handler(state=BySell.Registration_Q15)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Registration_Q14.set()
        await message.answer('Укажите информатора', reply_markup=kb_back)
    else:
        informant_phone = message.text
        await state.update_data(var_informant_phone=informant_phone)
        await message.answer('Укажите вознаграждение информатора ($)', reply_markup=kb_back)
        await BySell.Registration_Q16.set()


@dp.message_handler(state=BySell.Registration_Q16)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Registration_Q15.set()
        await message.answer('Укажите номер информатора', reply_markup=kb_back)
    else:
        informant_reward = message.text
        await state.update_data(var_informant_reward=informant_reward)
        await message.answer('Подписали Договор / ИКУ ?', reply_markup=kb_contract)
        await BySell.Registration_Q17.set()


@dp.message_handler(state=BySell.Registration_Q17)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Registration_Q16.set()
        await message.answer('Укажите вознаграждение информатора ($)', reply_markup=kb_back)
    else:
        contract = message.text
        await state.update_data(var_contract=contract)
        await message.answer('Отправили справки или акт сверки ?', reply_markup=kb_reference)
        await BySell.Registration_Q18.set()


@dp.message_handler(state=BySell.Registration_Q18)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Registration_Q17.set()
        await message.answer('Подписали Договор / ИКУ ?', reply_markup=kb_contract)
    else:
        reference = message.text
        await state.update_data(var_reference=reference)
        await message.answer('Взяли видео отзыв?', reply_markup=kb_yes_or_no)
        await BySell.Registration_Q19.set()


@dp.message_handler(state=BySell.Registration_Q19)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Registration_Q18.set()
        await message.answer('Отправили справки или акт сверки ?', reply_markup=kb_reference)
    else:
        video_review = message.text
        await state.update_data(var_video_review=video_review)
        await message.answer('Все заполнил(-а) правильно ?', reply_markup=kb_yes_or_no)
        await BySell.Registration_Q20.set()


@dp.message_handler(state=BySell.Registration_Q20)
async def select_district(message: types.Message, state=FSMContext):
    filled_in_correctly = message.text
    answer = await state.get_data()
    user_name = message.from_user.full_name

    if filled_in_correctly.lower() == 'да':
        dt_time = str(date.today())
        answer = await state.get_data()
        list_answer = []
        list_answer.append(dt_time)
        list_answer.append(answer['var_type_transaction'])
        list_answer.append(user_name)
        list_answer.append(answer['var_address'])
        list_answer.append(answer['var_id'])
        list_answer.append(answer['var_commission'])
        list_answer.append(answer['var_total_cost'])
        list_answer.append(answer['var_buyer_name'])
        list_answer.append(answer['var_buyer_phone'])
        list_answer.append(answer['var_seller_name'])
        list_answer.append(answer['var_seller_phone'])
        list_answer.append(answer['var_date_registration'])
        list_answer.append(answer['var_agent_name_take_object'])
        list_answer.append(answer['var_agent_name_sell_object'])
        list_answer.append(answer['var_agent_name_reg_object'])
        list_answer.append(answer['var_informant'])
        list_answer.append(answer['var_informant_phone'])
        list_answer.append(answer['var_informant_reward'])
        list_answer.append(answer['var_contract'])
        list_answer.append(answer['var_reference'])
        list_answer.append(answer['var_video_review'])
        await state.reset_state()
        await message.answer('Оформление отправлено', reply_markup=kb_main_menu)
        google_sendler('1cybTRAnHDJ1gRiX5aY9XkD_84LXbMKccQPmjZn4YcCs', 'Оформление!A', 'U', list_answer)
    elif filled_in_correctly.lower() == 'нет':
        await state.reset_state()
        await message.answer('Вы отменили отправку', reply_markup=kb_main_menu)
    else:
        await message.answer('Отправлено не верное значение( Попробуйте снова')
