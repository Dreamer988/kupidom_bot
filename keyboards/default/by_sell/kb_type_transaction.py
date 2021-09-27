from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_type_transaction = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Купля - Продажа'),
            KeyboardButton(text='Аренда'),
        ],
        [
            KeyboardButton(text='ИКУ')
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)

kb_type_transaction_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Купля - Продажа'),
            KeyboardButton(text='Аренда'),
        ],
        [
            KeyboardButton(text='ИКУ')
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
).add(back)
