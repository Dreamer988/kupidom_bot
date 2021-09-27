import googleapiclient.discovery
import httplib2
from oauth2client.service_account import ServiceAccountCredentials


class GoogleWork:

    def __init__(self):
        CREDENTAILS_FILE = "G:\Python\kupidom_telegram_bot\creds.json"
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(
            CREDENTAILS_FILE,
            ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive'])
        httpAuth = self.credentials.authorize(httplib2.Http())
        self.service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)

    def google_add_row(self, sheet_id, name_list, array_data):
        """
        Добавление строки с данными в google_work sheets

        sheet_id -> ID таблицы google_work sheets
        name_list -> Название листа в таблице (Например: List1)
        start_col -> Начало диапазона. Указывается название столбца (Например: A)
        end_col -> Конец диапазона. Указывается название столбца (Например: AY)
        array_data -> dict, Массив данных для добавления в таблицу. Длинна массива должна быть равна диапазону
        """

        values = self.service.spreadsheets().values().append(
            spreadsheetId=sheet_id,
            range=f"{name_list}",
            valueInputOption="USER_ENTERED",
            body={
                "values": [array_data]
            }
        ).execute()

    def google_get_values(self, sheet_id, name_list, start_col, end_col, major_dimension, start_row=None, end_row=None):
        if start_row and end_row:
            values = self.service.spreadsheets().values().get(
                spreadsheetId=sheet_id,
                range=f"'{name_list}'!{start_col}{start_row}:{end_col}{end_row}",
                majorDimension=major_dimension
            ).execute()
            return values["values"]
        else:
            values = self.service.spreadsheets().values().get(
                spreadsheetId=sheet_id,
                range=f"'{name_list}'!{start_col}:{end_col}",
                majorDimension=major_dimension
            ).execute()
            return values["values"]
