from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

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