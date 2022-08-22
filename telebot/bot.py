import telebot
import configure
from telebot import types

client = telebot.TeleBot(configure.config['token'])

@client.message_handler(content_types = ['text', 'document', 'audio'])
def get_text(message):
        if message.text.lower() == 'мне грустно':
            client.send_message(message.chat.id, 'ты самая лучшая девочка в мире, я люблю тебя больше всего на свете Аке!!!❤')
        elif message.text.lower() == 'я скучаю':
            client.send_message(message.chat.id, 'малыш, я тоже очень скучаю, но я сейчас немножко занят. скоро напишу!!! люблю тебя малыш!❤❤')    
        elif message.text.lower() == 'я хочу печеньку!':
            client.send_message(message.chat.id, 'вот твоя печенька!🍪 ' )   
        elif message.text.lower() == 'как с тобой говорить?':
            client.send_message(message.chat.id, 'напиши что-то из этого : "я хочу печеньку!", "я скучаю", "мне грустно"' )



client.polling(none_stop = True, interval = 0)            