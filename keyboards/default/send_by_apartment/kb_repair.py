from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_repair = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Авторский ремонт'),
            KeyboardButton(text='Без ремонта')
        ],
        [
            KeyboardButton(text='Евроремонт'),
            KeyboardButton(text='Капитальный ремонт')
        ],
        [
            KeyboardButton(text='Коробка'),
            KeyboardButton(text='Косметический ремонт')
        ],
        [
            KeyboardButton(text='Под снос'),
            KeyboardButton(text='Пред чистовая отделка')
        ],
        [
            KeyboardButton(text='Средний ремонт'),
            KeyboardButton(text='Требует ремонта')
        ],
        [
            KeyboardButton(text='Частичный ремонт'),
            KeyboardButton(text='Черновая отделка')
        ],
        [
            KeyboardButton(text='Чистая аккуратная')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_repair_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Авторский ремонт'),
            KeyboardButton(text='Без ремонта')
        ],
        [
            KeyboardButton(text='Евроремонт'),
            KeyboardButton(text='Капитальный ремонт')
        ],
        [
            KeyboardButton(text='Коробка'),
            KeyboardButton(text='Косметический ремонт')
        ],
        [
            KeyboardButton(text='Под снос'),
            KeyboardButton(text='Пред чистовая отделка')
        ],
        [
            KeyboardButton(text='Средний ремонт'),
            KeyboardButton(text='Требует ремонта')
        ],
        [
            KeyboardButton(text='Частичный ремонт'),
            KeyboardButton(text='Черновая отделка')
        ],
        [
            KeyboardButton(text='Чистая аккуратная')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
