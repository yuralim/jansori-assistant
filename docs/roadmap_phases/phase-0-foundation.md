Phase 0 Milestone definition and issue list for GitHub Project/Issues management. Each issue is scoped so it can be closed with a single PR.

---

## Milestone: `Phase 0: Foundation`

**Description:** The thinnest possible end-to-end pipeline where sending a message on Telegram results in a Jansori-style reply. The persona tone is established, and costs are controllable.

**Duration:** ~2 weeks (loosely)

**Definition of Done**

1. Casual conversation on Telegram → Jansori-tone reply comes back
2. Automatically stop API calls when the daily token cap is reached
3. `interface adapter` interface exists so other channels can be swapped in later
4. Local and production environments are separated

---

## Issues

Recommended order based on dependencies.

### #1 Repo Bootstrap & Project Structure Setup

* **Labels:** `chore`, `phase-0`
* **Description:** Monorepo directory structure, package manager, linter/formatter, pre-commit, `.env.example`, initial README draft.
* **Acceptance Criteria**

  *  [ ] `core/`, `adapters/`, `skills/` directory skeletons exist
  *  [ ] Can run locally with `make dev` or equivalent command
  *  [ ] `.env` is gitignored, only `.env.example` is committed

### #2 Environment Separation (local / prod) & Secret Management

* **Labels:** `infra`, `phase-0`
* **Depends on:** #1
* **Description:** Environment variable loading, config object structure, decide production deployment target Fly.io.
* **Acceptance Criteria**

  *  [ ] Different configs load depending on `ENV=local|prod`
  *  [ ] Telegram bot token, LLM API key, and DB URL are separated
  *  [ ] Successfully deploy to production once (even just hello world)

### #3 DB Schema v0 + Migration Setup (SQLAlchemy + Alembic)

* **Labels:** `core`, `db`, `phase-0`
* **Depends on:** #1, #2
* **Description:** **Postgres** only (SQLite prohibited). **SQLAlchemy 2.0 (async)** ORM + **Alembic** migrations. Only `users` and `messages` tables for now.
* **Acceptance Criteria**

  *  [ ] SQLAlchemy 2.0 async setup (`asyncpg` driver)
  *  [ ] Alembic initialized, `alembic upgrade head` works
  *  [ ] `users(id, telegram_chat_id, created_at)`
  *  [ ] `messages(id, user_id, role, content, tokens_in, tokens_out, created_at)`
  *  [ ] Validate `alembic revision --autogenerate` workflow
* **Acceptance Criteria**

  *  [ ] `users(id, telegram_chat_id, created_at)`
  *  [ ] `messages(id, user_id, role, content, tokens_in, tokens_out, created_at)`
  *  [ ] Schema can be created/rolled back through migration commands

### #4 Define Interface Adapter Abstraction

* **Labels:** `core`, `architecture`, `phase-0`
* **Depends on:** #1
* **Description:** Define the `Adapter` interface — the Core should not know the channel. Something like `receive_message()` and `send_message()`. Later, the RPi voice adapter should implement the same interface.
* **Acceptance Criteria**

  *  [ ] Interface definition exists (abstract class or protocol)
  *  [ ] One dummy/test adapter implemented (for unit testing)

### #5 Implement Telegram Adapter (python-telegram-bot)

* **Labels:** `adapter`, `phase-0`
* **Depends on:** #2, #4
* **Description:** Use **`python-telegram-bot` v21+** (async support). Telegram bot receives message → calls Core → replies. **Use long polling mode locally** (no public URL required). Webhook migration will happen in #11.
* **Acceptance Criteria**

  *  [ ] Messages sent on Telegram are logged in the DB
  *  [ ] Sends the Core response back to Telegram
  *  [ ] Automatically register first-time users
  *  [ ] Structure supports polling/webhook switching through config only
* **Acceptance Criteria**

  *  [ ] Messages sent on Telegram are logged in the DB
  *  [ ] Sends the Core response back to Telegram
  *  [ ] Automatically register first-time users

### #6 LLM Client + Persona Integration

* **Labels:** `core`, `llm`, `phase-0`
* **Depends on:** #3
* **Description:** LLM call wrapper. Inject persona into the system prompt, include recent N-turn conversation context.
* **Acceptance Criteria**

  *  [ ] Configurable model / temperature / max_tokens
  *  [ ] Prompt caching enabled
  *  [ ] Record per-call token usage into the `messages` table

### #7 Persona Document v0

* **Labels:** `persona`, `phase-0`
* **Depends on:** — (parallel possible)
* **Description:** `persona/jansori.md` — tone definition, things it should never do, 5–10 few-shot dialogue examples. Should support hot reload.
* **Acceptance Criteria**

  *  [ ] Document exists + loaded by the LLM client
  *  [ ] At least 5 few-shot examples
  *  [ ] Tone guide explicitly defines the boundary of “lovably annoying”

### #8 Budget Guard (Daily Token Cap)

* **Labels:** `infra`, `safety`, `phase-0`
* **Depends on:** #6
* **Description:** Aggregate daily/weekly token usage. If thresholds are exceeded, block LLM calls and return fallback messages.
* **Acceptance Criteria**

  *  [ ] `DAILY_TOKEN_CAP` environment variable
  *  [ ] Reject calls + log when cap exceeded
  *  [ ] Reset at midnight

### #9 Rate Limiter (per-user, per-minute)

* **Labels:** `infra`, `safety`, `phase-0`
* **Depends on:** #5
* **Description:** Protection against infinite loops/spam. Limit N requests per minute per user.
* **Acceptance Criteria**

  *  [ ] Polite rejection message when exceeded (in Jansori tone)
  *  [ ] In-memory implementation is acceptable (Redis is overengineering)

### #10 Structured Logging + Basic Monitoring

* **Labels:** `infra`, `phase-0`
* **Depends on:** #2
* **Description:** request_id-based logs, error notifications (email or Telegram ping to yourself).
* **Acceptance Criteria**

  *  [ ] Entire flow of a single message processing can be traced with one request_id
  *  [ ] Notify yourself when an unhandled exception occurs

### #11 E2E Smoke Test + Deployment

* **Labels:** `test`, `deploy`, `phase-0`
* **Depends on:** #5, #6, #7, #8
* **Description:** Real conversation on Telegram after production deployment. Using it in daily life for one week = completion condition for Phase 0.
* **Acceptance Criteria**

  *  [ ] Running in production 24/7
  *  [ ] Replies successfully for 7 consecutive days of messages
  *  [ ] Cost report: measure average daily token usage
