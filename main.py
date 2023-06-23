import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot('5887209531:AAEP7xXzLeRh30QsLTlOqzc-fAISKaYwhYQ')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn1 = types.KeyboardButton("/获取代理")
    btn2 = types.KeyboardButton("/get")
    btn3 = types.KeyboardButton("/get")
    markup.add(btn1,btn2,btn3)
    # 创建信息
    chat_msg = '风浪越大'
    # 创建按钮
    button_url = InlineKeyboardButton('官方频道', url='https://t.me/faka8866')
    keyboard = [[button_url]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # 发送图片消息
    bot.send_message(chat_id=message.chat.id, text=chat_msg, reply_markup=markup)


@bot.message_handler(commands=['获取代理'])
def send_welcome(message):
    # 创建信息
    chat_msg = '代理均可点击连接 \n\n代理连接等待10s'
    # 创建按钮
    button_url = InlineKeyboardButton('官方频道', url='https://t.me/faka8866')
    button_url_two = InlineKeyboardButton('官方频道', url='https://t.me/faka8866')
    keyboard = [
        [button_url],
        [button_url_two]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # 发送图片消息
    bot.send_message(chat_id=message.chat.id, text=chat_msg, reply_markup=reply_markup)


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(reply_to_message_id=message.message_id, chat_id=message.chat.id, text='有什么可以帮您')


if __name__ == '__main__':
    bot.polling()
