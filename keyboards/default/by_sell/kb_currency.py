from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
kb_currency = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='$'),
            KeyboardButton(text='som'),
        ],
        [
            KeyboardButton(text='Назад ⬅️')
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)