from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default.step_back.kb_back import back

kb_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Объект")
        ],
        [
            KeyboardButton(text="Купля - Продажа")
        ],
        [
            KeyboardButton(text="Поиск"),
            KeyboardButton(text="Маклер")
        ],
        [
            KeyboardButton(text="OLX"),
            KeyboardButton(text="Обзвон")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_object_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Объект")
        ],
        [
            KeyboardButton(text="Купля - Продажа")
        ],
        [
            KeyboardButton(text="Поиск"),
            KeyboardButton(text="Маклер")
        ],
        [
            KeyboardButton(text="OLX"),
            KeyboardButton(text="Обзвон")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_object_menu_back = kb_object_menu.add(back)