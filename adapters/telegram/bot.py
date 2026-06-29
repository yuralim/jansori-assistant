import logging

from telegram import Update
from telegram.ext import Application, ApplicationBuilder, ContextTypes, MessageHandler, filters

from core.adapter import IncomingMessage
from core.adapter import MessageHandler as CoreMessageHandler

logger = logging.getLogger(__name__)


class TelegramAdapter:
    def __init__(self, token: str, handler: CoreMessageHandler) -> None:
        self._handler = handler
        self._app: Application = ApplicationBuilder().token(token).build()
        self._app.add_handler(MessageHandler(filters.ALL, self._on_update))

    async def send_message(self, chat_id: int, text: str) -> None:
        await self._app.bot.send_message(chat_id=chat_id, text=text)

    def start(self) -> None:
        logger.info("Telegram bot starting (polling mode)")
        self._app.run_polling()

    async def _on_update(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        message = update.effective_message
        if message is None:
            logger.warning("received update without an effective message")
            return

        incoming = IncomingMessage(chat_id=message.chat_id, text=message.text or "")
        reply = await self._handler(incoming)
        if reply is not None:
            await self.send_message(message.chat_id, reply)
