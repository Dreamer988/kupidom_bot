from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_video_review = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Да'),
            KeyboardButton(text='Нет'),
        ],
        [
            KeyboardButton(text='С двух сторон')
        ],
        [
            KeyboardButton(text='Назад ⬅️')
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)
