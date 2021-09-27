from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_apartment_layout = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Зеркальная'),
            KeyboardButton(text='Коробка')
        ],
        [
            KeyboardButton(text='Малогабаритная'),
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
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_apartment_layout_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Зеркальная'),
            KeyboardButton(text='Коробка')
        ],
        [
            KeyboardButton(text='Малогабаритная'),
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
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
