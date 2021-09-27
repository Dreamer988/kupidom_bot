from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.default.system import kb_users_add, kb_users_delete, kb_users_edit, kb_users_show
from loader import dp
from states import SystemState


@dp.message_handler(Text(equals='Добавить'), state=SystemState.UserMenu)
async def verification_password(message: types.Message):
    await message.answer('Кого будем добавлять ?', reply_markup=kb_users_add)
    await SystemState.UserAdd.set()


@dp.message_handler(Text(equals='Удалить'), state=SystemState.UserMenu)
async def verification_password(message: types.Message):
    await message.answer('Кого будем удалять ?', reply_markup=kb_users_delete)
    await SystemState.UserDelete.set()


@dp.message_handler(Text(equals='Изменить'), state=SystemState.UserMenu)
async def verification_password(message: types.Message):
    await message.answer('Кого будем изменять ?', reply_markup=kb_users_edit)
    await SystemState.UserEdit.set()


@dp.message_handler(Text(equals='Просмотреть'), state=SystemState.UserMenu)
async def verification_password(message: types.Message):
    await message.answer('Кого будем смотреть ?', reply_markup=kb_users_show)
    await SystemState.UserShow.set()
