import logging

from aiogram import types

from data.config import user_access
from loader import dp


async def info_users_start_bot(message: types.Message):
    users = user_access()
    for user in users:
        try:
            await dp.bot.send_message(user,
                                      'Бот запущен и готов к работе!\nЕсли это сообщение '
                                      'вышло когда вы были в процессе работы с ботом, '
                                      'просим прощения но данные которые вы ввели не сохранились.'
                                      '\nЗаполните их заново')
        except Exception as err:
            logging.exception(err)
