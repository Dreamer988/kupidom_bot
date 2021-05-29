from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_completed_building = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Завершено'),
            KeyboardButton(text='Не завершено')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)