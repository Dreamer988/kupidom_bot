from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_registration_date = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Более 3-х лет'),
            KeyboardButton(text='Менее 3-х лет')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_registration_date_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Более 3-х лет'),
            KeyboardButton(text='Менее 3-х лет')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
