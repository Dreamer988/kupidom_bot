from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default.step_back.kb_back import back

kb_users_edit_manager_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Имя"),
            KeyboardButton(text="Фамилия"),
            KeyboardButton(text="Отчество")
        ],
        [
            KeyboardButton(text="Дата рождения"),
            KeyboardButton(text="Место проживания")
        ],
        [
            KeyboardButton(text="Номер телефона"),
            KeyboardButton(text="Телеграм ID")
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_users_edit_manager_menu_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Имя"),
            KeyboardButton(text="Фамилия"),
            KeyboardButton(text="Отчество")
        ],
        [
            KeyboardButton(text="Дата рождения"),
            KeyboardButton(text="Место проживания")
        ],
        [
            KeyboardButton(text="Номер телефона"),
            KeyboardButton(text="Телеграм ID")
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
