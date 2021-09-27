from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

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
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

kb_sewerage_back = ReplyKeyboardMarkup(
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
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
).add(back)
