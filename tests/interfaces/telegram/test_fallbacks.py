from unittest.mock import AsyncMock, MagicMock

import pytest

from interfaces.telegram.fallbacks import text_message, unknown_command


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
async def test_unknown_command_suggests_help():
    update = _make_update("/bogus")
    context = MagicMock()

    await unknown_command(update, context)

    update.message.reply_text.assert_awaited_once()
    reply = update.message.reply_text.await_args.args[0]
    assert "/help" in reply


@pytest.mark.asyncio
async def test_text_message_falls_back():
    update = _make_update("hello there")
    context = MagicMock()

    await text_message(update, context)

    update.message.reply_text.assert_awaited_once()
    reply = update.message.reply_text.await_args.args[0]
    assert "똑똑하게" in reply
