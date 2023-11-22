import telegram
import schedule
import time
import datetime
import pytz
import asyncio

token = "6801716374:AAHf9y6oCdGKPLRvXG3vHvNNgVSIoZxhPWA"
public_chat_name = "@OS_kgu"

async def send_message_async():
    bot = telegram.Bot(token=token)
    return await bot.sendMessage(chat_id=public_chat_name, text="alarm arrived!!!!!")

def job():
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    if now.hour >= 23 or now.hour <= 6:
        return

# Schedule the job to run every 30 minutes
schedule.every(30).minutes.do(job)

async def main():
    while True:
        await send_message_async()
        schedule.run_pending()
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
