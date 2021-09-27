import os

from dotenv import load_dotenv
from mysql import connector
from mysql.connector.errors import Error

load_dotenv()


class Connection:

    def __init__(self):
        self.host = os.getenv("DB_HOSTING")
        self.user = os.getenv("db_user")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB")
        self.connector = None
        self.cursor = None

        try:
            self.connector = connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Connection MySQL DB successfully")
        except Error as e:
            print(e)

    def make_cursor(self):
        try:
            self.cursor = self.connector.cursor()
            print("Cursor make successfully")
        except Error as e:
            print(e)

