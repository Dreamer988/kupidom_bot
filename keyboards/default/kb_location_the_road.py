from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_location_the_road = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='1 ряд'),
            KeyboardButton(text='2 ряд'),
            KeyboardButton(text='3 ряд'),
        ],
        [
            KeyboardButton(text='Вдоль дороги')
        ],
        [
            KeyboardButton(text='Торцом к дороге')
        ],
        [
            KeyboardButton(text='Внутри района (квартала)')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)