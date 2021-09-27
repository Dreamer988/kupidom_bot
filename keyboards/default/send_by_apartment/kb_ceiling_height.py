from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default.step_back.kb_back import back

kb_ceiling_height = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="260"),
            KeyboardButton(text="270"),
            KeyboardButton(text="280")
        ],
        [
            KeyboardButton(text="290"),
            KeyboardButton(text="300"),
            KeyboardButton(text="320")
        ],
        [
            KeyboardButton(text="340"),
            KeyboardButton(text="360"),
            KeyboardButton(text="380")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_ceiling_height_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="260"),
            KeyboardButton(text="270"),
            KeyboardButton(text="280")
        ],
        [
            KeyboardButton(text="290"),
            KeyboardButton(text="300"),
            KeyboardButton(text="320")
        ],
        [
            KeyboardButton(text="340"),
            KeyboardButton(text="360"),
            KeyboardButton(text="380")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
