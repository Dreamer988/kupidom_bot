from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_freestanding = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Отдельно стоящее'),
            KeyboardButton(text='Не отдельно стоящее')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_freestanding_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Отдельно стоящее'),
            KeyboardButton(text='Не отдельно стоящее')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
