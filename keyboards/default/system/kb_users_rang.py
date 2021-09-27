from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default.step_back.kb_back import back

kb_users_rang = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Стажер"),
            KeyboardButton(text="Агент"),
            KeyboardButton(text="Эксперт")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_users_rang_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Стажер"),
            KeyboardButton(text="Агент"),
            KeyboardButton(text="Эксперт")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
