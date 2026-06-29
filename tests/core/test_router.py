from contextlib import asynccontextmanager
from unittest.mock import AsyncMock, MagicMock

import pytest

from core import router
from core.adapter import IncomingMessage
from core.db.models import Message


class _FakeSession:
    def __init__(self, added: list[Message]) -> None:
        self._added = added
        self.commit = AsyncMock()

    def add(self, obj: object) -> None:
        assert isinstance(obj, Message)
        self._added.append(obj)


@pytest.fixture
def captured_messages(monkeypatch: pytest.MonkeyPatch) -> list[Message]:
    added: list[Message] = []

    @asynccontextmanager
    async def fake_get_session():
        yield _FakeSession(added)

    monkeypatch.setattr(router, "get_session", fake_get_session)
    return added


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "text, expected",
    [
        ("/start", router.START_REPLY),
        ("/help", router.HELP_REPLY),
        ("/ping", router.PING_REPLY),
        ("/unknowncmd", router.UNKNOWN_COMMAND_REPLY),
        ("hello there", router.TEXT_FALLBACK_REPLY),
    ],
)
async def test_handle_message_routes_and_persists(
    captured_messages: list[Message], text: str, expected: str
) -> None:
    reply = await router.handle_message(IncomingMessage(chat_id=1, text=text))

    assert reply == expected
    assert [(m.role, m.content) for m in captured_messages] == [
        ("user", text),
        ("assistant", expected),
    ]


@pytest.mark.asyncio
async def test_handle_message_commits_each_persist(monkeypatch: pytest.MonkeyPatch) -> None:
    session = MagicMock()
    session.add = MagicMock()
    session.commit = AsyncMock()

    @asynccontextmanager
    async def fake_get_session():
        yield session

    monkeypatch.setattr(router, "get_session", fake_get_session)

    await router.handle_message(IncomingMessage(chat_id=1, text="hi"))

    assert session.commit.await_count == 2
