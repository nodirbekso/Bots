import telebot
import urllib3.util
from telebot import types

bot = telebot.TeleBot("5505615342:AAFYXu7sJMiZlNztqLfaPOMu457YjbInCFU")


@bot.message_handler(commands=["start"])
def start(message):
    mess = f"Ассалому алайкум <b>{message.from_user.first_name} </b> "
    bot.send_message(message.chat.id, mess, parse_mode="html")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    beeline = types.KeyboardButton('Beeline')
    uzmobile = types.KeyboardButton('Uzmobile')
    ucell = types.KeyboardButton('Ucell')
    mobiuz = types.KeyboardButton('MobiUz')
    markup.add(beeline, uzmobile, ucell, mobiuz)
    bot.send_message(message.chat.id, 'web saytlarga', reply_markup=markup)


# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == "Assalomu alaykum" or message.text == "Ассалому алайкум":
#         mess = "Ва алайкум ассалом ва рохматуллохи ва барокатуху!!!"
#         bot.send_message(message.chat.id, mess, parse_mode="html")
#
#     elif message.text == "id":
#         mess = f"Сизнинг Id: {message.from_user.id}"
#         bot.send_message(message.chat.id, mess, parse_mode="html")
#
#     elif message.text=="foto" or message.text=="photo":
#         photo=open('iam.jpg','rb')
#         bot.send_photo(message.chat.id, photo)
#
#     elif message.text == "Локация":
#         bot.send_location(message.chat.id, 40.313556, 72.321125 )
#     else:
#         mess="Нормальный гаплашелик!!!"
#         bot.send_message(message.chat.id, mess, parse_mode="html")
@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, "Ваще ю а ?")


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Beeline", url='http://beeline.uz'))
    bot.send_message(message.chat.id, 'Beeline web saytiga', reply_markup=markup)


bot.polling(none_stop=True)
