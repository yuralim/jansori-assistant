import os

from dotenv import load_dotenv

from adapters.telegram.bot import TelegramAdapter
from core.logging import configure_logging
from core.router import handle_message


def run() -> None:
    load_dotenv()

    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        raise RuntimeError("TELEGRAM_BOT_TOKEN is not set")

    configure_logging()

    adapter = TelegramAdapter(token=token, handler=handle_message)
    adapter.start()


if __name__ == "__main__":
    run()
