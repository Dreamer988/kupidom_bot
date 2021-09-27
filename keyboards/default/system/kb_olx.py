from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default.step_back.kb_back import back

kb_olx = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Добавить")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_olx_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Добавить")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
