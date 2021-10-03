from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_business = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рабочий бизнес с фирмой'),
        ],
        [
            KeyboardButton(text='Нет')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_business_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рабочий бизнес с фирмой'),
        ],
        [
            KeyboardButton(text='Нет')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
