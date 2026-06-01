import logging
import uuid

from telegram import Update
from telegram.ext import ContextTypes

from core.logging import request_id

logger = logging.getLogger(__name__)

START_REPLY = "안녕! 나는 소리야. 오늘은 뭘 하고 싶어? 도움이 필요하면 /help 를 입력해줘."

HELP_REPLY = (
    "지금은 기본 명령어만 사용할 수 있어. /start 로 다시 시작할 수 있고, "
    "앞으로 할 일 관리와 리마인더 기능을 하나씩 배워갈 예정이야."
)


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    request_id.set(uuid.uuid4().hex[:8])
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
    request_id.set(uuid.uuid4().hex[:8])
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
    request_id.set(uuid.uuid4().hex[:8])
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
