from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

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
        ],
        [
            KeyboardButton(text='Назад ⬅️')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)