import os
import telebot
import yt_dlp

TOKEN = "8353491200:AAFJHFeXKu4dpdQFKVBVF_ZLMCaf_odg8Xg"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! أرسل لي رابط الفيديو وسأقوم بتحميله.")

@bot.message_handler(func=lambda message: True)
def download_video(message):
    url = message.text
    bot.reply_to(message, "جاري المعالجة والتحميل...")
    try:
        ydl_opts = {'outtmpl': '%(id)s.%(ext)s'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
        with open(filename, 'rb') as video:
            bot.send_video(message.chat.id, video)
        os.remove(filename)
    except Exception as e:
        bot.reply_to(message, f"حدث خطأ: {e}")

bot.infinity_polling()
tots  
