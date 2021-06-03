from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_system_heating = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Автономное'),
            KeyboardButton(text='Городское')
        ],
        [
            KeyboardButton(text='Нету'),
        ],
        [
            KeyboardButton(text='Назад ⬅️')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
