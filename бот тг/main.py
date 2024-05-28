import telebot
import webbrowser
from telebot import types
import logging
from PIL import Image
import io

bot = telebot.TeleBot("6610256377:AAExQcLJdXDVg0uZkgi4xiU3tPGqXbjRDP4")

logging.basicConfig(level=logging.INFO)

def resize_image(image_path):
    with Image.open(image_path) as img:
        img.thumbnail((1280, 1280))
        byte_arr = io.BytesIO()
        img.save(byte_arr, format='JPEG')
        return byte_arr.getvalue()


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('Наш Веб сайт')
    btn4 = types.KeyboardButton('О нас')
    markup.row(btn4, btn1)
    btn2 = types.KeyboardButton('Помощь')
    markup.row(btn2)
    photo = open('photos.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, caption='Здравствуйте! Вас приветствует бот колледжа "КМИБ" — Колледжа менеджмента и бизнеса города Астана. Данный бот поможет вам узнать информацию о нашем учебном заведении.', reply_markup=markup)
    bot.register_next_step_handler(message, one_click)

@bot.message_handler(func=lambda msg: msg.text == '/info')
def get_user_photo(message: types.Message):
    bot.send_photo(message.chat.id, "https://imgur.com/a/g3vwZzI")
    bot.send_photo(message.chat.id, "https://imgur.com/a/jHcgout")
    bot.send_photo(message.chat.id, "https://imgur.com/a/jXEYXDm")
    bot.send_photo(message.chat.id, "https://imgur.com/a/9ahAUNT")
    bot.send_photo(message.chat.id, "https://imgur.com/a/u7FcdkL")
    bot.send_photo(message.chat.id, "https://imgur.com/a/50NKZ33")
    bot.send_photo(message.chat.id, "https://imgur.com/a/XnMhmQa")
    bot.send_photo(message.chat.id, "https://imgur.com/a/Pxg68Yv")
    bot.send_photo(message.chat.id, "https://imgur.com/a/SSeyCMD")
    bot.send_photo(message.chat.id, "https://imgur.com/a/Lhjx7KS")
    bot.send_photo(message.chat.id, "https://imgur.com/a/EH6RFUy")
    bot.send_photo(message.chat.id, "https://imgur.com/a/rRoX7hk")
    bot.send_photo(message.chat.id, "https://imgur.com/a/U26EX6W")
    bot.send_photo(message.chat.id, "https://imgur.com/a/S2klkAb")
    bot.send_photo(message.chat.id, "https://imgur.com/a/EswJ50H")
    bot.send_photo(message.chat.id, "https://imgur.com/a/JvoSDiA")
    bot.send_photo(message.chat.id, "https://imgur.com/a/1kNXJU4")
    bot.send_photo(message.chat.id, "https://imgur.com/a/ohxIOV4")
    bot.send_photo(message.chat.id, "https://imgur.com/a/HjtqNDZ")
    bot.send_photo(message.chat.id, "https://imgur.com/a/ZgP441R")
    bot.send_photo(message.chat.id, "https://imgur.com/a/qAWEWBX")
    bot.send_photo(message.chat.id, "https://imgur.com/a/Rp6aWB7")
    bot.send_photo(message.chat.id, "https://imgur.com/a/FM3xODM")

@bot.message_handler(func=lambda msg: msg.text == '/specialties')
def get_user_photo(message: types.Message):
    bot.send_photo(message.chat.id, "https://imgur.com/a/SuoZj1J")
    bot.send_photo(message.chat.id, "https://imgur.com/a/LH2C3Zn")

def one_click(message):
    if message.text == 'Наш Веб сайт':
        bot.send_message(message.chat.id, 'На сайте нашего колледжа вы можете узнать больше информации про колледж, ознакомиться со свежими новостями, а также подать электронную заявку на поступление: https://kmib.edu.kz/')
    elif message.text == 'Помощь':
        bot.send_message(message.chat.id, 'Команды бота \n'
                                          '1)Чтобы узнать адрес коледжа - /location \n'
                                          '2)Информация о поступлении - /info\n'
                                          '3)Специальности - /specialties\n'
                                          '4)Контакты - /contacts\n'
                                          '5)Сайт коледжа - /site\n'
                                          '6)Наш колектив -/colective')
    elif message.text == 'О нас':
        bot.send_message(message.chat.id, f'Миссия: Предоставление инновационных образовательных услуг и обеспечение квалифицированными специалистами столицы и РК \n \n'
                                          'Видение: Войти в десятку лучших колледжей Республики Казахстан. Укрепление роли как одного из ведущих частных колледжей столицы. \n \n'
                                          'Преимущества колледжа: \n'
                                          '1)Прохождение производственной практики на базе социальных партнеров с дальнейшим трудоустройством (100% трудоустройство) \n \n' 
                                          '2)Новое общежитие, оборудованное современной техникой в шаговой доступности от колледжа (открытие в 2022г.) \n \n'
                                          '3)Мы находимся на рынке труда 15 лет \n \n'
                                          '4)Возможность получения двойного диплома \n \n'
                                          '5)Удобное месторасположение с удобной транспортной развязкой \n \n'
                                          'Условия колледжа \n \n'
                                          '1) Зачисление без вступительных экзаменов на основе собеседования \n \n'
                                          '2) Обучение бесплатное (с выплатой государственной стипендии) и на договорной основе \n \n'
                                          '3) Отсрочка от службы в армию \n \n'
                                          '4) Яркая студенческая жизнь \n \n'
                                          '5) Продолжение получения образования в ВУЗах Казахстана и за рубежом по родственным специальностям с сокращенным сроком обучения\n \n'
                                          '6) Участие студентов в городских, республиканских и международных конкурсах и выставках')
        


@bot.message_handler(commands=['contacts'])
def contacts(message):
    bot.send_message(message.chat.id, f'Колледж КМИБО - это ведущий образовательный центр с множеством программ обучения. \n \n'
                                      'Тел.: +77172382605, +77172380413, +77004349100 \n'
                                      'Эл.Почта : kmib@list.ru \n'
                                      'facebook - https://www.facebook.com/profile.php?id=61552068718349 \n'
                                      'instagram - https://www.instagram.com/kmib_life/')

@bot.message_handler(commands=['colective'])
def colective(message):
    bot.send_message(message.chat.id, 'Колектив нашего колледжа\n \n'
                                      'Пшенова Балкия Асыгатовна - Первый Руководитель\n \n'
                                      'Бектурсынова Раушан Ажибековна - Заместитель руководителя по воспитательной работе\n \n'
                                      'Камбетова Гаухар Закошевна - Заместитель руководителя по учебно-методической работе\n \n'
                                      'Касенова Гульбарам Сарсенбаевна - Заместитель руководителя по учебной работе\n \n'                 
                                      'Сагинбаева Шырайлым Кыдыргалиевна - Заместитель руководителя по произведственному обучению\n \n'
                                      'Исакова Айгуль Ерденевна - Заведующий отделением\n \n'
                                      'Избасканова Улбосын Бектасовна - Заведующий отделением\n \n'
                                      'Мукашева Жанаргуль Туякбаевна - Заведующий отделением\n \n'
                                      'Айтимова Кызгалдак Елтаевна - Руководитель отдела кадров\n \n'
                                      'Аженова Карлыгаш Султаналиевна - Преподователь специальных дисциплин по специальности "Швейное производство и моделирование одежды"\n \n'
                                      'Айтхожина-Сагатова Шнар Ауезхановна - Преподаватель казахского языка и литературы\n \n'
                                      'Бурумбаев Арман Орупаевич - Преподователь специальных дисциплин по специальности "Графический и мультимедийный дизайн"\n \n'
                                      'Жексенбинова Шырын Ержигитовна - Преподователь истории\n \n'
                                      'Жакыпкожин Айдар Аскербекович - Преподователь начальной военной подготовки\n \n'
                                      'Заркум Мадина - Преподователь физической культуры\n \n'
                                      'Игнатова Ирина Александровна - Мастер по производственному обучению "Парикмахерское искусство и декоративная косметика"\n \n'
                                      'Игамбедиева Акерке Нишоналикизи - Преподаватель специальных дисциплин по специальности "Вычислительная техника и информационные сети","Программное обеспечение"\n \n'
                                      'Калиева Жамиля Тусуповна - Преподователь казахского языка\n \n'
                                      'Омарова Мейрамкуль Тлеукеновна - Преподаватель специальных дисциплин по специальности "Вычислительная техника и программное обеспечение"\n \n'
                                      'Тургамбаева Гульмира Сабыржановна - Преподователь химии и биологии\n \n'
                                      'Тусупова Гульзира Нуркеновна - Преподователь истории\n \n'
                                      'Нурмагамбетов Ерлик Жанатлекович - Преподаватель специальных дисциплин по специальности "Дизайн"\n \n'
                                      'Мусина Салтанат Амангельдыевна - Преподователь английского языка\n \n'
                                      'Жалмуханова Самал Жиенбаевна - Преподователь экономических дисциплин\n \n'
                                      'Устюгова Анна Валерьевна - Мастер по производственному обучению по специальности "Организация питания"\n \n')


@bot.message_handler(commands=['location'])
def location(message):
  bot.send_message(message.chat.id, 'Адрес колледжа: \nг. Астана проспект Женис 68 а')


@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, 'Правила приема на обучение на 2023-2024 учебный год')


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://kmib.edu.kz')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Команды бота \n'
                                      '1) Чтобы узнать адрес коледжа - /location \n'
                                      '2) Информация о поступлении - /info \n'
                                      '3) Специальности - /specialties \n'
                                      '4) Сайт коледжа - /site  \n'
                                      '5) Контакты - /contacts\n'
                                      '6) Наш колектив - /colective')

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, "Извините, я не понимаю этот вопрос. Пожалуйста, используйте /help для просмотра доступных команд.")


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.reply_to(message, 'Красивое фото')



bot.infinity_polling(timeout=10, long_polling_timeout = 5)
