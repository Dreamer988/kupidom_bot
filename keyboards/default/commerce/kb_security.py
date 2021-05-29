from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_security = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Закрытая территория'),
            KeyboardButton(text='Видеонаблюдение')
        ],
        [
            KeyboardButton(text='Решетки на окнах'),
            KeyboardButton(text='Проходной двор')
        ],
        [
            KeyboardButton(text='Высокий забор с собакой'),
            KeyboardButton(text='Круглосуточная охрана')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
