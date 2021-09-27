from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

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
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_entrance_back = ReplyKeyboardMarkup(
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
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
