from telebot import types, TeleBot
from random import randint
import pathlib
import os

work_dir = pathlib.Path(__file__).parent.absolute()
bot = TeleBot('TOKEN')

hello = [
    	'music/Hello/privetkigovnoed.ogg',
		'music/Hello/zdarovachertila.ogg',
		'music/Hello/hulipripersya.ogg',
    ]

history = [
    	'music/History/idinahui.ogg',
		'music/History/istioriahuynya.ogg',
		'music/History/nihuyaneponyatno.ogg',
		'music/History/prospis.ogg',
		'music/History/putinpomozhet.ogg',
    ]


def hello_audio(message,hello=hello):
	with open(os.path.join(work_dir, hello[randint(0, len(hello)) - 1]), 'rb') as f:
	    bot.send_audio(message.chat.id, f)


def history_audio(message, history=history):
	with open(os.path.join(work_dir, history[randint(0, len(history)) - 1]), 'rb') as f:
	    bot.send_audio(message.chat.id, f)


def manifest_audio(message):
	with open(os.path.join(work_dir, 'music/manifest.mp3'), 'rb') as f:
	    bot.send_audio(message.chat.id, f)


def open_video(message):
    with open(os.path.join(work_dir, 'video/TUTORIAL.MP4'), 'rb') as f:
        bot.send_video(message.chat.id, f)


def open_hat(message):
	with open(os.path.join(work_dir, 'img/chort_hat.png'), 'rb') as f:
	    bot.send_document(message.chat.id, f)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	markup = types.ReplyKeyboardMarkup(row_width=2)
	btn1 = types.KeyboardButton('Привет')
	btn2 = types.KeyboardButton('Шапка')
	btn3 = types.KeyboardButton('Манифест')
	btn4 = types.KeyboardButton('Догмы')
	btn5 = types.KeyboardButton('Рассказать историю')
	markup.add(btn1, btn2, btn3, btn4, btn5)
	bot.send_message(message.chat.id, "Добро пожаловать к чертовому боту, мне ты можешь рассказать свою историю и\
	 я тебе обязательно помогу. А так же можешь воспользоваться моими командами для того, чтобы все о нас узнать", reply_markup=markup)
	hello_audio(message)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	if message.text == 'Привет':
		hello_audio(message)
	elif message.text == 'Шапка':
		open_hat(message)
		bot.send_message(message.chat.id, 'Ссылка на стикерпак: https://t.me/addstickers/CHERTKLASSIK')
		open_video(message)
	elif message.text == 'Догмы':
		bot.send_message(message.chat.id, 'Догмы Chort Classique 👹\n\n• Никто не поднимает тему настольных игр. Никогда.\n\n \
• Когда Молчание разрушает общество, мы делаем «Бип».\n\n • Образцовый участник не забывает одну минуту в сутки прощать Владимира Владимировича Путина. В 1:11 часов ночи по Москве.\n\n \
• Покидая комнату, надо прощаться.\n\n • Все, что говорит чорт - есть истина! Извиняться нельзя.')
	elif message.text == 'Манифест':
		manifest_audio(message)
	elif message.text == 'Рассказать историю':
		bot.send_message(message.chat.id, 'Напиши свою чертовски интересную историю, чтобы получить самый полезный совет')
	else:
		history_audio(message)


bot.polling(none_stop=True, interval=1)
