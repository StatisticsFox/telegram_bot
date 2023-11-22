import telegram
import schedule
import time
import datetime
import pytz
'''
token = "6801716374:AAHf9y6oCdGKPLRvXG3vHvNNgVSIoZxhPWA"
# Bot: OS_kgu_bot
# Token: 6801716374:AAHf9y6oCdGKPLRvXG3vHvNNgVSIoZxhPWA
chat_id: 6436398215
# channel : OS_kgu
bot = telegram.Bot(token = token)
public_chat_name = '@OS_kgu'
id_channel = bot.sendMessage(chat_id=public_chat_name, 
                             text="alarm arrived!!!!!").chat_id


def job():
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    if now.hour >= 23 or now.hour <= 6:
        return

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
'''
token = "6801716374:AAHf9y6oCdGKPLRvXG3vHvNNgVSIoZxhPWA"
public_chat_name = '@OS_kgu'

async def send_message_async():
    bot = telegram.Bot(token=token)
    return await bot.sendMessage(chat_id=public_chat_name, text="alarm arrived!!!!!")

def job():
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    if now.hour >= 23 or now.hour <= 6:
        return

# Schedule the job to run every 1 minute
schedule.every(30).minutes.do(job)

async def main():
    while True:
        await send_message_async()
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())








'''
async def job():
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    if now.hour >= 23 or now.hour <= 6:
        return
    # await asyncio.to_thread(bot.sendMessage, public_chat_name, "alarm arrived!!!!!")

def main():
    schedule.every(1).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())





'''