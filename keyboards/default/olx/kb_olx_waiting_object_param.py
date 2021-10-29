from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default.step_back.kb_back import back

kb_olx_waiting_object_param = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Поиск по номеру")
        ],
        [
            KeyboardButton(text="Взял(-а)"),
            KeyboardButton(text="Продан")
        ],
        [
            KeyboardButton(text="Пропустить"),
            KeyboardButton(text="Главное меню")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_olx_waiting_object_param_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Поиск по номеру")
        ],
        [
            KeyboardButton(text="Взял(-а)"),
            KeyboardButton(text="Продан")
        ],
        [
            KeyboardButton(text="Пропустить"),
            KeyboardButton(text="Главное меню")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
