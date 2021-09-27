from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default.step_back.kb_back import back

kb_users = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Добавить"),
            KeyboardButton(text="Удалить")
        ],
        [
            KeyboardButton(text="Изменить"),
            KeyboardButton(text="Просмотреть")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_users_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Добавить"),
            KeyboardButton(text="Удалить")
        ],
        [
            KeyboardButton(text="Изменить"),
            KeyboardButton(text="Просмотреть")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)