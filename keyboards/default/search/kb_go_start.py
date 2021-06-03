from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
kb_go_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Перейти в главное меню')
        ],
        [
            KeyboardButton(text='Повторить запрос')
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)