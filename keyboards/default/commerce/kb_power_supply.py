from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_power_supply = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='220 Вольт'),
            KeyboardButton(text='380 Вольт')
        ],
        [
            KeyboardButton(text='Свой ТП'),
            KeyboardButton(text='Нет')
        ],
        [
            KeyboardButton(text='Нет, но есть возможеность подключить')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
