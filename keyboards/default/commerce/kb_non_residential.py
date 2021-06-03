from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_non_residential = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Да'),
            KeyboardButton(text='Нет')
        ],
        [
            KeyboardButton(text='Переведут после задатка'),
        ],
        [
            KeyboardButton(text='Назад ⬅️')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
