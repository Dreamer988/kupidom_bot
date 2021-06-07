from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_prepayment = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1 месяц"),
            KeyboardButton(text="2 месяца"),
        ],
        [
            KeyboardButton(text="3 месяца"),
            KeyboardButton(text="4 месяца"),
        ],
        [
            KeyboardButton(text="5 месяцев"),
            KeyboardButton(text="6 месяцев"),
        ],
        [
            KeyboardButton(text='Назад ⬅️')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)