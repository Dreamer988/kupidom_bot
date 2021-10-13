from mysql.connector.errors import Error

from sql.sql_query import SqlQuery


def create_db_agents():
    # Создадим таблицу users для пользователей бота
    try:
        query = """
                CREATE TABLE agents (
                    `id` INT AUTO_INCREMENT PRIMARY KEY,
                    `telegram_id` BIGINT UNIQUE,
                    `first_name` VARCHAR(100),
                    `last_name` VARCHAR(100),
                    `patronymic` VARCHAR(100),
                    `date` DATE,
                    `phone` VARCHAR(100),
                    `residence_area` VARCHAR(100),
                    `type_of_property` VARCHAR(100),
                    `class` VARCHAR(100),
                    `sector` INT )
                """
        # Создаем базу данных
        SqlQuery().create_table(query=query)
        print("Create table agents successfully")
    except Error as e:
        print(e)
        print("DB agents has already been created")


def create_db_managers():
    # Создадим таблицу users для пользователей бота
    try:
        query = """
                CREATE TABLE managers (
                    `id` INT AUTO_INCREMENT PRIMARY KEY,
                    `telegram_id` BIGINT UNIQUE,
                    `first_name` VARCHAR(100),
                    `last_name` VARCHAR(100),
                    `patronymic` VARCHAR(100),
                    `date` DATE,
                    `phone` VARCHAR(100),
                    `position` VARCHAR(100),
                    `residence_area` VARCHAR(100) )
                """
        # Создаем базу данных
        SqlQuery().create_table(query=query)
        print("Create table managers successfully")
    except Error as e:
        print(e)
        print("DB managers has already been created")


def create_db_olx():
    # Создадим таблицу users для пользователей бота
    try:
        query = """
                CREATE TABLE olx (
                    `id` INT AUTO_INCREMENT PRIMARY KEY,
                    `type_of_property` VARCHAR(100),
                    `district` VARCHAR(100),
                    `sector` INT,
                    `phone` VARCHAR (100),
                    `information` VARCHAR(2000),
                    `date` DATETIME
                     )
                """
        # Создаем базу данных
        SqlQuery().create_table(query=query)
        print("Create table olx successfully")
    except Error as e:
        print(e)
        print("DB olx has already been created")


def create_db_bot_timer():
    # Создадим таблицу users для пользователей бота
    try:
        query = """
                CREATE TABLE bot_timer (
                    `id` INT AUTO_INCREMENT NOT NULL UNIQUE,
                    `telegram_id` BIGINT UNIQUE,
                    `count_day` INT,
                    `count_hours` INT,
                    `day` INT,
                    `hour` INT,
                    FOREIGN KEY(telegram_id) REFERENCES agents(telegram_id)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
                )
                """
        # Создаем базу данных
        SqlQuery().create_table(query=query)
        print("Create table bot_timer successfully")
    except Error as e:
        print(e)
        print("DB bot_timer has already been created")
