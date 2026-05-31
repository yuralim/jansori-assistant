from unittest.mock import AsyncMock, MagicMock

import pytest

from interfaces.telegram.handlers import help_command, ping, start


def _make_update(text: str):
    update = MagicMock()
    update.message = MagicMock()
    update.message.reply_text = AsyncMock()
    update.message.chat_id = 123
    update.message.text = text
    update.effective_message = update.message
    update.effective_user = MagicMock()
    update.effective_user.id = 456
    return update


@pytest.mark.asyncio
async def test_ping_replies_pong():
    update = _make_update("/ping")
    context = MagicMock()

    await ping(update, context)

    update.message.reply_text.assert_awaited_once_with("pong")


@pytest.mark.asyncio
async def test_ping_replies_to_effective_message():
    update = MagicMock()
    update.message = None
    update.effective_message = MagicMock()
    update.effective_message.reply_text = AsyncMock()
    update.effective_message.chat_id = 123
    update.effective_message.text = "/ping"
    update.effective_user = MagicMock()
    update.effective_user.id = 456

    context = MagicMock()

    await ping(update, context)

    update.effective_message.reply_text.assert_awaited_once_with("pong")


@pytest.mark.asyncio
async def test_start_greets_user():
    update = _make_update("/start")
    context = MagicMock()

    await start(update, context)

    update.message.reply_text.assert_awaited_once()
    reply = update.message.reply_text.await_args.args[0]
    assert "Jansori" in reply
    assert "/help" in reply


@pytest.mark.asyncio
async def test_help_lists_commands():
    update = _make_update("/help")
    context = MagicMock()

    await help_command(update, context)

    update.message.reply_text.assert_awaited_once()
    reply = update.message.reply_text.await_args.args[0]
    assert "/start" in reply
    assert "/help" in reply
    assert "/ping" in reply
