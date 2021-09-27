from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_infrastructure = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Дет.сад'),
            KeyboardButton(text='Остановка')
        ],
        [
            KeyboardButton(text='Больница'),
            KeyboardButton(text='Торговый центр')
        ],
        [
            KeyboardButton(text='Школа'),
            KeyboardButton(text='Парк')
        ],
        [
            KeyboardButton(text='Кафе'),
            KeyboardButton(text='Магазин')
        ],
        [
            KeyboardButton(text='Готово ✅')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_infrastructure_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Дет.сад'),
            KeyboardButton(text='Остановка')
        ],
        [
            KeyboardButton(text='Больница'),
            KeyboardButton(text='Торговый центр')
        ],
        [
            KeyboardButton(text='Школа'),
            KeyboardButton(text='Парк')
        ],
        [
            KeyboardButton(text='Кафе'),
            KeyboardButton(text='Магазин')
        ],
        [
            KeyboardButton(text='Готово ✅')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
