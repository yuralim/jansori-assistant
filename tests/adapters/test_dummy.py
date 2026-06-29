import pytest

from adapters.dummy import DummyAdapter
from core.adapter import IncomingMessage


@pytest.mark.asyncio
async def test_simulate_incoming_invokes_handler_and_records_reply():
    received: list[IncomingMessage] = []

    async def handler(incoming: IncomingMessage) -> str:
        received.append(incoming)
        return f"echo:{incoming.text}"

    adapter = DummyAdapter(handler=handler)

    reply = await adapter.simulate_incoming(chat_id=42, text="hi")

    assert reply == "echo:hi"
    assert received == [IncomingMessage(chat_id=42, text="hi")]
    assert adapter.sent == [(42, "echo:hi")]


@pytest.mark.asyncio
async def test_simulate_incoming_skips_send_when_handler_returns_none():
    async def handler(_: IncomingMessage) -> None:
        return None

    adapter = DummyAdapter(handler=handler)

    reply = await adapter.simulate_incoming(chat_id=1, text="hello")

    assert reply is None
    assert adapter.sent == []


@pytest.mark.asyncio
async def test_send_message_records_payload():
    async def handler(_: IncomingMessage) -> None:
        return None

    adapter = DummyAdapter(handler=handler)

    await adapter.send_message(chat_id=7, text="direct")

    assert adapter.sent == [(7, "direct")]
