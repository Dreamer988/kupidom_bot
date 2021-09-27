from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default.step_back.kb_back import back

kb_type_of_layout = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="76 серия"),
            KeyboardButton(text="77 серия")
        ],
        [
            KeyboardButton(text="Банковская"),
            KeyboardButton(text="Высокопотолочная"),
        ],
        [
            KeyboardButton(text="Галерейная"),
            KeyboardButton(text="Грузинская"),
        ],
        [
            KeyboardButton(text="Казахская"),
            KeyboardButton(text="Ленинградская"),
        ],
        [
            KeyboardButton(text="Монолит"),
            KeyboardButton(text="Московская"),
        ],
        [
            KeyboardButton(text="Новостройка"),
            KeyboardButton(text="Общежитие"),
        ],
        [
            KeyboardButton(text="Пентхаус"),
            KeyboardButton(text="Специальная"),
        ],
        [
            KeyboardButton(text="Улучшенная"),
            KeyboardButton(text="Французская"),
        ],
        [
            KeyboardButton(text="Хрущевка"),
            KeyboardButton(text="Экспериментальная"),
        ],
        [
            KeyboardButton(text="Японская"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_type_of_layout_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="76 серия"),
            KeyboardButton(text="77 серия")
        ],
        [
            KeyboardButton(text="Банковская"),
            KeyboardButton(text="Высокопотолочная"),
        ],
        [
            KeyboardButton(text="Галерейная"),
            KeyboardButton(text="Грузинская"),
        ],
        [
            KeyboardButton(text="Казахская"),
            KeyboardButton(text="Ленинградская"),
        ],
        [
            KeyboardButton(text="Монолит"),
            KeyboardButton(text="Московская"),
        ],
        [
            KeyboardButton(text="Новостройка"),
            KeyboardButton(text="Общежитие"),
        ],
        [
            KeyboardButton(text="Пентхаус"),
            KeyboardButton(text="Специальная"),
        ],
        [
            KeyboardButton(text="Улучшенная"),
            KeyboardButton(text="Французская"),
        ],
        [
            KeyboardButton(text="Хрущевка"),
            KeyboardButton(text="Экспериментальная"),
        ],
        [
            KeyboardButton(text="Японская"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
