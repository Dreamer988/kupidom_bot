import logging

from aiogram import Dispatcher

from data.config import user_admin


async def on_startup_notify(dp: Dispatcher):
    admins = user_admin()
    for admin in admins:
        try:
            await dp.bot.send_message(admin, "Бот Запущен и готов к работе")

        except Exception as err:
            logging.exception(err)
