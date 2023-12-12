from datetime import datetime
from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import DateTime


@as_declarative()
class Base:
    id: Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    created = Column(DateTime(timezone=True), default=datetime.utcnow, index=True)
    modified = Column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        index=True,
        onupdate=datetime.utcnow,
    )

    def __str__(self):
        return f"{self.__tablename__}:{self.id}"

    def __repr__(self):
        try:
            return f"{self.__class__.__name__}({self.__tablename__}:{self.id})"
        except:
            return f"Faulty-{self.__class__.__name__}"