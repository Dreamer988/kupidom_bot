from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_olx_next = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Продолжить'),
            KeyboardButton(text='Главное меню')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_olx_next_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Продолжить'),
            KeyboardButton(text='Главное меню')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
