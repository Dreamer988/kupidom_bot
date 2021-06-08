from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_business = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рабочий бизнес'),
        ],
        [
            KeyboardButton(text='Рабочий бизнес с фирмой')
        ],
        [
            KeyboardButton(text='Назад ⬅️')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
