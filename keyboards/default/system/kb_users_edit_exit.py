from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default.step_back.kb_back import back

kb_users_edit_exit = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Главное меню"),
            KeyboardButton(text="Изменить ещё")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_users_edit_exit_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Главное меню"),
            KeyboardButton(text="Изменить ещё")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
