import logging
from config.settings import settings

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="Hi, from Python code"
    )


def run_bot():
    application = ApplicationBuilder().token(settings.TELEGRAM_BOT_KEY).build()
    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)
    application.run_polling()
