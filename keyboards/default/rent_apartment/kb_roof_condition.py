from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_roof_condition = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Новая'),
            KeyboardButton(text='Старая')
        ],
        [
            KeyboardButton(text='Течёт'),
            KeyboardButton(text='Не последний этаж')
        ],
        [
            KeyboardButton(text='Назад ⬅️')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
