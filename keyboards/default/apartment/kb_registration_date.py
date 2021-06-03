from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_registration_date = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Более 3-х лет'),
            KeyboardButton(text='Менее 3-х лет')
        ],
        [
            KeyboardButton(text='Назад ⬅️')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)