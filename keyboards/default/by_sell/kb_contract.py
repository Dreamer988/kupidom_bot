from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_contract = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Только договор'),
            KeyboardButton(text='Только ИКУ'),
        ],
        [
            KeyboardButton(text='Договори и ИКУ'),
            KeyboardButton(text='2 ИКУ'),
        ],
        [
            KeyboardButton(text='Нет')
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)

kb_contract_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Только договор'),
            KeyboardButton(text='Только ИКУ'),
        ],
        [
            KeyboardButton(text='Договори и ИКУ'),
            KeyboardButton(text='2 ИКУ'),
        ],
        [
            KeyboardButton(text='Нет')
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
).add(back)
