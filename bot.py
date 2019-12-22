import telebot
from telebot import types
from telebot.types import Message
import Pars as p
TOKEN = '934588759:AAGZLc_5-hfd824gkwCGyn3_TZKiP6abtSg'
bot = telebot.TeleBot(TOKEN)

ans_f = p.get_football()
ans_b = p.get_basketball()
print(ans_b[1][3])

@bot.message_handler(commands=['start','начать'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Рады вас видеть 🤩 🤩 🤩 🤩', reply_markup = keyboard())

@bot.message_handler(content_types=["text"])
def send_anything(message):
    chat_id = message.chat.id
    if message.text == '🏈 Soccer' :
        text1 = '👇🏻 вот список матчей по футболу'
        bot.send_message(chat_id, text1)
        for i in range(len(ans_f)):
            bot.send_message(chat_id, '{} ДАТА {} в {} 💥💥💥💥💥 {} 🔛 {}'.format(ans_f[i][4],ans_f[i][2],ans_f[i][3],ans_f[i][0],ans_f[i][1]))
    elif message.text == '🏀 Basketball':
        text2 = '👇🏻 вот список матчей по баскетболу'
        bot.send_message(chat_id, text2)
        for i in range(len(ans_b)):
            bot.send_message(chat_id, '{} в {} 💥💥💥💥💥 {} 🆚 {}'.format(ans_b[i][1],ans_b[i][0],ans_b[i][2],ans_b[i][3]))

def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True)
    btn1 = types.KeyboardButton('🏈 Soccer')
    btn2 = types.KeyboardButton('🏀 Basketball')
    markup.add(btn1)
    markup.add(btn2)
    return markup

bot.polling()
