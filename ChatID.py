import telegram
token = "6801716374:AAHf9y6oCdGKPLRvXG3vHvNNgVSIoZxhPWA"
# Bot: OS_kgu_bot
# Token: 6801716374:AAHf9y6oCdGKPLRvXG3vHvNNgVSIoZxhPWA
# chat_id: 6801716374
bot = telegram.Bot(token = token)
updates = bot.get_updates()
for u in updates:
    print(u.message['chat']['id'])  