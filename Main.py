import schedule
import time
from telegram import Bot

TELEGRAM_TOKEN = 'your_token_here'
CHAT_ID = 'your_chat_id_here'

bot = Bot(token=TELEGRAM_TOKEN)

daily_tasks = [
    {"time": "07:00", "task": "Wake up and stretch"},
    {"time": "09:00", "task": "Start your work"},
    {"time": "13:00", "task": "Lunch Time"},
    {"time": "15:00", "task": "Quick meditation break"},
    {"time": "20:00", "task": "Dinner Time"},
    {"time": "22:30", "task": "Prepare to sleep"},
]

def notify(task):
    bot.send_message(chat_id=CHAT_ID, text=f"🔔 Reminder: {task}")

for t in daily_tasks:
    schedule.every().day.at(t["time"]).do(notify, task=t["task"])

while True:
    schedule.run_pending()
    time.sleep(1)
