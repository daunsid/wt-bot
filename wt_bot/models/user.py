from sqlalchemy import Integer, String, Column, Boolean
from wt_bot.db.base_class import Base


class User(Base):
    
    id = Column(String, primary_key=True, index=True)
    full_name = Column(String)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)

