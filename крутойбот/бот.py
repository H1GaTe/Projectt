import telebot
from telebot import types
from config import Config

bot = telebot.TeleBot(Config.TOKEN)

# Словарь для хранения пользователей
users = {}

# Приветственное сообщение и авторизация пользователя
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать в бот колледжа! Пожалуйста, авторизуйтесь.")
    bot.send_message(message.chat.id, "Введите ваше имя пользователя:")
    bot.register_next_step_handler(message, process_username)

def process_username(message):
    username = message.text
    users[message.chat.id] = {'username': username}
    bot.send_message(message.chat.id, f"Привет, {username}! Используйте /help для просмотра доступных команд.")

# Справка
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "/start - Начать работу с ботом\n"
        "/help - Список доступных команд\n"
        "/info - Информация о колледже\n"
        "/schedule - Расписание занятий\n"
        "/faq - Часто задаваемые вопросы\n"
        "/teachers - Информация о преподавателях\n"
        "/news - Новости и объявления"
    )
    bot.reply_to(message, help_text)

# Информация о колледже
@bot.message_handler(commands=['info'])
def send_info(message):
    info_text = (
        "Колледж XYZ - это ведущий образовательный центр с множеством программ обучения.\n"
        "Адрес: Улица Примерная, 123\n"
        "Телефон: +1234567890\n"
        "Email: info@xyzcollege.com"
    )
    bot.reply_to(message, info_text)

# Расписание занятий
@bot.message_handler(commands=['schedule'])
def send_schedule(message):
    schedule_text = (
        "Расписание занятий:\n"
        "Понедельник - Пятница: 8:00 - 18:00\n"
        "Суббота: 8:00 - 14:00\n"
        "Воскресенье: выходной"
    )
    bot.reply_to(message, schedule_text)

# Часто задаваемые вопросы
@bot.message_handler(commands=['faq'])
def send_faq(message):
    faq_text = (
        "Часто задаваемые вопросы:\n"
        "1. Как подать заявку? - Вы можете подать заявку на нашем сайте.\n"
        "2. Какие программы обучения доступны? - Мы предлагаем программы по различным направлениям.\n"
        "3. Как связаться с нами? - Вы можете позвонить по телефону +1234567890 или написать на email info@xyzcollege.com."
    )
    bot.reply_to(message, faq_text)

# Информация о преподавателях
@bot.message_handler(commands=['teachers'])
def send_teachers(message):
    teachers_text = (
        "Преподаватели колледжа:\n"
        "1. Иван Иванович - Программирование\n"
        "2. Петр Петрович - Математика\n"
        "3. Мария Ивановна - Физика"
    )
    bot.reply_to(message, teachers_text)

# Новости и объявления
@bot.message_handler(commands=['news'])
def send_news(message):
    news_text = (
        "Последние новости и объявления:\n"
        "1. День открытых дверей состоится 25 мая.\n"
        "2. Начало нового семестра 1 сентября.\n"
        "3. Конкурс научных проектов в октябре."
    )
    bot.reply_to(message, news_text)

# Клавиатура
def main_menu_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    btn_info = types.KeyboardButton('/info')
    btn_schedule = types.KeyboardButton('/schedule')
    btn_faq = types.KeyboardButton('/faq')
    btn_teachers = types.KeyboardButton('/teachers')
    btn_news = types.KeyboardButton('/news')
    keyboard.add(btn_info, btn_schedule, btn_faq, btn_teachers, btn_news)
    return keyboard

# Обработчик всех текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.send_message(message.chat.id, "Извините, я не понимаю этот запрос. Пожалуйста, используйте /help для просмотра доступных команд.", reply_markup=main_menu_keyboard())

# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)