import time
import telebot

bot = telebot.TeleBot('6102482906:AAFzv89CWk55lYUY7YcNd1Kx3L7OW8IaGng')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет,<b>{message.from_user.full_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


    for i in range(20):
        with open('flowers.jpg', 'rb') as f:
            bot.send_message(message.chat.id, 'Вам букетик!', parse_mode='html')
            bot.send_photo(message.chat.id, f)
            time.sleep(60*30)

bot.polling(none_stop=True)