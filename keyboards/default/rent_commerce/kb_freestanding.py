from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_freestanding = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Отдельно стоящее'),
            KeyboardButton(text='Не отдельно стоящее')
        ],
        [
            KeyboardButton(text='Назад ⬅️')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)