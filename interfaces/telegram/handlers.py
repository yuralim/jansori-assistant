import logging

from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.effective_message
    user = update.effective_user
    if message is None:
        logger.warning("received /ping without an effective message")
        return

    logger.info(
        "received /ping chat_id=%s user_id=%s text=%r",
        message.chat_id,
        user.id if user else None,
        message.text,
    )
    await message.reply_text("pong")
