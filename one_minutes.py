import telegram
import schedule
import time
import datetime
import pytz

token = "6801716374:AAHf9y6oCdGKPLRvXG3vHvNNgVSIoZxhPWA"
public_chat_name = '@OS_kgu'

def send_message():
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=public_chat_name, text="alarm arrived!!!!!")

def job():
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    if 6 <= now.hour < 23:
        send_message()

# Schedule the job to run every 30 minutes
schedule.every(30).minutes.do(job)

def main():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()