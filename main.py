import os
from telegram import Bot
from dotenv import load_dotenv
import asyncio

load_dotenv()

async def main():
    bot=Bot(os.getenv("BOT_TOKEN"))
    chat=os.getenv("CHAT_ID")
    await bot.send_message(chat_id=chat,text="✅ Código Rescate está funcionando.")

asyncio.run(main())
