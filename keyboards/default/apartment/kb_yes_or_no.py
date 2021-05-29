from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_yes_or_no = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Да'),
            KeyboardButton(text='Нет')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
