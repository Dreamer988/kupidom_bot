from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_furniture = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Да'),
            KeyboardButton(text='Нет')
        ],
        [
            KeyboardButton(text='Частично')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)