from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_furniture = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Да'),
            KeyboardButton(text='Нет')
        ],
        [
            KeyboardButton(text='Частично')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_furniture_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Да'),
            KeyboardButton(text='Нет')
        ],
        [
            KeyboardButton(text='Частично')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
