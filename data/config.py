import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
admins = [
    362089194
]

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
users_access = ['535176521', '389654095', '751245977', '1039881340', '720106529', '1004944693', '613067717',
                '1014269565', '1798423812', '769220154', '1011307903', '769219016', '1809144253']
