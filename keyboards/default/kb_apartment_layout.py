from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_apartment_layout = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Зеркальная'),
            KeyboardButton(text='Коробка')
        ],
        [
            KeyboardButton(text='Малосемейная'),
            KeyboardButton(text='Многоуровневая')
        ],
        [
            KeyboardButton(text='Однокомнатная'),
            KeyboardButton(text='Параллельная')
        ],
        [
            KeyboardButton(text='Пентхаус'),
            KeyboardButton(text='Раздельная')
        ],
        [
            KeyboardButton(text='Свободная'),
            KeyboardButton(text='Смежная')
        ],
        [
            KeyboardButton(text='Смежно - раздельная'),
            KeyboardButton(text='Студия')
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)