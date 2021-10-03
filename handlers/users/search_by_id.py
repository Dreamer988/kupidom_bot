import time

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from google_work.google_work import GoogleWork
from keyboards.default.send_by_apartment import kb_main_menu
from keyboards.default.search import kb_go_start, kb_word_object
from loader import dp
from sql.sql_query import SqlQuery
from states import SearchState


def verified_data_time(telegram_id):
    # Задаем лимиты в день и час
    limit_day = 33
    limit_hour = 11

    data_time = time.time()  # Время в секундах с 1970 года
    now_hour = int(data_time / 60 / 60)  # Преобразуем секунды в часы
    now_day = int(now_hour / 24)  # Преобразуем часы в дни

    # Получаем с БД информацию по данным таймера пользователя
    count_day = SqlQuery().get_column_by_param(
        table_name='bot_timer',
        get_column_name='count_day',
        search_column_name='telegram_id',
        search_value=telegram_id
    )
    count_hours = SqlQuery().get_column_by_param(
        table_name='bot_timer',
        get_column_name='count_hours',
        search_column_name='telegram_id',
        search_value=telegram_id
    )
    db_day = SqlQuery().get_column_by_param(
        table_name='bot_timer',
        get_column_name='day',
        search_column_name='telegram_id',
        search_value=telegram_id
    )
    db_hour = SqlQuery().get_column_by_param(
        table_name='bot_timer',
        get_column_name='hour',
        search_column_name='telegram_id',
        search_value=telegram_id
    )
    try:
        count_day = count_day[0][0]
        count_hours = count_hours[0][0]
        db_day = db_day[0][0]
        db_hour = db_hour[0][0]
    except:
        return 'Вы не агент! Вас нету в базе.'

    def verified_by_id(user_id):
        all_user_id = SqlQuery().get_column(table_name='bot_timer',
                                            get_column_name='telegram_id')
        all_user_id = all_user_id[0]
        for current_id in all_user_id:
            if current_id == user_id:
                return True
            else:
                continue
        return False

    def verified_by_date(user_id):
        if now_day > db_day:
            SqlQuery().edit_row(
                table_name='bot_timer',
                search_column_name='telegram_id',
                search_value=user_id,
                edit_param=[
                    f'count_day=0',
                    f'count_hours=0',
                    f'day={now_day}',
                    f'hour={now_hour}'
                ]
            )
            return True
        elif now_hour > db_hour:
            SqlQuery().edit_row(
                table_name='bot_timer',
                search_column_name='telegram_id',
                search_value=user_id,
                edit_param=[
                    f'count_hours=0',
                    f'hour={now_hour}'
                ]
            )
            return True
        else:
            return True

    def verified_by_limit():
        print(f"{count_day} > {limit_day}")
        print(f"{count_hours} > {limit_hour}")
        if int(count_day) > int(limit_day):
            return f'Вы привысили норму в день!\nНорма в день составляет {limit_day} шт.'
        elif int(count_hours) > int(limit_hour):
            return f'Вы привысили норму в час!\nНорма в час составляет {limit_hour} шт.'
        else:
            return True

    if verified_by_id(telegram_id) and verified_by_date(telegram_id) and verified_by_limit():
        return verified_by_limit()
    else:
        return False


def add_point(telegram_id):
    count_day = SqlQuery().get_column_by_param(
        table_name="bot_timer",
        get_column_name="count_day",
        search_column_name="telegram_id",
        search_value=telegram_id
    )
    count_hours = SqlQuery().get_column_by_param(
        table_name='bot_timer',
        get_column_name='count_hours',
        search_column_name='telegram_id',
        search_value=telegram_id
    )

    count_day = count_day[0][0]
    count_hours = count_hours[0][0]

    SqlQuery().edit_row(
        table_name="bot_timer",
        search_column_name="telegram_id",
        search_value=telegram_id,
        edit_param=[f"`count_day` = '{count_day + 1}'"])
    SqlQuery().edit_row(
        table_name="bot_timer",
        search_column_name="telegram_id",
        search_value=telegram_id,
        edit_param=[f"`count_hours` = '{count_hours + 1}'"])


# Квартиры
def search_by_id_apartment(id_row, user_id):
    values = GoogleWork().google_get_values(sheet_id="1_OlIeV7jYMN5H6zXZOqVsKrfuDjlJwpkhGoIjOQIUkg",
                                            name_list="Общая база",
                                            start_col="A",
                                            end_col="BE",
                                            major_dimension="ROWS")
    print(user_id)
    if verified_data_time(user_id) == True:
        for row in values:
            if str(row[0]) == str(id_row):
                try:
                    answer = f'ID:  {row[0]}\n' \
                             f'Квартал:  {row[1]}\n' \
                             f'Ориентиры:  {row[2]}\n' \
                             f'Улица:  {row[3]}\n' \
                             f'Номер дома:  {row[29]}\n' \
                             f'Номер квартиры:  {row[30]}\n' \
                             f'Кол-во комнат:  {row[4]}\n' \
                             f'Этаж:  {row[5]}\n' \
                             f'Этаж-сть:  {row[6]}\n' \
                             f'S общая:  {row[7]}\n' \
                             f'Балкон:  {row[8]}\n' \
                             f'Сан.узел:  {row[9]}\n' \
                             f'Ремонт:  {row[10]}\n' \
                             f'Тип строения:  {row[11]}\n' \
                             f'Планировка:  {row[12]}\n' \
                             f'Тип постройки:  {row[13]}\n' \
                             f'Высота потолков:  {row[15]}\n' \
                             f'Мебель:  {row[16]}\n' \
                             f'Техника:  {row[17]}\n' \
                             f'Стартовая цена:  {row[21]}\n' \
                             f'Цена:  {row[22]}\n' \
                             f'Имя собственника:  {row[23]}\n' \
                             f'Номер телефона:  {row[24]}\n' \
                             f'Доп.номер телефона:  {row[25]}\n' \
                             f'Вариант:  {row[35]}\n'

                    if len(row) >= 51:
                        answer = answer + f'Ссылка на сайт:  {row[51]}\n'

                    add_point(user_id)
                except:
                    return 'Не удалось получить данные с базы'

                return answer
            else:
                continue
        return 'Объекта нету в базе'
    else:
        return verified_data_time(user_id)


# Коммерция
def search_by_id_commerce(id_row, user_id):
    values = GoogleWork().google_get_values(sheet_id="1Q2jSOeCYi2FPVs0gI7vLQVljw1DfYKBHdUq7HpZVz4k",
                                            name_list="Общая база",
                                            start_col="A",
                                            end_col="BE",
                                            major_dimension="ROWS")

    if verified_data_time(user_id) == True:
        for row in values:
            if str(row[0]) == str(id_row):
                try:
                    answer = f'ID:  {row[0]}\n' \
                             f'Район:  {row[1]}\n' \
                             f'Ориентиры:  {row[2]}\n' \
                             f'Улица:  {row[3]}\n' \
                             f'Номер дома:  {row[31]}\n' \
                             f'Кол-во комнат:  {row[4]}\n' \
                             f'Этаж:  {row[5]}\n' \
                             f'Этаж-сть:  {row[6]}\n' \
                             f'S общая:  {row[7]}\n' \
                             f'S полезная:  {row[8]}\n' \
                             f'Площадь земли:  {row[14]}\n' \
                             f'Ремонт:  {row[9]}\n' \
                             f'Назначение:  {row[12]}\n' \
                             f'Тип строения:  {row[10]}\n' \
                             f'Тип недвижимости:  {row[11]}\n' \
                             f'Количество строений:  {row[13]}\n' \
                             f'Переведено в нежилое:  {row[15]}\n' \
                             f'Высота потолков:  {row[16]}\n' \
                             f'Проходимость:  {row[18]}\n' \
                             f'Завершенное строительство:  {row[21]}\n' \
                             f'Стартовая цена:  {row[23]}\n' \
                             f'Цена:  {row[24]}\n' \
                             f'Имя собственника:  {row[25]}\n' \
                             f'Номер телефона:  {row[26]}\n' \
                             f'Доп.номер телефона:  {row[27]}\n' \
                             f'Вариант:  {row[38]}\n'

                    if len(row) >= 42:
                        answer = answer + f'Ссылка на сайт:  {row[42]}\n'
                except:
                    return 'Не удалось получить данные с базы'

                if not answer:
                    pass
                else:
                    return answer
            else:
                continue
        return 'Объекта нету в базе'
    else:
        return verified_data_time(user_id)


# Дома
def search_by_id_home(id_row, user_id):
    values = GoogleWork().google_get_values(sheet_id="1zLwG9oJQU3wHSe0OQgOO27v7EDF_CCWrRVji1qr3dqs",
                                            name_list="Общая база",
                                            start_col="A",
                                            end_col="BE",
                                            major_dimension="ROWS")
    if verified_data_time(user_id) == True:
        for row in values:
            if str(row[0]) == str(id_row):
                try:
                    answer = f'ID:  {row[0]}\n' \
                             f'Район:  {row[1]}\n' \
                             f'Ориентиры:  {row[2]}\n' \
                             f'Улица:  {row[3]}\n' \
                             f'Номер дома:  {row[28]}\n' \
                             f'Кол-во комнат:  {row[4]}\n' \
                             f'Жилых комнат:  {row[5]}\n' \
                             f'Этаж-сть:  {row[6]}\n' \
                             f'S участка:  {row[7]}\n' \
                             f'S дома:  {row[8]}\n' \
                             f'Форма участка:  {row[9]}\n' \
                             f'Ремонт:  {row[11]}\n' \
                             f'Тип строения:  {row[12]}\n' \
                             f'Вид строительства:  {row[13]}\n' \
                             f'Строительство завершено:  {row[14]}\n' \
                             f'Высота потолков:  {row[16]}\n' \
                             f'Сан.узел:  {row[10]}\n' \
                             f'Мебель:  {row[17]}\n' \
                             f'Техника:  {row[18]}\n' \
                             f'Стартовая цена:  {row[21]}\n' \
                             f'Цена:  {row[22]}\n' \
                             f'Имя собственника:  {row[23]}\n' \
                             f'Номер телефона:  {row[24]}\n' \
                             f'Доп.номер телефона:  {row[25]}\n' \
                             f'Вариант:  {row[32]}\n'

                    if len(row) >= 36:
                        answer = answer + f'Ссылка на сайт:  {row[36]}\n'
                except:
                    return 'Не удалось получить данные с базы'

                if not answer:
                    pass
                else:
                    return answer
            else:
                continue
        return 'Объекта нету в базе'
    else:
        return verified_data_time(user_id)


# Аренда Квартиры
def search_by_id_apartment_rent(id_row, user_id):
    values = GoogleWork().google_get_values(sheet_id="1KA7eydXuGpmPDrYWisGQOnGHpeXEnlCv2ciBEcOMxNw",
                                            name_list="Квартиры",
                                            start_col="A",
                                            end_col="BE",
                                            major_dimension="ROWS")
    if verified_data_time(user_id) == True:
        for row in values:
            if str(row[0]) == str(id_row):
                try:
                    answer = f'ID:  {row[0]}\n' \
                             f'Квартал:  {row[1]}\n' \
                             f'Ориентиры:  {row[2]}\n' \
                             f'Улица:  {row[3]}\n' \
                             f'Номер дома:  {row[33]}\n' \
                             f'Номер квартиры:  {row[34]}\n' \
                             f'Кол-во комнат:  {row[4]}\n' \
                             f'Этаж:  {row[5]}\n' \
                             f'Этаж-сть:  {row[6]}\n' \
                             f'S общая:  {row[7]}\n' \
                             f'Балкон:  {row[8]}\n' \
                             f'Сан.узел:  {row[9]}\n' \
                             f'Ремонт:  {row[10]}\n' \
                             f'Тип строения:  {row[11]}\n' \
                             f'Планировка:  {row[12]}\n' \
                             f'Тип постройки:  {row[13]}\n' \
                             f'Высота потолков:  {row[28]}\n' \
                             f'Мебель:  {row[15]}\n' \
                             f'Техника:  {row[16]}\n' \
                             f'Кондиционер:  {row[17]}\n' \
                             f'Цена ежемесячная:  {row[20]}\n' \
                             f'Депозит:  {row[21]}\n' \
                             f'Предоплата:  {row[22]}\n' \
                             f'Комунальные:  {row[23]}\n' \
                             f'Имя собственника:  {row[24]}\n' \
                             f'Номер телефона:  {row[25]}\n' \
                             f'Доп.номер телефона:  {row[26]}\n' \
                             f'Вариант:  {row[37]}\n'

                    if len(row) >= 41:
                        answer = answer + f'Ссылка на сайт:  {row[41]}\n'
                except:
                    return 'Не удалось получить данные с базы'

                if not answer:
                    pass
                else:
                    return answer
            else:
                continue
        return 'Объекта нету в базе'
    else:
        return verified_data_time(user_id)


# Аренда Коммерция
def search_by_id_commerce_rent(id_row, user_id):
    values = GoogleWork().google_get_values(sheet_id="1KA7eydXuGpmPDrYWisGQOnGHpeXEnlCv2ciBEcOMxNw",
                                            name_list="Коммерция",
                                            start_col="A",
                                            end_col="BE",
                                            major_dimension="ROWS")
    if verified_data_time(user_id) == True:
        for row in values:
            if str(row[0]) == str(id_row):
                try:
                    answer = f'ID:  {row[0]}\n' \
                             f'Район:  {row[1]}\n' \
                             f'Ориентиры:  {row[3]}\n' \
                             f'Улица:  {row[2]}\n' \
                             f'Номер дома:  {row[32]}\n' \
                             f'Кол-во комнат:  {row[4]}\n' \
                             f'Этаж:  {row[5]}\n' \
                             f'Этаж-сть:  {row[6]}\n' \
                             f'S общая:  {row[8]}\n' \
                             f'S полезная:  {row[9]}\n' \
                             f'Площадь земли:  {row[10]}\n' \
                             f'Ремонт:  {row[11]}\n' \
                             f'Назначение:  {row[15]}\n' \
                             f'Тип строения:  {row[12]}\n' \
                             f'Парковка:  {row[20]}\n' \
                             f'Высота потолков:  {row[16]}\n' \
                             f'Проходимость:  {row[18]}\n' \
                             f'Цена ежемесячная:  {row[22]}\n' \
                             f'Депозит:  {row[23]}\n' \
                             f'Предоплата:  {row[24]}\n' \
                             f'Коммунальные:  {row[25]}\n' \
                             f'Имя собственника:  {row[27]}\n' \
                             f'Номер телефона:  {row[28]}\n' \
                             f'Доп.номер телефона:  {row[29]}\n' \
                             f'Вариант:  {row[36]}\n'

                    if len(row) >= 40:
                        answer = answer + f'Ссылка на сайт:  {row[40]}\n'
                except:
                    return 'Не удалось получить данные с базы'

                if not answer:
                    pass
                else:
                    return answer
            else:
                continue
        return 'Объекта нету в базе'
    else:
        return verified_data_time(user_id)


# Аренда Дома
def search_by_id_home_rent(id_row, user_id):
    values = GoogleWork().google_get_values(sheet_id="1KA7eydXuGpmPDrYWisGQOnGHpeXEnlCv2ciBEcOMxNw",
                                            name_list="Дома",
                                            start_col="A",
                                            end_col="BE",
                                            major_dimension="ROWS")
    if verified_data_time(user_id) == True:
        for row in values:
            if str(row[0]) == str(id_row):
                try:
                    answer = f'ID:  {row[0]}\n' \
                             f'Район:  {row[1]}\n' \
                             f'Ориентиры:  {row[3]}\n' \
                             f'Улица:  {row[2]}\n' \
                             f'Номер дома:  {row[28]}\n' \
                             f'Кол-во комнат:  {row[4]}\n' \
                             f'Жилых комнат:  {row[5]}\n' \
                             f'Этаж-сть:  {row[6]}\n' \
                             f'S участка:  {row[7]}\n' \
                             f'S дома:  {row[8]}\n' \
                             f'Ремонт:  {row[10]}\n' \
                             f'Тип строения:  {row[11]}\n' \
                             f'Арендатор:  {row[12]}\n' \
                             f'Высота потолков:  {row[14]}\n' \
                             f'Сан.узел:  {row[9]}\n' \
                             f'Мебель:  {row[15]}\n' \
                             f'Техника:  {row[16]}\n' \
                             f'Цена ежемесячная:  {row[19]}\n' \
                             f'Депозит:  {row[20]}\n' \
                             f'Предоплата:  {row[21]}\n' \
                             f'Комунальные:  {row[22]}\n' \
                             f'Имя собственника:  {row[23]}\n' \
                             f'Номер телефона:  {row[24]}\n' \
                             f'Доп.номер телефона:  {row[25]}\n' \
                             f'Вариант:  {row[31]}\n'

                    if len(row) >= 35:
                        answer = answer + f'Ссылка на сайт:  {row[35]}\n'
                except:
                    return 'Не удалось получить данные с базы'

                if not answer:
                    pass
                else:
                    return answer
            else:
                continue
        return 'Объекта нету в базе'
    else:
        return verified_data_time(user_id)


@dp.message_handler(state=SearchState.SearchId_Q1)
async def get_row_word(message: types.Message, state=FSMContext):
    word_row = message.text
    await state.update_data(var_word_id=word_row)
    await message.answer('Введите ID объекта', reply_markup=ReplyKeyboardRemove())
    await SearchState.SearchId_Q2.set()


@dp.message_handler(state=SearchState.SearchId_Q2)
async def get_id_row(message: types.Message, state=FSMContext):
    id_row = message.text
    user_id = message.from_user.id
    if len(id_row) >= 6:
        data = await state.get_data()
        word_row = data['var_word_id']

        if word_row == 'К' or word_row == 'Н' or word_row == 'И':
            await message.answer(f"Поиск в базе квартир...")
            answer = search_by_id_apartment(id_row, user_id)
            await message.answer(f"{answer}")
            await message.answer(f"Выберите нужный вам вариант", reply_markup=kb_go_start)
            await SearchState.SearchId_Q3.set()

        elif word_row == 'КМ':
            await message.answer(f"Поиск в базе коммерции...")
            answer = search_by_id_commerce(id_row, user_id)
            await message.answer(f"{answer}")
            await message.answer(f"Выберите нужный вам вариант", reply_markup=kb_go_start)
            await SearchState.SearchId_Q3.set()

        elif word_row == 'Д':
            await message.answer(f"Поиск в базе домов...")
            answer = search_by_id_home(id_row, user_id)
            await message.answer(f"{answer}")
            await message.answer(f"Выберите нужный вам вариант", reply_markup=kb_go_start)
            await SearchState.SearchId_Q3.set()

        elif word_row == 'АК':
            await message.answer(f"Поиск в базе аренды квартир...")
            answer = search_by_id_apartment_rent(id_row, user_id)
            await message.answer(f"{answer}")
            await message.answer(f"Выберите нужный вам вариант", reply_markup=kb_go_start)
            await SearchState.SearchId_Q3.set()

        elif word_row == 'АКМ':
            await message.answer(f"Поиск в базе аренды коммерции...")
            answer = search_by_id_commerce_rent(id_row, user_id)
            await message.answer(f"{answer}")
            await message.answer(f"Выберите нужный вам вариант", reply_markup=kb_go_start)
            await SearchState.SearchId_Q3.set()

        elif word_row == 'АД':
            await message.answer(f"Поиск в базе аренды домов...")
            answer = search_by_id_home_rent(id_row, user_id)
            await message.answer(f"{answer}")
            await message.answer(f"Выберите нужный вам вариант", reply_markup=kb_go_start)
            await SearchState.SearchId_Q3.set()

    else:
        await message.answer(f"Пожалуйста введите корректный ID...")
        await message.answer(f"Выберите нужный вам вариант", reply_markup=kb_go_start)
        await SearchState.SearchId_Q3.set()


@dp.message_handler(Text(equals='Повторить запрос'), state=SearchState.SearchId_Q3)
async def go_to_start(message: types.Message, state=FSMContext):
    await message.answer('Выберите букву объекта:\n'
                         'К - квартира\n'
                         'Н - новостройка\n'
                         'И - и другие\n'
                         'КМ - коммерция\n'
                         'Д - дом\n'
                         'АК - аренда квартиры\n'
                         'АКМ - аренда коммерции\n'
                         'АД - аренда дома\n'
                         , reply_markup=kb_word_object)
    await SearchState.SearchId_Q1.set()


@dp.message_handler(Text(equals='Перейти в главное меню'), state=SearchState.SearchId_Q3)
async def go_to_start(message: types.Message, state=FSMContext):
    await message.answer('Что тебе нужно?',
                         reply_markup=kb_main_menu)
    await state.reset_state()
