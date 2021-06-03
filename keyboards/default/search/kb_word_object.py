from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
kb_word_object = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='К'),
            KeyboardButton(text='Н'),
            KeyboardButton(text='И')
        ],
        [
            KeyboardButton(text='КМ'),
            KeyboardButton(text='Д')
        ],
        [
            KeyboardButton(text='АК'),
            KeyboardButton(text='АКМ'),
            KeyboardButton(text='АД')
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)