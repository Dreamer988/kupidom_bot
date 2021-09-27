from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default.step_back.kb_back import back

kb_users_edit = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Агент"),
            KeyboardButton(text="Менеджер")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_users_edit_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Агент"),
            KeyboardButton(text="Менеджер")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
