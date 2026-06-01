from sqlalchemy import select

from core.db.engine import get_session
from core.db.models import Message


async def test_message_crud_roundtrip() -> None:
    async with get_session() as session:
        msg = Message(role="user", content="hello", tokens_in=3, tokens_out=None)
        session.add(msg)
        await session.commit()
        await session.refresh(msg)
        inserted_id = msg.id

    assert inserted_id is not None

    async with get_session() as session:
        result = await session.execute(select(Message).where(Message.id == inserted_id))
        fetched = result.scalar_one()
        assert fetched.role == "user"
        assert fetched.content == "hello"
        assert fetched.tokens_in == 3
        assert fetched.tokens_out is None
        assert fetched.created_at is not None
