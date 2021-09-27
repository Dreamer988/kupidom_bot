from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default.step_back.kb_back import back

kb_completed_building = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Завершено'),
            KeyboardButton(text='Не завершено')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_completed_building_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Завершено'),
            KeyboardButton(text='Не завершено')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
