from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
kb_type_of_property = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Квартира"),
            KeyboardButton(text="Дом")
        ],
        [
            KeyboardButton(text="Коммерция")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

