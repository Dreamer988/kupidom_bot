from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_traffic_level = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Низкая'),
            KeyboardButton(text='Средняя'),
            KeyboardButton(text='Высокая')
        ],
        [
            KeyboardButton(text='Оживленная проезжая часть'),
        ],
        [
            KeyboardButton(text='Оживленная проезжая часть и высокая проходимость'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_traffic_level_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Низкая'),
            KeyboardButton(text='Средняя'),
            KeyboardButton(text='Высокая')
        ],
        [
            KeyboardButton(text='Оживленная проезжая часть'),
        ],
        [
            KeyboardButton(text='Оживленная проезжая часть и высокая проходимость'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
