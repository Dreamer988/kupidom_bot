from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_redevelopment = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Да'),
            KeyboardButton(text='Нет')
        ],
        [
            KeyboardButton(text='Кухня на балконе')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_redevelopment_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Да'),
            KeyboardButton(text='Нет')
        ],
        [
            KeyboardButton(text='Кухня на балконе')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
