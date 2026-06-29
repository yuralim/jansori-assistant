from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class IncomingMessage:
    chat_id: int
    text: str


MessageHandler = Callable[[IncomingMessage], Awaitable[str | None]]


class Adapter(Protocol):
    async def send_message(self, chat_id: int, text: str) -> None: ...

    def start(self) -> None: ...
