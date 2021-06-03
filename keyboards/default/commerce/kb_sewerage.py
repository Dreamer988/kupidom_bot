from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_sewerage = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Центральное водоснабжение'),
            KeyboardButton(text='Центральное водоснабжение и канализация')
        ],
        [
            KeyboardButton(text='Своя скважина'),
            KeyboardButton(text='Своя скважина и канализация')
        ],
        [
            KeyboardButton(text='Сливная яма и ЦВС'),
            KeyboardButton(text='Сливная яма и скважина')
        ],
        [
            KeyboardButton(text='Есть возможность подключить')
        ],
        [
            KeyboardButton(text='Назад ⬅️')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
