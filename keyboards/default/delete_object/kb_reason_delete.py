from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default.step_back.kb_back import back

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

kb_reason_delete_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Объект продан"),
            KeyboardButton(text="Передумали продавать")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
