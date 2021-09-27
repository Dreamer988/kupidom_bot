from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_system_gas = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Да'),
            KeyboardButton(text='Нет')
        ],
        [
            KeyboardButton(text='Нет, но есть возможность подключить'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_system_gas_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Да'),
            KeyboardButton(text='Нет')
        ],
        [
            KeyboardButton(text='Нет, но есть возможность подключить'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
