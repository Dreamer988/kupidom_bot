from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

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
        ],
        [
            KeyboardButton(text='Назад ⬅️')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)