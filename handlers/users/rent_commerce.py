# import os
#
# import googleapiclient.discovery
# import httplib2
# from aiogram import types
# from aiogram.dispatcher import FSMContext
# from dotenv import load_dotenv
# from oauth2client.service_account import ServiceAccountCredentials
#
# from loader import dp
# from states import ObjectState, ApartmentState
#
# load_dotenv()
#
#
# def google_sendler(sheet_id, start_col, end_col, array_data):
#     CREDENTAILS_FILE = os.getenv('CREDENTAILS_FILE')
#     credentials = ServiceAccountCredentials.from_json_keyfile_name(
#         CREDENTAILS_FILE,
#         ['https://www.googleapis.com/auth/spreadsheets',
#          'https://www.googleapis.com/auth/drive'])
#     httpAuth = credentials.authorize(httplib2.Http())
#     service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)
#     spreadsheet_id = sheet_id
#
#     values = service.spreadsheets().values().get(
#         spreadsheetId=spreadsheet_id,
#         range=f"{start_col}:{end_col}",
#         majorDimension="COLUMNS"
#     ).execute()
#     start_range = len(values['values'][0]) + 1
#     sheet_range = f"{start_col}{start_range}:{end_col}{start_range}"
#
#     values = service.spreadsheets().values().append(
#         spreadsheetId=spreadsheet_id,
#         range=f"{start_col}{start_range}",
#         valueInputOption="USER_ENTERED",
#         body={
#             "values": [['']]
#         }
#     ).execute()
#
#     values = service.spreadsheets().values().batchUpdate(
#         spreadsheetId=spreadsheet_id,
#         body={
#             "valueInputOption": "USER_ENTERED",
#             "data": [
#                 {
#                     "range": sheet_range,
#                     "majorDimension": "ROWS",
#                     "values": [array_data]
#                 }
#             ]
#         }
#     ).execute()
#
#
# # Отслеживаем сообщение по фильтру состояния MenuState.Sale
# @dp.message_handler(text="Квартира", state=ObjectState.Sale)
# async def select_district(message: types.Message, state=FSMContext):
#     # Получаем текст сообщения, а после записываем значение в переменную district
#     type_of_service = message.text
#
#     # Записываем полученное значение в словарь машины состояний под ключом var_type_of_service
#     await state.update_data(var_type_of_service=type_of_service)
#     # Отправляем сообщение и массив кнопок
#     await message.answer("Выберите район", reply_markup=)
#     # Переходим в машину состояний ApartmentState
#     await ApartmentState.first()
