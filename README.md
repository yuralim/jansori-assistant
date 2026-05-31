# jansori-assistant
An AI-powered personal assistant project focused on habit management, routine building, and realistic daily accountability.

See [docs/](docs/) for project overview and roadmap.

## Run the Telegram bot

1. Create a bot with [@BotFather](https://t.me/BotFather) on Telegram and copy the token.
2. Copy `.env.example` to `.env` and paste the token:
   ```sh
   cp .env.example .env
   ```
3. Install dependencies:
   ```sh
   uv sync
   ```
4. Start the bot (polling mode):
   ```sh
   uv run python main.py
   ```
5. In Telegram, DM the bot:
   - `/start` — get a short introduction
   - `/help` — list the available commands
   - `/ping` — should reply `pong`

   Any other command or plain text message gets a short fallback reply pointing back to `/help`.

Run tests with:
```sh
uv run pytest
```
