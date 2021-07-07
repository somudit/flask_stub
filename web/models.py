from typing import Any
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy_utils import generic_repr

Base: Any = declarative_base()


class DBError(Exception):
    """Class to raise any sort of error while doing db operation"""


def get_session() -> Session:
    """Get a SQLAlchemy session object.
    Args:
      db_url: DB connection string following SQLAlchemy pattern
        `dialect[+driver]://user:password@host/dbname[?key=value..]`.
        http://docs.sqlalchemy.org/en/latest/core/engines.html#sqlalchemy.create_engine
      echo: Print SQL statements to stdout.
    Returns:
      Instance of Session.

    Note: use `sess.close()` after completing all transaction. Be a good citizen.
    """
    from app import engine
    session = sessionmaker(bind=engine)
    return session()


class CreateSession:
    """Context Manager to manage SA session. Connection is automatically closed.

    with CreateSession(db_url) as sess:
        obj = Model(a=a, b=b)
        sess.add(obj)
        sess.commit()

    This wraps `get_session`.

    """

    def __init__(self) -> None:
        self.session = get_session()

    def __enter__(self):
        return self.session

    def __exit__(self, type_, value, traceback):
        self.session.close()


class IdMixin:
    """"Mixin class to insert `id` field in inherited class."""
    id = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True,
                   nullable=False)

    @classmethod
    def get_by_id(cls, id_, sess=None):  # to prevent shadowing of builtin id
        """
        Gets object by for the respective model class
        :param id_: id of the model
        :param sess:
        :return:
        """
        return sess.query(cls).filter_by(id=id_)


class TimestampMixin:
    created = sa.Column(sa.DateTime(timezone=True), default=sa.sql.func.now())
    updated = sa.Column(sa.DateTime(timezone=True), default=sa.sql.func.now(),
                        onupdate=sa.sql.func.now())


