from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_type_transaction = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Купля - Продажа'),
            KeyboardButton(text='Аренда'),
        ],
        [
            KeyboardButton(text='ИКУ')
        ],
        [
            KeyboardButton(text='Назад ⬅️')
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)
