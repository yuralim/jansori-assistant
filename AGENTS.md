# AGENTS.md

Repository guidance for coding agents working on `jansori-assistant`.

## Read This First

- Before making code changes, read the relevant files in `docs/` for product and architecture context.
- If the task is broad or touches product direction, skim all current docs:
  - `docs/overview.md`
  - `docs/architecture.md`
  - `docs/roadmap.md`
- Treat `README.md` as the quickstart and `docs/` as the source of longer-term intent.
- If implementation and docs disagree, mention the mismatch before changing behavior.

## Development Commands

- Install or sync dependencies: `uv sync`
- Run the app locally: `uv run python main.py`
- Run tests: `uv run pytest`
- Run a focused test: `uv run pytest tests/path/to/test_file.py -k test_name`

Run the smallest useful test while iterating, then run `uv run pytest` before considering a code change complete.

## Python Rules

- Target Python 3.13 or newer.
- Prefer simple functions and small modules over speculative abstractions.
- Use type hints for new public functions and for code where types clarify behavior.
- Keep async Telegram handlers async; test them with `pytest.mark.asyncio` and `AsyncMock` when awaiting calls.
- Use the standard `logging` module for runtime diagnostics. Do not use `print` for application logs.
- Read configuration from environment variables. Do not hard-code secrets, tokens, user data, or machine-specific paths.
- Raise clear exceptions for missing required configuration at startup.
- Keep imports tidy and remove only unused imports introduced by your change.

## Testing Rules

- Add or update tests for behavior changes.
- For bug fixes, prefer a failing test that reproduces the issue before changing code.
- Keep tests focused on externally visible behavior rather than implementation details.
- Mock Telegram network/API objects; unit tests should not call real Telegram services.
- Do not require real secrets or `.env` files for tests.

## Dependency Rules

- Ask before adding new production dependencies.
- Prefer the Python standard library unless a dependency already exists or clearly pays for itself.
- Update `pyproject.toml` and `uv.lock` together when dependency changes are required.
- Do not hand-edit generated lockfile content except as part of the normal package-management workflow.

## Docs Rules

- Update `README.md` when setup, run, or test commands change.
- Update files in `docs/` when product behavior, architecture, phases, or design principles change.
- Keep docs grounded in implemented behavior versus future roadmap. Label future plans clearly.

## Change Discipline

- State assumptions when requirements are ambiguous.
- Ask before making destructive changes, large refactors, or broad architectural moves.
- Touch only files needed for the task.
- Match the existing style of nearby code.
- Do not clean up unrelated code, formatting, or dead files unless asked.
- After changes, summarize what was verified and any remaining risk.
