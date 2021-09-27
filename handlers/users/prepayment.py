from datetime import date

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from filters.is_digit import IsDigit
from google_work.google_work import GoogleWork
from keyboards.default.send_by_apartment import kb_main_menu, kb_yes_or_no
from keyboards.default.by_sell import kb_currency
from keyboards.default.step_back import kb_back
from loader import dp
from states import BySell


@dp.message_handler(IsDigit(), state=BySell.Prepayment_Q1)
async def set_prepayment(message: types.Message, state=FSMContext):
    sum_prepayment = message.text
    await state.update_data(var_sum_prepayment=sum_prepayment)
    await message.answer('Выберите валюту в которой был взят аванс',
                         reply_markup=kb_currency)
    await BySell.Prepayment_Q2.set()


@dp.message_handler(state=BySell.Prepayment_Q2)
async def set_prepayment(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Prepayment_Q1.set()
        await message.answer('Укажите сумму взятого вами аванса',
                             reply_markup=ReplyKeyboardRemove())
    else:
        currency_prepayment = message.text
        await state.update_data(var_currency_prepayment=currency_prepayment)
        await message.answer('Укажите дату получения аванса \n(Пример : 30.01.2020)',
                             reply_markup=kb_back)
        await BySell.Prepayment_Q3.set()


@dp.message_handler(state=BySell.Prepayment_Q3)
async def select_district(message: types.Message, state=FSMContext):
    if message.text == 'Назад ⬅️':
        await BySell.Prepayment_Q2.set()
        await message.answer('Выберите валюту в которой был взят аванс',
                             reply_markup=kb_back)
    else:
        date_prepayment = message.text
        await state.update_data(var_date_prepayment=date_prepayment)

        await message.answer(f"Все заполнил(-а) правильно ?", reply_markup=kb_yes_or_no)
        await BySell.Prepayment_Q4.set()


@dp.message_handler(state=BySell.Prepayment_Q4)
async def select_district(message: types.Message, state=FSMContext):
    filled_in_correctly = message.text

    if filled_in_correctly.lower() == 'да':
        answer = await state.get_data()
        await state.reset_state()
        await message.answer('Аванс отправлен', reply_markup=kb_main_menu)
        GoogleWork().google_add_row(sheet_id='1cybTRAnHDJ1gRiX5aY9XkD_84LXbMKccQPmjZn4YcCs',
                                    name_list='Аванс',
                                    array_data=[
                                        str(date.today()),
                                        message.from_user.full_name,
                                        answer['var_sum_prepayment'],
                                        answer['var_currency_prepayment'],
                                        answer['var_date_prepayment']
                                    ])
    elif filled_in_correctly.lower() == 'нет':
        await state.reset_state()
        await message.answer('Вы отменили отправку', reply_markup=kb_main_menu)
    else:
        await message.answer('Отправлено не верное значение( Попробуйте снова')
