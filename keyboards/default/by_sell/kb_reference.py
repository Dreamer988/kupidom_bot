from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_reference = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Да'),
            KeyboardButton(text='Нет')
        ],
        [
            KeyboardButton(text='Частично')
        ],
        [
            KeyboardButton(text='Назад ⬅️')

        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)
