from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_toilet = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Раздельный'),
            KeyboardButton(text='Совмещенный')
        ],
        [
            KeyboardButton(text='2 и более')
        ],
        [
            KeyboardButton(text='Назад ⬅️')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)