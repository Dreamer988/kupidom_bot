from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_toilet = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Раздельный'),
            KeyboardButton(text='Совмещенный')
        ],
        [
            KeyboardButton(text='2 и более')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_toilet_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Раздельный'),
            KeyboardButton(text='Совмещенный')
        ],
        [
            KeyboardButton(text='2 и более')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
