from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_roof_condition = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Новая'),
            KeyboardButton(text='Старая')
        ],
        [
            KeyboardButton(text='Течёт'),
            KeyboardButton(text='Не последний этаж')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_roof_condition_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Новая'),
            KeyboardButton(text='Старая')
        ],
        [
            KeyboardButton(text='Течёт'),
            KeyboardButton(text='Не последний этаж')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
