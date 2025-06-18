from gtts import gTTS
from telegram import Bot
from datetime import datetime
import time
import os

# Environment variables (use Railway's dashboard)
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

def send_reminder():
    now = datetime.now().strftime("%I:%M %p")
    message = f"Hello! It's {now}. Please check your daily task."
    tts = gTTS(text=message, lang='en')
    tts.save("reminder.mp3")

    with open("reminder.mp3", "rb") as voice:
        bot.send_voice(chat_id=CHAT_ID, voice=voice)

if __name__ == "__main__":
    while True:
        current = datetime.now().strftime("%H:%M")
        if current in ["08:00", "13:00", "20:00"]:  # customize your times
            send_reminder()
            time.sleep(60)
        time.sleep(10)
