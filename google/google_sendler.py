import os
from pprint import pprint

import googleapiclient.discovery
import httplib2
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()


def google_sendler():
    CREDENTAILS_FILE = '../../creds.json'
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTAILS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)
    spreadsheet_id = '1-B80joNKTOSTIJRLiACOcfH1E3dH5yrNPbS-CU5Bvxc'

    # values = service.spreadsheets().values().get(
    #     spreadsheetId=spreadsheet_id,
    #     range="A:A",
    #     majorDimension="COLUMNS"
    # ).execute()
    # pprint(values['values'][0])
    # pprint(len(values['values'][0]))
    # start_range = len(values['values'][0]) + 1
    # sheet_range = f"{start_col}{start_range}:{end_col}{start_range}"

    values = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range="A11",
        valueInputOption="USER_ENTERED",
        body={
                "values": [['']]
        }
    ).execute()



google_sendler()
