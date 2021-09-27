from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

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

kb_menu_by_sell_back = ReplyKeyboardMarkup(
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
).add(back)
