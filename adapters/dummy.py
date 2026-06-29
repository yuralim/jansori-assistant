from core.adapter import IncomingMessage, MessageHandler


class DummyAdapter:
    def __init__(self, handler: MessageHandler) -> None:
        self.sent: list[tuple[int, str]] = []
        self._handler = handler

    async def send_message(self, chat_id: int, text: str) -> None:
        self.sent.append((chat_id, text))

    def start(self) -> None:
        pass

    async def simulate_incoming(self, chat_id: int, text: str) -> str | None:
        reply = await self._handler(IncomingMessage(chat_id=chat_id, text=text))
        if reply is not None:
            await self.send_message(chat_id, reply)
        return reply
