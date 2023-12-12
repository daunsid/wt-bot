from datetime import datetime
from fastapi import Depends, HTTPException, status
from typing import Generator

from fastapi.security import HTTPBearer
from pydantic import ValidationError
from sqlalchemy.orm import Session
import jwt

from wt_bot import crud, models, schemas, utils
from wt_bot.core.config import settings
from wt_bot.db.session import SessionLocal

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

async def get_current_user(
        authorization:str = Depends(HTTPBearer()),
        db:Session = Depends(get_db)
) -> models.User:
    try:
        token = authorization.credentials
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = schemas.TokenPayload(**payload)

    except jwt.ExpiredSignatureError as e :
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=str(e)
        )
    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Token prefix missing",
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Authentication Failed",
        )
    
    user = await crud.user.get(db, id=token_data.sub)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return user
