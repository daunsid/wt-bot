from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, drop_database
import uuid

from apgar_health.db.base import Base
from apgar_health.models.user import User
from apgar_health.core.config import settings

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_SERVER}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_testing_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def setup_test_db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()

def test_create_user():
    user = User(
        id = str(uuid.uuid4()),
        full_name="test user",
        email="test6@mail.com",
        hashed_password="password",
    )
    db = next(setup_test_db())
    db.add(user)
    db.commit()

    retrieved_user = db.query(User).filter(User.id == user.id).first()

    assert retrieved_user is not None
    assert retrieved_user.full_name == "test user"
    assert retrieved_user.email == "test6@mail.com"
    

    db.delete(user)
    db.commit()
