from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
kb_type_of_property = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Квартиры"),
            KeyboardButton(text="Дома")
        ],
        [
            KeyboardButton(text="Коммерция")
        ],
        [
            KeyboardButton(text="Аренда Квартиры"),
            KeyboardButton(text="Аренда Дома")
        ],
        [
            KeyboardButton(text="Аренда Коммерция")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

