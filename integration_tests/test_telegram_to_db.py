from sqlalchemy import select

from adapters.dummy import DummyAdapter
from core.db.engine import get_session
from core.db.models import Message
from core.router import PING_REPLY, handle_message


async def test_simulate_incoming_persists_user_and_assistant_messages() -> None:
    adapter = DummyAdapter(handler=handle_message)

    reply = await adapter.simulate_incoming(chat_id=123, text="/ping")

    assert reply == PING_REPLY
    assert adapter.sent == [(123, PING_REPLY)]

    async with get_session() as session:
        result = await session.execute(select(Message).order_by(Message.id))
        rows = [(m.role, m.content) for m in result.scalars().all()]

    assert rows == [
        ("user", "/ping"),
        ("assistant", PING_REPLY),
    ]
