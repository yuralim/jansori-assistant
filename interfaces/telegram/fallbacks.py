import logging

from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)

UNKNOWN_COMMAND_REPLY = "I don't recognize that command. Try /help."

TEXT_FALLBACK_REPLY = (
    "I can only respond to commands right now. Try /help to see what's available."
)


async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.effective_message
    user = update.effective_user
    if message is None:
        logger.warning("received unknown command without an effective message")
        return

    logger.info(
        "received unknown command chat_id=%s user_id=%s text=%r",
        message.chat_id,
        user.id if user else None,
        message.text,
    )
    await message.reply_text(UNKNOWN_COMMAND_REPLY)


async def text_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.effective_message
    user = update.effective_user
    if message is None:
        logger.warning("received text message without an effective message")
        return

    logger.info(
        "received text message chat_id=%s user_id=%s text=%r",
        message.chat_id,
        user.id if user else None,
        message.text,
    )
    await message.reply_text(TEXT_FALLBACK_REPLY)
