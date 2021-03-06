from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_balcony_size = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='1 * 3'),
            KeyboardButton(text='1 * 7')
        ],
        [
            KeyboardButton(text='1.2 * 12'),
            KeyboardButton(text='1.5 * 3')
        ],
        [
            KeyboardButton(text='1.5 * 6'),
            KeyboardButton(text='2 * 3')
        ],
        [
            KeyboardButton(text='2 * 4'),
            KeyboardButton(text='2 * 6')
        ],
        [
            KeyboardButton(text='2 * 7'),
            KeyboardButton(text='2 * 9')
        ],
        [
            KeyboardButton(text='3 * 4'),
            KeyboardButton(text='3 * 6')
        ],
        [
            KeyboardButton(text='2 и более')
        ],
        [
            KeyboardButton(text='Г-образный (угловой)')
        ],
        [
            KeyboardButton(text='Подвесной балкон')
        ],
        [
            KeyboardButton(text='Нет')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_balcony_size_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='1 * 3'),
            KeyboardButton(text='1 * 7')
        ],
        [
            KeyboardButton(text='1.2 * 12'),
            KeyboardButton(text='1.5 * 3')
        ],
        [
            KeyboardButton(text='1.5 * 6'),
            KeyboardButton(text='2 * 3')
        ],
        [
            KeyboardButton(text='2 * 4'),
            KeyboardButton(text='2 * 6')
        ],
        [
            KeyboardButton(text='2 * 7'),
            KeyboardButton(text='2 * 9')
        ],
        [
            KeyboardButton(text='3 * 4'),
            KeyboardButton(text='3 * 6')
        ],
        [
            KeyboardButton(text='2 и более')
        ],
        [
            KeyboardButton(text='Г-образный (угловой)')
        ],
        [
            KeyboardButton(text='Подвесной балкон')
        ],
        [
            KeyboardButton(text='Нет')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
