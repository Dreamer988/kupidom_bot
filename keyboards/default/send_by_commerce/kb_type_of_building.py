from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default.step_back.kb_back import back

kb_type_of_building = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Кирпич'),
            KeyboardButton(text='Панель')
        ],
        [
            KeyboardButton(text='Монолит'),
            KeyboardButton(text='Керамзит'),
        ],
        [
            KeyboardButton(text='Блочный'),
            KeyboardButton(text='Контейнер'),
        ],
        [
            KeyboardButton(text='Шлакоблок'),
            KeyboardButton(text='Сендвич панель'),
        ],
        [
            KeyboardButton(text='Стекляшка'),
            KeyboardButton(text='Пахса'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_type_of_building_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Кирпич'),
            KeyboardButton(text='Панель')
        ],
        [
            KeyboardButton(text='Монолит'),
            KeyboardButton(text='Керамзит'),
        ],
        [
            KeyboardButton(text='Блочный'),
            KeyboardButton(text='Контейнер'),
        ],
        [
            KeyboardButton(text='Шлакоблок'),
            KeyboardButton(text='Сендвич панель'),
        ],
        [
            KeyboardButton(text='Стекляшка'),
            KeyboardButton(text='Пахса'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
