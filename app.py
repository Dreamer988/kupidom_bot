from sql.sql_query import SqlQuery
from sql.stock_table_query import create_db_agents, create_db_managers, create_db_bot_timer, create_db_olx, \
    create_db_olx_verification, create_db_olx_waiting
from utils.set_bot_commands import set_default_commands


async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)
    await set_default_commands(dp)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    db_tables = SqlQuery().get_all_name_tables()
    if 'agents' not in db_tables:
        create_db_agents()
    if 'managers' not in db_tables:
        create_db_managers()
    if 'bot_timer' not in db_tables:
        create_db_bot_timer()
    if 'olx' not in db_tables:
        create_db_olx()
    if 'olx_verification' not in db_tables:
        create_db_olx_verification()
    if 'olx_waiting' not in db_tables:
        create_db_olx_waiting()

    executor.start_polling(dp, on_startup=on_startup)
