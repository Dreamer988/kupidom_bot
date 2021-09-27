from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

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

kb_side_building_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Торец'),
            KeyboardButton(text='Не торец')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
