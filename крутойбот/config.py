import os

class Config:
    TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN') or '7172583524:AAFUBObEKo1qi_zBcIlupuAGafBUk_9r0pM'
    ADMIN_ID = os.environ.get('ADMIN_ID') or '1255584574'