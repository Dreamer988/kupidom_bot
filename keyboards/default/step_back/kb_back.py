from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

back = KeyboardButton('Назад ⬅️')
kb_back = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(back)
