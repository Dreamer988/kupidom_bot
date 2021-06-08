from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

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
        ],
        [
            KeyboardButton(text='Назад ⬅️')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)