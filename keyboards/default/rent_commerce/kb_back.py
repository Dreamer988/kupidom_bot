from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Назад ⬅️')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)