import logging
import os

from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler

from interfaces.telegram.handlers import ping

logger = logging.getLogger(__name__)


def run() -> None:
    load_dotenv()

    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        raise RuntimeError("TELEGRAM_BOT_TOKEN is not set")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s - %(message)s",
    )

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("ping", ping))

    logger.info("Telegram bot starting (polling mode)")
    app.run_polling()
