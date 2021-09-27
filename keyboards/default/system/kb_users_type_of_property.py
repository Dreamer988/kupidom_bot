from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default.step_back.kb_back import back

kb_users_type_of_property = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Квартира"),
            KeyboardButton(text="Дом"),
            KeyboardButton(text="Коммерция")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_users_type_of_property_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Квартира"),
            KeyboardButton(text="Дом"),
            KeyboardButton(text="Коммерция")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
