from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

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
        ],
        [
            KeyboardButton(text='Назад ⬅️')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)