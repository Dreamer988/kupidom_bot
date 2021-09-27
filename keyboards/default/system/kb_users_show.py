from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default.step_back.kb_back import back

kb_users_show = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Агентов"),
            KeyboardButton(text="Менеджеров")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_users_show_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Агентов"),
            KeyboardButton(text="Менеджеров")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
