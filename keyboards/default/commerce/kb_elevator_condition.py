from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

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
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
