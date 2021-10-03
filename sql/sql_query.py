from mysql.connector.errors import Error

from sql import connection


def tuple_to_dict(arrays):
    try:
        if type(arrays[0]) is tuple:
            array_main = []
            for array in arrays:
                sub_array = []
                for item in array:
                    sub_array.append(item)
                array_main.append(sub_array)
            return array_main
    except:
        print('Передан не массив с кортежами')
        return None


class SqlQuery:
    """
    Выполняет изменения в БД users
    """

    def __init__(self):
        # Создаем экземпляр класса
        connect = connection.Connection()
        # Создаем курсор
        connect.make_cursor()
        # Получаем объект курсора
        self.cursor = connect.cursor
        # Получаем объект соединения с базой
        self.connection = connect.connector

    def  create_table(self, query):
        """
        Создание таблиц в БД
        """
        try:
            # Выполням полученный запрос
            self.cursor.execute(query)
            # Сохраняем изменеия в БД
            self.connection.commit()

        except Error as e:
            print(e)

    def get_all_name_tables(self):
        """
        Функция котрая возвращает все названия таблиц существующих в БД
        """

        # Создаем запрос
        query_get_all_tables = \
            f"""
                SHOW 
                    TABLES
            """

        try:
            # Выполням созданный запрос
            self.cursor.execute(query_get_all_tables)
            # Получаем значения
            values = self.cursor.fetchall()
            # Преобразуем кортеж в список
            if values:
                values = tuple_to_dict(values)
            else:
                return values
            # Возвращаем значения
            return values
        except Error as e:
            print(e)
            return False

    def add_row(self, table_name=None, keys=None, values=None):
        """
        Добавление пользователя в БД
        Последовательность ключей и значений должна быть одинаковой

        table_name -> str, название таблицы
        keys -> dict, через запятую прописанные ключи
        (названия столбцов в БД)
        vales -> tuple, кортеж со значениями для ключей

        """

        # Объеденяем ключи в строку через запятую
        join_keys = ','.join(keys)

        # Создаем запрос
        query = \
            f"""
                INSERT INTO 
                    {table_name} 
                        ({join_keys})
                VALUES 
                    {values}
            """
        try:
            # Выполням созданный запрос
            self.cursor.execute(query)
            # Сохраняем изменеия в БД
            self.connection.commit()
        except Error as e:
            print(e)
            return False

    def delete_row(self, table_name=None, search_column_name=None, search_value=None):
        """
        Удаление строки из базы данных
        """

        # Создаем запрос
        query = \
            f"""
                DELETE FROM 
                    {table_name}
                WHERE 
                    {search_column_name} = '{search_value}'
            """
        try:
            # Выполням созданный запрос
            self.cursor.execute(query)
            # Сохраняем изменеия в БД
            self.connection.commit()
        except Error as e:
            print(e)
            return False

    def edit_row(self, table_name=None, search_column_name=None, search_value=None, edit_param=None):
        """
        Изменение данных строки

        edit_param -> dict[] -> str() , `key` (название столбца) = value
        """

        # Объеденяем изменяемые параметры в строку через запятую
        join_keys = ','.join(edit_param)

        # Создаем запрос
        query = \
            f"""
                UPDATE 
                    {table_name}
                SET 
                    {join_keys}
                WHERE 
                    {search_column_name} = '{search_value}'
            """
        try:
            # Выполням созданный запрос
            self.cursor.execute(query)
            # Сохраняем изменеия в БД
            self.connection.commit()
        except Error as e:
            print(e)
            return False

    def get_table(self, table_name):
        # Создаем запрос
        query_get_table = \
            f"""
                SELECT * FROM 
                    {table_name}
            """
        try:
            # Выполням созданный запрос
            self.cursor.execute(query_get_table)
            # Получаем значения
            values = self.cursor.fetchall()
            # Преобразуем кортеж в список
            values = tuple_to_dict(values)
            # Возвращаем значения
            return values
        except Error as e:
            print(e)
            return False

    def get_row(self, table_name=None, search_param=None):
        """
        search_param -> list[param]
        *param -> str, key = 'value'
        """
        join_search_param = ' and '.join(search_param)

        # Создаем запрос
        query_get_row = \
            f"""
                SELECT
                    *
                FROM
                    {table_name}
                WHERE
                    {join_search_param}
            """
        try:
            # Выполням созданный запрос
            self.cursor.execute(query_get_row)
            # Получаем значения
            values = self.cursor.fetchall()
            # Преобразуем кортеж в список
            values = tuple_to_dict(values)
            # Возвращаем значения
            return values
        except Error as e:
            print(e)
            return False

    def get_column(self, table_name=None, get_column_name=None):
        # Создаем запрос
        query_get_column = \
            f"""
                SELECT
                    {get_column_name}
                FROM
                    {table_name}      
            """
        try:
            # Выполням созданный запрос
            self.cursor.execute(query_get_column)
            # Получаем значения
            values = self.cursor.fetchall()
            # Преобразуем кортеж в список
            values = tuple_to_dict(values)
            # Возвращаем значения
            return values
        except Error as e:
            print(e)
            return False

    def get_column_by_param(self, table_name=None, get_column_name='*', search_column_name=None, search_value=None):
        # Создаем запрос
        query_get_column_by_param = \
            f"""
                SELECT
                    {get_column_name}
                FROM
                    {table_name}      
                WHERE
                    {search_column_name} = '{search_value}'
            """
        try:
            # Выполням созданный запрос
            self.cursor.execute(query_get_column_by_param)
            # Получаем значения
            values = self.cursor.fetchall()
            # Преобразуем кортеж в список
            values = tuple_to_dict(values)
            # Возвращаем значения
            return values
        except Error as e:
            print(e)
            return False
