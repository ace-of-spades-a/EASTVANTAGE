from typing import (
    Any,
    List,
    Sequence,
)

from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import Executable


class SessionMixin:
    """Provides instance of database session."""

    def __init__(self, session: Session) -> None:
        self.session = session


class BaseService(SessionMixin):
    """Base class for application services."""


class BaseDataManager(SessionMixin):
    """Base data manager class responsible for operations over database."""

    def get_one(self, select_stmt: Executable) -> Any:
        return self.session.scalar(select_stmt)

    def get_all(self, select_stmt: Executable) -> List[Any]:
        return list(self.session.scalars(select_stmt).all())

    def add_one(self, model: Any) -> int:
        self.session.add(model)
        self.session.flush()
        return model

    def add_all(self, models: Sequence[Any]) -> None:
        self.session.add_all(models)

    def update_one(self, update_stmt: Executable) -> Any:
        return self.session.scalar(update_stmt)

    def delete(self, delete_stmt: Executable):
        self.session.execute(delete_stmt)
        return True
