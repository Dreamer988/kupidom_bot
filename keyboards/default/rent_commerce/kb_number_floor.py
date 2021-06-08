from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_number_floor = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1"),
            KeyboardButton(text="2"),
            KeyboardButton(text="3"),
            KeyboardButton(text="4")
        ],
        [
            KeyboardButton(text="5"),
            KeyboardButton(text="6"),
            KeyboardButton(text="7"),
            KeyboardButton(text="8")
        ],
        [
            KeyboardButton(text="9"),
            KeyboardButton(text="10"),
            KeyboardButton(text="11"),
            KeyboardButton(text="12")
        ],
        [
            KeyboardButton(text="13"),
            KeyboardButton(text="14"),
            KeyboardButton(text="15"),
            KeyboardButton(text="16")
        ],
        [
            KeyboardButton(text="0")
        ],
        [
            KeyboardButton(text='Назад ⬅️')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)