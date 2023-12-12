from datetime import datetime
from typing import Any

from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException



from sqlalchemy.orm import Session
import jwt



from wt_bot import models, schemas
from wt_bot.api import deps
from wt_bot.core import security
from wt_bot.core.config import settings
from wt_bot.core.security import get_password_hash



router = APIRouter()

namespace = "user"

@router.post("/login")
async def login(

)->Any:
    """
    get access and refresh token.
    """
    


@router.post("/")
async def create_user(
    *,
    db:Session=Depends(deps.get_db),
    #user_in:schemas.UserCreate,
    #current_user:models.User = Depends
):
    pass