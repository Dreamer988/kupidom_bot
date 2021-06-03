from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
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
        ],
        [
            KeyboardButton(text='Назад ⬅️')
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)