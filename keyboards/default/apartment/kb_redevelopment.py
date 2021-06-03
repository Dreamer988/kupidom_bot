from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_redevelopment = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Да'),
            KeyboardButton(text='Нет')
        ],
        [
            KeyboardButton(text='Кухня на балконе')
        ],
        [
            KeyboardButton(text='Назад ⬅️')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
