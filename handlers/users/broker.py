import re

from aiogram import types
from aiogram.dispatcher import FSMContext

from filters.is_phone import IsPhone
from google_work.google_work import GoogleWork
from keyboards.default.send_by_commerce import kb_yes_or_no, kb_main_menu
from loader import dp
from states import MenuState


def broker_number_decorator(number):
    broker_number = re.findall(r'\d+', number)  # Находим только числа через регулярные выражения
    broker_number = ''.join(broker_number)  # Объединяем списки с числами
    broker_number = f'998{broker_number[-9:]}'  # Выбираем 9 чисел с правой стороны и добавляем код страны
    return broker_number  # Возвращаем отформатированный номер телфона


@dp.message_handler(IsPhone(), state=MenuState.Broker)
async def select_by_sell(message: types.Message, state=FSMContext):
    broker_correct_number = broker_number_decorator(number=message.text)

    await state.update_data(var_broker_correct_number=broker_correct_number)
    await message.answer(f"Все заполнил(-а) правильно ?", reply_markup=kb_yes_or_no)
    await MenuState.Broker_Q1.set()


# Состояние MenuState.Broker_Q1 -->  Все заполнил(-а) правильно ?
@dp.message_handler(state=MenuState.Broker_Q1)
async def select_district(message: types.Message, state=FSMContext):
    filled_in_correctly = message.text

    if filled_in_correctly.lower() == 'да':
        answer = await state.get_data()
        await state.reset_state()
        await message.answer('Маклер добавлен в базу)', reply_markup=kb_main_menu)
        GoogleWork().google_add_row(sheet_id='1o71IQm9tcRyDcYVApTig0Xx6zmEGv6lJq8c401lWW6c',
                                    name_list='Маклера',
                                    array_data=[answer['var_broker_correct_number']])
    elif filled_in_correctly.lower() == 'нет':
        await state.reset_state()
        await message.answer('Вы отменили отправку', reply_markup=kb_main_menu)
    else:
        await message.answer('Отправлено не верное значение( Попробуйте снова')
