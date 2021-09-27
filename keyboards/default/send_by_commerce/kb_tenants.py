from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_tenants = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Есть'),
            KeyboardButton(text='Нету')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_tenants_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Есть'),
            KeyboardButton(text='Нету')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
