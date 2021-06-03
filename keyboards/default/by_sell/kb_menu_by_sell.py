from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
kb_menu_by_sell = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Задаток'),
            KeyboardButton(text='Оформление')
        ],
        [
            KeyboardButton(text='Аванс')
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)