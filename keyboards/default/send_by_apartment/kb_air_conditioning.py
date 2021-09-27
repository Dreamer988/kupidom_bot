from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_air_conditioning = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Да'),
            KeyboardButton(text='Нет')
        ],
        [
            KeyboardButton(text='2 и более')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_air_conditioning_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Да'),
            KeyboardButton(text='Нет')
        ],
        [
            KeyboardButton(text='2 и более')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
