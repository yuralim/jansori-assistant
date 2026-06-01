import logging

from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)

UNKNOWN_COMMAND_REPLY = "아직 모르는 명령어야. 사용할 수 있는 명령어를 보려면 /help 를 입력해줘."

TEXT_FALLBACK_REPLY = "알았어. 아직은 간단한 답장만 할 수 있지만, 앞으로는 더 똑똑하게 도와줄게."


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
