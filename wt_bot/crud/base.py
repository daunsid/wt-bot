from asyncio import iscoroutine
from datetime import datetime
from typing import Any, Generic, Type, TypeVar, Awaitable


from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy.future import select


from wt_bot.db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class CRUDBase(Generic[ModelType, CreateSchemaType]):
    def __init__(self, model:Type[ModelType]) -> None:
        """
        CRUD object with default methods to create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A pydantic model(schema) class
        """

        self.model = model

    def _commit_refresh(
            self, db:Session , db_obj:ModelType
    ) -> ModelType | Awaitable[ModelType]:
        db.commit()
        db.refresh(db_obj)

        return db_obj
    
    def _first(self, scalars) -> ModelType | None | Awaitable[ModelType | None]:
        return scalars.first()
    
    def _all(self, scalars) -> list[ModelType] | Awaitable[list[ModelType]]:
        return scalars.all()
    
    def get(
            self, db:Session, id:Any
    ) -> ModelType | Awaitable[ModelType] | None:
        query = select(self.model).filter(self.model.id == id)
        return self._first(db.scalars(query))
    def get_multi(
            
        self, 
        db:Session,
        *,
        skip:int =0,
        limit:int|None = 100,
        asc:bool=False

    )-> list[ModelType]| Awaitable[list[ModelType]]:


        query = (
            select(self.model)
            .order_by(self.model.id.asc() if asc else self.model.id.desc())
            .offset(skip)
        )
        if limit is None:
            return self._all(db.scalars(query))
        return self._all(db.scalars(query.limit(limit)))
    
    def create(
            self, db:Session, *, obj_in:CreateSchemaType
    ) -> ModelType|Awaitable[ModelType]:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        return self._commit_refresh(db=db, db_obj=db_obj)
    
    def update(
        self,
        db:Session,
        *,
        db_obj:ModelType,
        obj_in:UpdateSchemaType|dict[str, Any]|None = None
    ) -> ModelType | Awaitable[ModelType]:
        if obj_in is not None:
            obj_data = jsonable_encoder(db_obj)

            if isinstance(obj_in, dict):
                update_data = obj_in
            else:
                update_data = obj_in.dict(exclude_unset=True)
            for field in obj_data:
                if field in update_data:
                    setattr(db_obj, field, update_data[field])
        if hasattr(self.model, "modified"):
            setattr(db_obj, "modified", datetime.now())
        db.add(db_obj)
        return self._commit_refresh(db=db, db_obj=db_obj)
    


