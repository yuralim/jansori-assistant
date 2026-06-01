import os
import subprocess
from collections.abc import Iterator

import pytest
from sqlalchemy import text
from testcontainers.postgres import PostgresContainer

import core.db.engine as engine_module
from core.db.models import Base


@pytest.fixture(scope="session")
def _postgres_container() -> Iterator[PostgresContainer]:
    with PostgresContainer("postgres:16-alpine", driver="asyncpg") as pg:
        os.environ["DATABASE_URL"] = pg.get_connection_url()
        subprocess.run(["uv", "run", "alembic", "upgrade", "head"], check=True)
        yield pg


@pytest.fixture(autouse=True)
async def _truncate_tables(_postgres_container: PostgresContainer) -> None:
    yield
    engine = engine_module.get_engine()
    table_names = ", ".join(t.name for t in Base.metadata.sorted_tables)
    if not table_names:
        return
    async with engine.begin() as conn:
        await conn.execute(text(f"TRUNCATE TABLE {table_names} RESTART IDENTITY CASCADE"))
