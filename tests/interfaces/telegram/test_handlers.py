from unittest.mock import AsyncMock, MagicMock

import pytest

from interfaces.telegram.handlers import ping


@pytest.mark.asyncio
async def test_ping_replies_pong():
    update = MagicMock()
    update.message = MagicMock()
    update.message.reply_text = AsyncMock()
    update.message.chat_id = 123
    update.message.text = "/ping"
    update.effective_message = update.message
    update.effective_user = MagicMock()
    update.effective_user.id = 456

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
