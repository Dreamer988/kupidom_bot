import os

from dotenv import load_dotenv

from sql.sql_query import SqlQuery

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}


def user_access():
    managers_db = SqlQuery().get_column(
        table_name='managers',
        get_column_name='telegram_id',
    )
    agents_db = SqlQuery().get_column(
        table_name='agents',
        get_column_name='telegram_id',
    )
    all_users = []

    if managers_db:
        for manager in managers_db:
            all_users.append(manager[0])
    else:
        pass

    if agents_db:
        for agent in agents_db:
            all_users.append(agent[0])
    else:
        pass

    user = tuple(all_users)

    return user


def user_admin():
    admins_db = SqlQuery().get_column_by_param(
        table_name='managers',
        get_column_name='telegram_id',
        search_column_name='position',
        search_value='admin'
    )

    admins = []

    if admins_db:
        for admin in admins_db:
            admins.append(admin[0])
    else:
        pass

    return admins
