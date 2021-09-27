from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_type_of_service = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Продажа'),
            KeyboardButton(text='Аренда')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

kb_type_of_service_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Продажа'),
            KeyboardButton(text='Аренда')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
).add(back)