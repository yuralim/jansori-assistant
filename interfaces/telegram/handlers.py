import logging

from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)

START_REPLY = (
    "Hi, I'm Jansori — your slightly nagging personal assistant. "
    "Send /help to see what I can do so far."
)

HELP_REPLY = (
    "Available commands:\n"
    "/start - greet and introduce me\n"
    "/help - show this message\n"
    "/ping - check that I'm alive"
)


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


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.effective_message
    user = update.effective_user
    if message is None:
        logger.warning("received /start without an effective message")
        return

    logger.info(
        "received /start chat_id=%s user_id=%s text=%r",
        message.chat_id,
        user.id if user else None,
        message.text,
    )
    await message.reply_text(START_REPLY)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.effective_message
    user = update.effective_user
    if message is None:
        logger.warning("received /help without an effective message")
        return

    logger.info(
        "received /help chat_id=%s user_id=%s text=%r",
        message.chat_id,
        user.id if user else None,
        message.text,
    )
    await message.reply_text(HELP_REPLY)
