import telegram
import asyncio
token = "6801716374:AAHf9y6oCdGKPLRvXG3vHvNNgVSIoZxhPWA"
# Bot: OS_kgu_bot
# Token: 6801716374:AAHf9y6oCdGKPLRvXG3vHvNNgVSIoZxhPWA
# chat_id: 6436398215
bot = telegram.Bot(token = token)
chat_id = "6436398215"
text = '이건 또 다른 것인가?'
asyncio.run(bot.sendMessage(chat_id = chat_id , text=text))