from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default.step_back.kb_back import back

kb_olx_object = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Взял(-а)"),
            KeyboardButton(text="Продан")
        ],
        [
            KeyboardButton(text="Не могу дозвониться"),
            KeyboardButton(text="Вне зоны доступа")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_olx_object_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Взял(-а)"),
            KeyboardButton(text="Продан")
        ],
        [
            KeyboardButton(text="Не могу дозвониться"),
            KeyboardButton(text="Вне зоны доступа")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
