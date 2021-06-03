from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
kb_search_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Поиск по ID'),
            KeyboardButton(text='Поиск по номеру')
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)