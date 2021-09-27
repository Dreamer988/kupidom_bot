from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default.step_back.kb_back import back

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
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_prepayment_back = ReplyKeyboardMarkup(
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
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
