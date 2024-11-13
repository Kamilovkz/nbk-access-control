from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes
import os
from dotenv import load_dotenv
from pathlib import Path


dotenv_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=dotenv_path)
telegram_key = os.getenv("TEST_VARIANT")
print(f"{telegram_key} is this data is working and fetchinig data")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, I'm your bot!")


appication = ApplicationBuilder().token("")
