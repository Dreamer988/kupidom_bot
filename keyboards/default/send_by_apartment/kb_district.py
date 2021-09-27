from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from keyboards.default.step_back.kb_back import back

kb_district = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Алмазарский район'),
            KeyboardButton(text='Бектемирский район')
        ],
        [
            KeyboardButton(text='Мирабадский район'),
            KeyboardButton(text='Мирзо-Улугбекский район')
        ],
        [
            KeyboardButton(text='Сергелийский район'),
            KeyboardButton(text='Учтепинский район')
        ],
        [
            KeyboardButton(text='Чиланзарский район'),
            KeyboardButton(text='Шайхантахурский район')
        ],
        [
            KeyboardButton(text='Юнусабадский район'),
            KeyboardButton(text='Яккасарайский район')
        ],
        [
            KeyboardButton(text='Янгихаётский район'),
            KeyboardButton(text='Яшнабадский район')
        ],
        [
            KeyboardButton(text='Зангиатинский район'),
        ],
        [
            KeyboardButton(text='Зангиатинский район, Сергели'),
        ],
        [
            KeyboardButton(text='Зангиатинский район, Назарбек')
        ],
        [
            KeyboardButton(text='Ташкентская область')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

kb_district_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Алмазарский район'),
            KeyboardButton(text='Бектемирский район')
        ],
        [
            KeyboardButton(text='Мирабадский район'),
            KeyboardButton(text='Мирзо-Улугбекский район')
        ],
        [
            KeyboardButton(text='Сергелийский район'),
            KeyboardButton(text='Учтепинский район')
        ],
        [
            KeyboardButton(text='Чиланзарский район'),
            KeyboardButton(text='Шайхантахурский район')
        ],
        [
            KeyboardButton(text='Юнусабадский район'),
            KeyboardButton(text='Яккасарайский район')
        ],
        [
            KeyboardButton(text='Янгихаётский район'),
            KeyboardButton(text='Яшнабадский район')
        ],
        [
            KeyboardButton(text='Зангиатинский район'),
        ],
        [
            KeyboardButton(text='Зангиатинский район, Сергели'),
        ],
        [
            KeyboardButton(text='Зангиатинский район, Назарбек')
        ],
        [
            KeyboardButton(text='Ташкентская область')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
).add(back)
