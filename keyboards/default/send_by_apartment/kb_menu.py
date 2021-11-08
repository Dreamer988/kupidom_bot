from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

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
            KeyboardButton(text="Добавить"),

        ],
        [
            KeyboardButton(text="Удалить"),
            KeyboardButton(text="Изменить"),
            KeyboardButton(text="Активировать")
        ],
        [
            KeyboardButton(text="Добавить фото"),
            KeyboardButton(text="Горящий объект")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
