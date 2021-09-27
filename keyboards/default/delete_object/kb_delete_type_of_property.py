from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default.step_back.kb_back import back

kb_delete_type_of_property = ReplyKeyboardMarkup(
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

kb_delete_type_of_property_back = ReplyKeyboardMarkup(
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
).add(back)
