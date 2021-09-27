from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

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

kb_security_back = ReplyKeyboardMarkup(
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
).add(back)
