from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
kb_system_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Очистить чат с сотстоянием"),
            KeyboardButton(text="Диалог")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

