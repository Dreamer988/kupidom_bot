from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


kb_appointment = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Жилое под офис'),
            KeyboardButton(text='Нежилое под офис'),
            KeyboardButton(text='Недостройка')
        ],
        [
            KeyboardButton(text='Магазин'),
            KeyboardButton(text='Аптека'),
            KeyboardButton(text='Кафе'),
        ],
        [
            KeyboardButton(text='Клиника'),
            KeyboardButton(text='Салон красоты'),
            KeyboardButton(text='Автосервис/Автомойка')
        ],
        [
            KeyboardButton(text='Гостиница'),
            KeyboardButton(text='Коплекс'),
            KeyboardButton(text='База отдыха')
        ],
        [
            KeyboardButton(text='Учебный центр'),
            KeyboardButton(text='Нежилое под застрой')
        ],
        [
            KeyboardButton(text='Склады и производственные помещения')
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


