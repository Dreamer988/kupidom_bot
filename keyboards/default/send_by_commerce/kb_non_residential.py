from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default.step_back.kb_back import back

kb_non_residential = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Да'),
            KeyboardButton(text='Нет')
        ],
        [
            KeyboardButton(text='Переведут после задатка'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_non_residential_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Да'),
            KeyboardButton(text='Нет')
        ],
        [
            KeyboardButton(text='Переведут после задатка'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
