from datetime import date

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from filters.is_phone import IsPhone
from google_work.google_work import GoogleWork
from keyboards.default.send_by_apartment import kb_yes_or_no, kb_main_menu
from keyboards.default.by_sell import kb_type_transaction
from keyboards.default.step_back import kb_back
from loader import dp
from states import BySell


@dp.message_handler(state=BySell.Deposit_Q1)
async def set_registration(message: types.Message, state=FSMContext):
    type_transaction = message.text
    await state.update_data(var_type_transaction=type_transaction)
    await message.answer('Введите ID объекта:', reply_markup=ReplyKeyboardRemove())
    await BySell.Deposit_Q2.set()


@dp.message_handler(state=BySell.Deposit_Q2)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Deposit_Q1.set()
        await message.answer('Выберите вид сделки', reply_markup=kb_type_transaction)
    else:
        id = message.text
        await state.update_data(var_id=id)
        await message.answer('Введите адрес объекта:', reply_markup=kb_back)
        await BySell.Deposit_Q3.set()


@dp.message_handler(state=BySell.Deposit_Q3)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Deposit_Q2.set()
        await message.answer('Введите ID объекта:', reply_markup=kb_back)
    else:
        address = message.text
        await state.update_data(var_address=address)
        await message.answer('Введите имя покупателя', reply_markup=kb_back)
        await BySell.Deposit_Q4.set()


@dp.message_handler(state=BySell.Deposit_Q4)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Deposit_Q3.set()
        await message.answer('Введите адрес объекта:', reply_markup=kb_back)
    else:
        buyer_name = message.text
        await state.update_data(var_buyer_name=buyer_name)
        await message.answer('Введите номер телефона покупателя', reply_markup=kb_back)
        await BySell.Deposit_Q5.set()


@dp.message_handler(IsPhone(), state=BySell.Deposit_Q5)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Deposit_Q4.set()
        await message.answer('Введите имя покупателя', reply_markup=kb_back)
    else:
        buyer_phone = message.text
        await state.update_data(var_buyer_phone=buyer_phone)
        await message.answer('Введите имя продавца', reply_markup=kb_back)
        await BySell.Deposit_Q6.set()


@dp.message_handler(state=BySell.Deposit_Q6)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Deposit_Q5.set()
        await message.answer('Введите номер телефона покупателя', reply_markup=kb_back)
    else:
        seller_name = message.text
        await state.update_data(var_seller_name=seller_name)
        await message.answer('Введите номер телефона продавца', reply_markup=kb_back)
        await BySell.Deposit_Q7.set()


@dp.message_handler(IsPhone(), state=BySell.Deposit_Q7)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Deposit_Q6.set()
        await message.answer('Введите имя продавца', reply_markup=kb_back)
    else:
        seller_phone = message.text
        await state.update_data(var_seller_phone=seller_phone)
        await message.answer('Укажите итоговую стоимость квартиры ($)', reply_markup=kb_back)
        await BySell.Deposit_Q8.set()


@dp.message_handler(state=BySell.Deposit_Q8)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Deposit_Q7.set()
        await message.answer('Введите номер телефона продавца', reply_markup=kb_back)
    else:
        total_cost = message.text
        await state.update_data(var_total_cost=total_cost)
        await message.answer('Укажите сумму нашей комиссии ($)', reply_markup=kb_back)
        await BySell.Deposit_Q9.set()


@dp.message_handler(state=BySell.Deposit_Q9)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Deposit_Q8.set()
        await message.answer('Укажите итоговую стоимость квартиры ($)', reply_markup=kb_back)
    else:
        commission = message.text
        await state.update_data(var_commission=commission)
        await message.answer('Укажите информатора', reply_markup=kb_back)
        await BySell.Deposit_Q10.set()


@dp.message_handler(state=BySell.Deposit_Q10)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Deposit_Q9.set()
        await message.answer('Укажите сумму нашей комиссии ($)', reply_markup=kb_back)
    else:
        informant = message.text
        await state.update_data(var_informant=informant)
        await message.answer('Укажите номер информатора', reply_markup=kb_back)
        await BySell.Deposit_Q11.set()


@dp.message_handler(state=BySell.Deposit_Q11)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Deposit_Q10.set()
        await message.answer('Укажите информатора', reply_markup=kb_back)
    else:
        informant_phone = message.text
        await state.update_data(var_informant_phone=informant_phone)
        await message.answer('Укажите вознаграждение информатора ($)', reply_markup=kb_back)
        await BySell.Deposit_Q12.set()


@dp.message_handler(state=BySell.Deposit_Q12)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Deposit_Q11.set()
        await message.answer('Укажите номер информатора', reply_markup=kb_back)
    else:
        informant_reward = message.text
        await state.update_data(var_informant_reward=informant_reward)
        await message.answer('Укажите сумму задатка', reply_markup=kb_back)
        await BySell.Deposit_Q13.set()


@dp.message_handler(state=BySell.Deposit_Q13)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Deposit_Q12.set()
        await message.answer('Укажите номер информатора', reply_markup=kb_back)
    else:
        sum_deposit = message.text
        await state.update_data(var_sum_deposit=sum_deposit)
        await message.answer('Укажите дату заключения договора задатка (Пример : 01.12.2020)', reply_markup=kb_back)
        await BySell.Deposit_Q14.set()


@dp.message_handler(state=BySell.Deposit_Q14)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Deposit_Q13.set()
        await message.answer('Укажите вознаграждение информатора ($)', reply_markup=kb_back)
    else:
        date_start_contract = message.text
        await state.update_data(var_date_start_contract=date_start_contract)
        await message.answer('Укажите дату окончания договора задатка (Пример : 01.12.2020)', reply_markup=kb_back)
        await BySell.Deposit_Q15.set()


@dp.message_handler(state=BySell.Deposit_Q15)
async def set_registration(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Deposit_Q14.set()
        await message.answer('Укажите дату заключения договора задатка (Пример : 01.12.2020)', reply_markup=kb_back)
    else:
        date_end_contract = message.text
        await state.update_data(var_date_end_contract=date_end_contract)
        await message.answer('Все заполнил(-а) правильно ?', reply_markup=kb_yes_or_no)
        await BySell.Deposit_Q16.set()


@dp.message_handler(state=BySell.Deposit_Q16)
async def select_district(message: types.Message, state=FSMContext):
    filled_in_correctly = message.text

    if filled_in_correctly.lower() == 'да':
        answer = await state.get_data()
        await state.reset_state()
        await message.answer('Задаток отправлен', reply_markup=kb_main_menu)
        GoogleWork().google_add_row(sheet_id='1cybTRAnHDJ1gRiX5aY9XkD_84LXbMKccQPmjZn4YcCs',
                                    name_list='Задаток!',
                                    start_col='A',
                                    end_col='Q',
                                    array_data=[
                                        str(date.today()),
                                        answer['var_type_transaction'],
                                        message.from_user.full_name,
                                        answer['var_address'],
                                        answer['var_id'],
                                        answer['var_sum_deposit'],
                                        answer['var_date_start_contract'],
                                        answer['var_date_end_contract'],
                                        answer['var_total_cost'],
                                        answer['var_commission'],
                                        answer['var_buyer_name'],
                                        answer['var_buyer_phone'],
                                        answer['var_seller_name'],
                                        answer['var_seller_phone'],
                                        answer['var_informant'],
                                        answer['var_informant_phone'],
                                        answer['var_informant_reward']
                                    ])
    elif filled_in_correctly.lower() == 'нет':
        await state.reset_state()
        await message.answer('Вы отменили отправку', reply_markup=kb_main_menu)
    else:
        await message.answer('Отправлено не верное значение( Попробуйте снова')
