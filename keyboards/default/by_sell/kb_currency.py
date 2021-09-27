from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_currency = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='$'),
            KeyboardButton(text='som'),
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)

kb_currency_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='$'),
            KeyboardButton(text='som'),
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
).add(back)
