import logging
import uuid

from core.adapter import IncomingMessage
from core.db.engine import get_session
from core.db.models import Message
from core.logging import request_id

logger = logging.getLogger(__name__)

START_REPLY = "안녕! 나는 소리야. 오늘은 뭘 하고 싶어? 도움이 필요하면 /help 를 입력해줘."

HELP_REPLY = (
    "지금은 기본 명령어만 사용할 수 있어. /start 로 다시 시작할 수 있고, "
    "앞으로 할 일 관리와 리마인더 기능을 하나씩 배워갈 예정이야."
)

PING_REPLY = "pong"

UNKNOWN_COMMAND_REPLY = "아직 모르는 명령어야. 사용할 수 있는 명령어를 보려면 /help 를 입력해줘."

TEXT_FALLBACK_REPLY = "알았어. 아직은 간단한 답장만 할 수 있지만, 앞으로는 더 똑똑하게 도와줄게."


def _route(text: str) -> str:
    if text.startswith("/start"):
        return START_REPLY
    if text.startswith("/help"):
        return HELP_REPLY
    if text.startswith("/ping"):
        return PING_REPLY
    if text.startswith("/"):
        return UNKNOWN_COMMAND_REPLY
    return TEXT_FALLBACK_REPLY


async def _persist(role: str, content: str) -> None:
    async with get_session() as session:
        session.add(Message(role=role, content=content))
        await session.commit()


async def handle_message(incoming: IncomingMessage) -> str:
    request_id.set(uuid.uuid4().hex[:8])
    logger.info(
        "handling message chat_id=%s text=%r",
        incoming.chat_id,
        incoming.text,
    )

    await _persist(role="user", content=incoming.text)
    reply = _route(incoming.text)
    await _persist(role="assistant", content=reply)
    return reply
