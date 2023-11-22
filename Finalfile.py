import telegram
import schedule
import time
import datetime
import pytz

token = "6801716374:AAHf9y6oCdGKPLRvXG3vHvNNgVSIoZxhPWA"
public_chat_name = "@OS_kgu"

async def send_message_async():
    bot = telegram.Bot(token=token)
    return await bot.sendMessage(chat_id=public_chat_name, text="alarm arrived!!!!!")

def job():
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    if now.hour >= 23 or now.hour <= 6:
        return

# Schedule the job to run every 30 minute
schedule.every(30).minutes.do(job)
async def main():
    while True:
        await send_message_async()
        schedule.run_pending()
        time.sleep(1800)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())


