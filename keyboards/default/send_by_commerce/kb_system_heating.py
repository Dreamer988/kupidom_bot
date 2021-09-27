from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_system_heating = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Автономное'),
            KeyboardButton(text='Городское')
        ],
        [
            KeyboardButton(text='Нету'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_system_heating_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Автономное'),
            KeyboardButton(text='Городское')
        ],
        [
            KeyboardButton(text='Нету'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
