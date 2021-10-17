from datetime import date

from google_work.google_work import GoogleWork


def activate(type_of_property, id_object, date_enter=date.today()):
    date_enter = str(date_enter)
    if type_of_property == 'квартиры' or type_of_property == 'квартира':
        objects = GoogleWork().google_get_values(sheet_id='1_OlIeV7jYMN5H6zXZOqVsKrfuDjlJwpkhGoIjOQIUkg',
                                                 name_list='Общая база',
                                                 start_col='A',
                                                 end_col='B',
                                                 major_dimension='COLUMNS')
        num = 1
        for row in objects[0]:
            if str(row) == str(id_object):
                GoogleWork().google_edit_values(sheet_id='1_OlIeV7jYMN5H6zXZOqVsKrfuDjlJwpkhGoIjOQIUkg',
                                                name_list='Общая база',
                                                start_col='AL',
                                                start_row=num,
                                                end_col='Al',
                                                end_row=num,
                                                major_dimension="COLUMNS",
                                                values=[date_enter])
            else:
                num = num + 1
                pass

    elif type_of_property == 'коммерция':
        objects = GoogleWork().google_get_values(sheet_id='1Q2jSOeCYi2FPVs0gI7vLQVljw1DfYKBHdUq7HpZVz4k',
                                                 name_list='Общая база',
                                                 start_col='A',
                                                 end_col='B',
                                                 major_dimension='COLUMNS')
        num = 1
        for row in objects[0]:
            if str(row) == str(id_object):
                GoogleWork().google_edit_values(sheet_id='1Q2jSOeCYi2FPVs0gI7vLQVljw1DfYKBHdUq7HpZVz4k',
                                                name_list='Общая база',
                                                start_col='AQ',
                                                start_row=num,
                                                end_col='AQ',
                                                end_row=num,
                                                major_dimension="COLUMNS",
                                                values=[date_enter])
            else:
                num = num + 1
                pass

    elif type_of_property == 'дома' or 'дом':
        objects = GoogleWork().google_get_values(sheet_id='1zLwG9oJQU3wHSe0OQgOO27v7EDF_CCWrRVji1qr3dqs',
                                                 name_list='Общая база',
                                                 start_col='A',
                                                 end_col='B',
                                                 major_dimension='COLUMNS')
        num = 1
        for row in objects[0]:
            if str(row) == str(id_object):
                GoogleWork().google_edit_values(sheet_id='1zLwG9oJQU3wHSe0OQgOO27v7EDF_CCWrRVji1qr3dqs',
                                                name_list='Общая база',
                                                start_col='AK',
                                                start_row=num,
                                                end_col='AK',
                                                end_row=num,
                                                major_dimension="COLUMNS",
                                                values=[date_enter])
            else:
                num = num + 1
                pass

    elif type_of_property == 'аренда квартиры':
        objects = GoogleWork().google_get_values(sheet_id='1KA7eydXuGpmPDrYWisGQOnGHpeXEnlCv2ciBEcOMxNw',
                                                 name_list='Квартиры',
                                                 start_col='A',
                                                 end_col='B',
                                                 major_dimension='COLUMNS')
        num = 1
        for row in objects[0]:
            if str(row) == str(id_object):
                GoogleWork().google_edit_values(sheet_id='1KA7eydXuGpmPDrYWisGQOnGHpeXEnlCv2ciBEcOMxNw',
                                                name_list='Квартиры',
                                                start_col='AQ',
                                                start_row=num,
                                                end_col='AQ',
                                                end_row=num,
                                                major_dimension="COLUMNS",
                                                values=[date_enter])
            else:
                num = num + 1
                pass
    elif type_of_property == 'аренда дома':
        objects = GoogleWork().google_get_values(sheet_id='1KA7eydXuGpmPDrYWisGQOnGHpeXEnlCv2ciBEcOMxNw',
                                                 name_list='Дома',
                                                 start_col='A',
                                                 end_col='B',
                                                 major_dimension='COLUMNS')
        num = 1
        for row in objects[0]:
            if str(row) == str(id_object):
                GoogleWork().google_edit_values(sheet_id='1KA7eydXuGpmPDrYWisGQOnGHpeXEnlCv2ciBEcOMxNw',
                                                name_list='Дома',
                                                start_col='AK',
                                                start_row=num,
                                                end_col='AK',
                                                end_row=num,
                                                major_dimension="COLUMNS",
                                                values=[date_enter])
            else:
                num = num + 1
                pass
    elif type_of_property == 'аренда коммерция':
        objects = GoogleWork().google_get_values(sheet_id='1KA7eydXuGpmPDrYWisGQOnGHpeXEnlCv2ciBEcOMxNw',
                                                 name_list='Коммерция',
                                                 start_col='A',
                                                 end_col='B',
                                                 major_dimension='COLUMNS')
        num = 1
        for row in objects[0]:
            if str(row) == str(id_object):
                GoogleWork().google_edit_values(sheet_id='1KA7eydXuGpmPDrYWisGQOnGHpeXEnlCv2ciBEcOMxNw',
                                                name_list='Коммерция',
                                                start_col='AO',
                                                start_row=num,
                                                end_col='AO',
                                                end_row=num,
                                                major_dimension="COLUMNS",
                                                values=[date_enter])
            else:
                num = num + 1
                pass
    else:
        pass
