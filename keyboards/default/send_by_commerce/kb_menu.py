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
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_object_menu_back = kb_object_menu.add(back)