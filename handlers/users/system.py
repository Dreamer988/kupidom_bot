from aiogram import types
from aiogram.dispatcher.filters import Text, Command
from aiogram.types import ReplyKeyboardMarkup

from filters.password_verification import PasswordVerification
from filters.user_access import UserAccess
from keyboards.default.system import kb_system_menu, kb_olx, kb_users
from loader import dp
from states import SystemState


@dp.message_handler(UserAccess(), commands=['system'], state='*')
async def system_menu(message: types.Message):
    await message.answer('Пожалуйста введите <b>пароль</b> чтобы продолжить ...', reply_markup=ReplyKeyboardMarkup())
    await SystemState.Start.set()


@dp.message_handler(PasswordVerification(), state=SystemState.Start)
async def verification_password(message: types.Message):
    await message.answer('Добро пожаловать в системную часть бота !')
    await message.answer('Выберите что вам нужно.', reply_markup=kb_system_menu)
    await SystemState.MainMenu.set()


@dp.message_handler(Text(equals='Пользователи'), state=SystemState.MainMenu)
async def verification_password(message: types.Message):
    await message.answer('Что вы хотите сделать?', reply_markup=kb_users)
    await SystemState.UserMenu.set()


@dp.message_handler(Text(equals='OLX'), state=SystemState.MainMenu)
async def verification_password(message: types.Message):
    await message.answer('Что вы хотите сделать?', reply_markup=kb_olx)
    await SystemState.OlxMenu.set()
