import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from filters.is_phone import IsPhone
from google_work.google_work import GoogleWork
from keyboards.default.send_by_apartment import kb_main_menu
from keyboards.default.search import kb_go_start
from loader import dp
from states import SearchState
from utils.binary_search import binary_search


def search_by_number(number):
    number_sheets = GoogleWork().google_get_values(sheet_id="1dNu9kjbn02aFVeQz3Uk8ivwW2QQUENApoDqbeM2LEl0",
                                                   name_list="Сборка номеров",
                                                   start_col="H",
                                                   end_col="M",
                                                   major_dimension="COLUMNS")

    broker_sheets = GoogleWork().google_get_values(sheet_id="1dNu9kjbn02aFVeQz3Uk8ivwW2QQUENApoDqbeM2LEl0",
                                                   name_list="Маклера",
                                                   start_col="A",
                                                   end_col="A",
                                                   major_dimension="COLUMNS")

    broker_number = '998' + str(number)
    number_point = binary_search(array=number_sheets[0], search_value=number)
    broker_point = binary_search(array=broker_sheets[0], search_value=broker_number)

    if broker_point:
        return 'Маклер'
    elif number_point:
        # Устанавливаем найденную позицию на 10 меньше, чтобы взять дубликаты номеров если они имеются
        number_point = number_point - 10
        # Проходимся по циклу из 21 повторений, чтобы взять дубликаты номеров если они имеются
        for num in range(21):
            number_point += 1
            objects = []
            if str(number) == number_sheets[0][number_point]:
                object_value = [
                    number_sheets[0][number_point],
                    number_sheets[1][number_point],
                    number_sheets[2][number_point],
                    number_sheets[3][number_point],
                    number_sheets[4][number_point],
                    number_sheets[5][number_point],
                ]
            else:
                continue

            objects.append(object_value)
            return objects
    else:
        return 'Нету в базе'


@dp.message_handler(IsPhone(), state=SearchState.SearchNumber_Q1)
async def search(message: types.Message, state=FSMContext):
    number_object = message.text
    # Получаем с помощью регулярного выражения только числа
    decor_number = re.findall(r'\d+', number_object)
    # Получаем 9 чисел с правой стороны
    decor_number = int(''.join(decor_number)[-9:])
    # Передаем отформатированный номер функции для бинарного поиска и получаем позицию номера в списке
    objects = search_by_number(decor_number)

    if objects == 'Маклер':
        await message.answer('Маклер')
    elif objects == 'Нету в базе':
        await message.answer('Номера нету в базе данных')
    else:
        await message.answer('Все варианты найденые по номеру телефона:')
        for object_value in objects:
            await message.answer(f"Номер телефона:  {object_value[0]}\n"
                                 f"ID:  {object_value[1]}\n"
                                 f"Квартал/Район:  {object_value[2]}\n"
                                 f"Ориентир:  {object_value[3]}\n"
                                 f"Квартира:  {object_value[4]}\n"
                                 f"Дом:  {object_value[5]}\n"
                                 )

    await message.answer(f"Выберите нужный вам вариант", reply_markup=kb_go_start)
    await SearchState.SearchNumber_Q2.set()


@dp.message_handler(Text(equals='Повторить запрос'), state=SearchState.SearchNumber_Q2)
async def go_to_start(message: types.Message, state=FSMContext):
    await message.answer('Введите номер телфона', reply_markup=ReplyKeyboardRemove())
    await SearchState.SearchNumber_Q1.set()


@dp.message_handler(Text(equals='Перейти в главное меню'), state=SearchState.SearchNumber_Q2)
async def go_to_start(message: types.Message, state=FSMContext):
    await message.answer('Что тебе нужно?',
                         reply_markup=kb_main_menu)
    await state.reset_state()
