from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_entrance = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Светлый'),
            KeyboardButton(text='Тёмный')
        ],
        [
            KeyboardButton(text='С ремонтом'),
            KeyboardButton(text='Без ремонта')
        ],
        [
            KeyboardButton(text='Большой пролёт'),
        ],
        [
            KeyboardButton(text='Не приятный запах'),
        ],
        [
            KeyboardButton(text='Назад ⬅️')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
