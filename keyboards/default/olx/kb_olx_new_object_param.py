from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default.step_back.kb_back import back

kb_olx_new_object_param = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ожидание")
        ],
        [
            KeyboardButton(text="Взял(-а)"),
            KeyboardButton(text="Продан")
        ],
        [
            KeyboardButton(text="Не лояльный"),
            KeyboardButton(text="Удалить")
        ],
        [
            KeyboardButton(text="Не мой участок"),
            KeyboardButton(text="Маклер")
        ],
        [
            KeyboardButton(text="Не могу дозвониться"),
            KeyboardButton(text="Вне зоны доступа")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_olx_new_object_param_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ожидание")
        ],
        [
            KeyboardButton(text="Взял(-а)"),
            KeyboardButton(text="Продан")
        ],
        [
            KeyboardButton(text="Не лояльный"),
            KeyboardButton(text="Удалить")
        ],
        [
            KeyboardButton(text="Не мой участок"),
            KeyboardButton(text="Маклер")
        ],
        [
            KeyboardButton(text="Не могу дозвониться"),
            KeyboardButton(text="Вне зоны доступа")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
