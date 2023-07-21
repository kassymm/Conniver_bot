from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor
import os
from handlers.handlers import send_welcome, tts, echo
import json
load_dotenv()


ID = os.getenv("ID")
API_KEY = os.getenv("API_KEY")
HEADERS = {
    "accept": "application/json",
    "content-type": "application/json",
    "AUTHORIZATION": API_KEY,
    "X-USER-ID": ID,
}

BOT_TOKEN = os.getenv("BOT_TOKEN")

# initialize the bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


dp.register_message_handler(send_welcome, commands=['start', 'help'])


dp.register_message_handler(tts, commands='tts')


dp.register_message_handler(echo)

menu = ['Start', 'Text to speech']

bot.set_chat_menu_button(menu_button=json.dumps(menu))


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
