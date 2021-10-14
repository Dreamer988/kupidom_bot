from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from filters.user_access import UserAccess
from keyboards.default.olx import kb_olx_new_or_waiting
from keyboards.default.send_by_apartment import kb_object_menu, kb_main_menu, kb_yes_or_no
from keyboards.default.by_sell import kb_menu_by_sell
from keyboards.default.search import kb_search_menu
from loader import dp
from states import MenuState


@dp.message_handler(UserAccess(), commands=['menu'], state='*')
async def bot_start(message: types.Message, state=FSMContext):
    await message.answer('Главное меню в вашем распоряжении',
                         reply_markup=kb_main_menu)
    await state.reset_state()


@dp.message_handler(Text(equals='Объект'), state=None)
async def get_menu(message: types.Message):
    await message.answer(f"Виберите одно из действий", reply_markup=kb_object_menu)
    await MenuState.Object.set()


@dp.message_handler(Text(equals='Купля - Продажа'), state=None)
async def get_menu(message: types.Message):
    await message.answer('Выберите раздел Купли-Продажи:', reply_markup=kb_menu_by_sell)
    await MenuState.BySell.set()


@dp.message_handler(Text(equals='Поиск'), state=None)
async def search(message: types.Message, state=FSMContext):
    await message.answer('Выберите', reply_markup=kb_search_menu)
    await MenuState.Search.set()


@dp.message_handler(Text(equals='Маклер'), state=None)
async def get_menu(message: types.Message):
    await message.answer(f"Введите номер телефона маклера", reply_markup=ReplyKeyboardRemove())
    await MenuState.Broker.set()


@dp.message_handler(Text(equals='OLX'), state=None)
async def get_menu(message: types.Message):
    await message.answer(f"Какой OLX вы хотите получить?", reply_markup=kb_olx_new_or_waiting)
    await MenuState.OLX.set()