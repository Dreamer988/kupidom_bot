from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

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
        ],
        [
            KeyboardButton(text='Назад ⬅️')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)