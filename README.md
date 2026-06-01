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
   - `/help` — show a short help message
   - `/ping` — should reply `pong`

   Any other command or plain text message gets a short fallback reply.

## Database

Start a local Postgres (Docker required) and run migrations:
```sh
make db-up
make db-migrate
```
Stop it with `make db-down`. The connection string is set via `DATABASE_URL` in `.env`.

## Development

Run unit tests (default — no external services):
```sh
uv run pytest
```

Run integration tests (requires Docker; a Postgres container is started automatically via Testcontainers):
```sh
make test-integration
```

Format and lint with [Ruff](https://docs.astral.sh/ruff/):
```sh
make format    # or: uv run ruff format .
make lint   # or: uv run ruff check .
```

Install git pre-commit hooks (one time, after `uv sync`):
```sh
make install-hooks
```
Run all hooks against the repo:
```sh
make precommit
```
