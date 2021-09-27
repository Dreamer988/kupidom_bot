from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_type_parking = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Собственная'),
            KeyboardButton(text='На несколько машин')
        ],
        [
            KeyboardButton(text='Прилегающая общая'),
            KeyboardButton(text='В пешей доступности')
        ],
        [
            KeyboardButton(text='Нет')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_type_parking_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Собственная'),
            KeyboardButton(text='На несколько машин')
        ],
        [
            KeyboardButton(text='Прилегающая общая'),
            KeyboardButton(text='В пешей доступности')
        ],
        [
            KeyboardButton(text='Нет')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
