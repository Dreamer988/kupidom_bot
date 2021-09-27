from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_toilet = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='1'),
            KeyboardButton(text='2'),
            KeyboardButton(text='3 и более')
        ],
        [
            KeyboardButton(text='Нету')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_toilet_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='1'),
            KeyboardButton(text='2'),
            KeyboardButton(text='3 и более')
        ],
        [
            KeyboardButton(text='Нету')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
