import logging
import uuid

from sqlalchemy.orm import Session
from apgar_health import models
from apgar_health.core.config import settings
from apgar_health.core.security import get_password_hash
from apgar_health.db import base
from apgar_health.db.session import SessionLocal




logger =logging.getLogger(__name__)


def create_super_admin(db:Session) -> None:
    user = (
        db.query(models.User)
        .filter(models.User.email == settings.FIRST_SUPERUSER)
        .first()
    )

    if not user:
        user = models.User(
            id=str(uuid.uuid4()),
            email=settings.FIRST_SUPERUSER,
            hashed_password=get_password_hash(
                settings.FIRST_SUPERUSER_PASSWORD
            ),
        )
        db.add(user)
        db.commit()
        db.refresh(user)



def init_db(db:Session) -> None:
    create_super_admin(db)


if __name__ == '__main__':
    db = SessionLocal()
    init_db(db)