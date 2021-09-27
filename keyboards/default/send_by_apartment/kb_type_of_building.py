from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default.step_back.kb_back import back

kb_type_of_building = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Кирпич'),
            KeyboardButton(text='Панель')
        ],
        [
            KeyboardButton(text='Монолит'),
            KeyboardButton(text='Деревянный'),
        ],
        [
            KeyboardButton(text='Блочный'),
            KeyboardButton(text='Керамзит'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_type_of_building_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Кирпич'),
            KeyboardButton(text='Панель')
        ],
        [
            KeyboardButton(text='Монолит'),
            KeyboardButton(text='Деревянный'),
        ],
        [
            KeyboardButton(text='Блочный'),
            KeyboardButton(text='Керамзит'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
