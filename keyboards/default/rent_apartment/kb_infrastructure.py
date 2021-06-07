from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

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
        ],
        [
            KeyboardButton(text='Назад ⬅️')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)