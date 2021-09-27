from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
kb_system_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Пользователи"),
            KeyboardButton(text="OLX")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

