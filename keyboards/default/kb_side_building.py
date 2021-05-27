from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_side_building = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Торец'),
            KeyboardButton(text='Не торец')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)