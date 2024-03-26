from typing import Iterator

from sqlalchemy import create_engine
from sqlalchemy.orm import (
    Session,
    sessionmaker,
)

from backend.config import settings


# create session factory to generate new database sessions
print(
    f"--------------------------- {settings.DATABASE_URL} ---------------------------"
)
engin = create_engine(settings.DATABASE_URL)
SessionFactory = sessionmaker(
    bind=engin,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
)


def create_session() -> Iterator[Session]:
    """Create new database session.

    Yields:
        Database session.
    """

    session = SessionFactory()

    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
