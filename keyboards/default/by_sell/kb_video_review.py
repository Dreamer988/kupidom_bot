from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_video_review = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Да'),
            KeyboardButton(text='Нет'),
        ],
        [
            KeyboardButton(text='С двух сторон')
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)

kb_video_review_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Да'),
            KeyboardButton(text='Нет'),
        ],
        [
            KeyboardButton(text='С двух сторон')
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
).add(back)
