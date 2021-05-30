from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
kb_reason_delete = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Объект продан"),
            KeyboardButton(text="Передумали продавать")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

