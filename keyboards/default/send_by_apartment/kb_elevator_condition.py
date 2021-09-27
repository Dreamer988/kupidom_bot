from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_elevator_condition = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Новый'),
            KeyboardButton(text='Старый')
        ],
        [
            KeyboardButton(text='Чистый'),
            KeyboardButton(text='Грязный')
        ],
        [
            KeyboardButton(text='Нет'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_elevator_condition_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Новый'),
            KeyboardButton(text='Старый')
        ],
        [
            KeyboardButton(text='Чистый'),
            KeyboardButton(text='Грязный')
        ],
        [
            KeyboardButton(text='Нет'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
