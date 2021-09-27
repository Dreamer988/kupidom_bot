from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_distance_to_metro = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Менее 250 (м)'),
            KeyboardButton(text='От 250 (м) до 500 (м)')
        ],
        [
            KeyboardButton(text='От 500 (м) до 1000 (м)'),
            KeyboardButton(text='От 1000 (м) до 2000 (м)')
        ],
        [
            KeyboardButton(text='Более 2000 (м)')
        ],
        [
            KeyboardButton(text='Нету')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_distance_to_metro_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Менее 250 (м)'),
            KeyboardButton(text='От 250 (м) до 500 (м)')
        ],
        [
            KeyboardButton(text='От 500 (м) до 1000 (м)'),
            KeyboardButton(text='От 1000 (м) до 2000 (м)')
        ],
        [
            KeyboardButton(text='Более 2000 (м)')
        ],
        [
            KeyboardButton(text='Нету')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
