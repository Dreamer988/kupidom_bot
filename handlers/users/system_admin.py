from aiogram import types
from aiogram.types import ReplyKeyboardMarkup
from aiogram.dispatcher import FSMContext

from filters.user_admin import UserAdmin
from states.AdminState import AdminState
from keyboards.default.system import kb_system_menu
from loader import dp


@dp.message_handler(UserAdmin(), commands='admin', state=None)
async def bot_start(message: types.Message, state=FSMContext):
    await message.answer(f'Привет, {message.from_user.full_name}!\nДобро пожаловать в админ панель КупиДом бота!')
    await message.answer('Что тебе нужно?',
                         reply_markup=kb_system_menu)
    await AdminState.first()


@dp.message_handler(text='Очистить чат с сотстоянием', state=AdminState.Q1)
async def bot_start(message: types.Message, state=FSMContext):
    await message.answer(f'Отправьте id пользователя у которого вы хотите почистить историю переписки',
                         reply_markup=ReplyKeyboardMarkup())
    await AdminState.next()


@dp.message_handler(state=AdminState.Q2)
async def bot_start(message: types.Message, state=FSMContext):
    msg = await dp.bot.get_chat(message.text)
    msg2 = await dp.bot.get_chat_member(message.text,message.text)
    msg3 = await dp.bot.get_updates()
    await message.answer(f'{msg} \n/////////////\n{msg2}\n/////////////\n{msg3}')
