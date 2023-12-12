from typing import Any, Dict, Union, Awaitable


from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy.future import select


from wt_bot.core.security import get_password_hash, verify_password
from wt_bot.crud.base import CRUDBase
from wt_bot.models.user import User
from wt_bot.schemas.user import UserCreate


class CRUDUser(CRUDBase[User, UserCreate]):
    def get_by_email(
        self, db:Session, *, email:str
    ) -> User |None | Awaitable[User |None]:
        query = select(User).filter(User.email==email)
        return self._first(db.scalars(query))
    

    async def create(self, db: Session, *, obj_in: UserCreate) -> User:
        obj_in_data = jsonable_encoder(obj_in)
        obj_in_data["hashed_password"] = get_password_hash(obj_in.password)
        del obj_in_data["password"]
        obj_in_data = {k: v for k, v in obj_in_data.items() if v is not None}
        return await super().create(db, obj_in=obj_in_data)
    
    
    def authenticate(
        self, db: Session , *, email: str, password: str
    ) -> User | None | Awaitable[User | None]:
        # if isinstance(db, AsyncSession):
        #     return self.authenticate_async(db=db, email=email, password=password)
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user


user = CRUDUser(User)