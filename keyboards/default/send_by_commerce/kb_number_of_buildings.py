from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_number_of_buildings = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='1'),
            KeyboardButton(text='2'),
            KeyboardButton(text='3'),
            KeyboardButton(text='4')
        ],
        [
            KeyboardButton(text='5 и более')
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)

kb_number_of_buildings_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='1'),
            KeyboardButton(text='2'),
            KeyboardButton(text='3'),
            KeyboardButton(text='4')
        ],
        [
            KeyboardButton(text='5 и более')
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
).add(back)
