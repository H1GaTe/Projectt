import telebot
from telebot import types
import asyncio

# Инициализация бота с вашим токеном
bot = telebot.TeleBot('6610256377:AAExQcLJdXDVg0uZkgi4xiU3tPGqXbjRDP4')

# Переменная для хранения данных фото
photo_data = None

def load_photo():
    global photo_data
    with open('ваше фото.jpeg', 'rb') as file:
        photo_data = file.read()

@bot.message_handler(commands=['start'])
async def start(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('Наш Веб сайт')
    btn4 = types.KeyboardButton('О нас')
    markup.row(btn1, btn4)
    btn2 = types.KeyboardButton('Помощь')
    markup.row(btn2)
    
    # Отправляем фото из предварительно загруженных данных
    await bot.send_photo(message.chat.id, photo_data, caption='Ваш текст', reply_markup=markup)
    
    # Регистрируем обработчик следующего шага
    await bot.register_next_step_handler(message, one_click)

async def one_click(message):
    # Пример функции, которая будет вызвана после нажатия на любую кнопку
    if message.text == 'Наш Веб сайт':
        await bot.send_message(message.chat.id, 'Вот ссылка на наш вебсайт: https://example.com')
    elif message.text == 'О нас':
        await bot.send_message(message.chat.id, 'Мы - команда, которая делает что-то важное.')
    elif message.text == 'Помощь':
        await bot.send_message(message.chat.id, 'Какую помощь вам нужна?')
    else:
        await bot.send_message(message.chat.id, 'Извините, я не понимаю эту команду.')

if __name__ == "__main__":
    # Загружаем фото при старте бота
    load_photo()
    
    # Запуск бота с поддержкой асинхронной обработки
    asyncio.run(bot.polling(none_stop=True))