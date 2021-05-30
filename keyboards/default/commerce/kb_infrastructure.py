from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_infrastructure = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Дет.сад'),
            KeyboardButton(text='Остановка')
        ],
        [
            KeyboardButton(text='Готово ✅')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)