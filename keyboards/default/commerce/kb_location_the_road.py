from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_location_the_road = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Вдоль дороги'),
            KeyboardButton(text='Торцом к дороге'),
        ],
        [
            KeyboardButton(text='Внутри района (квартала)')
        ],
        [
            KeyboardButton(text='Махалля'),
            KeyboardButton(text='Тупик')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)