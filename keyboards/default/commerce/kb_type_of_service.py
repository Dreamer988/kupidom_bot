from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_type_of_service = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Продажа'),
            KeyboardButton(text='Аренда')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
