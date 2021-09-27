from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_side_building = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Торец'),
            KeyboardButton(text='Середина')
        ],
        [
            KeyboardButton(text='Цокольный этаж'),
            KeyboardButton(text='На первом этаже')
        ],
        [
            KeyboardButton(text='Один этаж ком.помещения'),
            KeyboardButton(text='В подвале')
        ],
        [
            KeyboardButton(text='Отдельно стоящее'),
            KeyboardButton(text='Пристройка'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_side_building_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Торец'),
            KeyboardButton(text='Середина')
        ],
        [
            KeyboardButton(text='Цокольный этаж'),
            KeyboardButton(text='На первом этаже')
        ],
        [
            KeyboardButton(text='Один этаж ком.помещения'),
            KeyboardButton(text='В подвале')
        ],
        [
            KeyboardButton(text='Отдельно стоящее'),
            KeyboardButton(text='Пристройка'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
