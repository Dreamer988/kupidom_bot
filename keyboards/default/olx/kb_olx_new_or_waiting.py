from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_olx_new_or_waiting = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Новый'),
            KeyboardButton(text='Ожидающий')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_olx_new_or_waiting_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Новый'),
            KeyboardButton(text='Ожидающий')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
