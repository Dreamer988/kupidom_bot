from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_tenants = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Есть'),
            KeyboardButton(text='Нету')
        ],
        [
            KeyboardButton(text='Назад ⬅️')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
