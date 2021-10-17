from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_calling = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Не могу дозвониться')
        ],
        [
            KeyboardButton(text='Активировать')
        ],
        [
            KeyboardButton(text='Изменить'),
            KeyboardButton(text='Удалить'),
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)

kb_calling_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Не могу дозвониться')
        ],
        [
            KeyboardButton(text='Активировать')
        ],
        [
            KeyboardButton(text='Изменить'),
            KeyboardButton(text='Удалить'),
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
).add(back)
