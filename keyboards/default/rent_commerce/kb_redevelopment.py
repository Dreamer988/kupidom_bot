from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_redevelopment = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Перепланировка'),
            KeyboardButton(text='Пристройка')
        ],
        [
            KeyboardButton(text='Перепланировка + Пристройка')
        ],
        [
            KeyboardButton(text='Нет')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_redevelopment_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Перепланировка'),
            KeyboardButton(text='Пристройка')
        ],
        [
            KeyboardButton(text='Перепланировка + Пристройка')
        ],
        [
            KeyboardButton(text='Нет')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
