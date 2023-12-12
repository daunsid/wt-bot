from typing import Optional

from pydantic import BaseModel#, EmailStr - emial-validator throwing error after being installed


class UserBase(BaseModel):
    email: str | None = None #EmailStr | None = None
    full_name:str | None = None
    is_active:bool | None= None
    is_superuser:bool = False

# Properties to recieve via API on creation
class UserCreate(UserBase):
    email: str|None#EmailStr | None
    password: str


# properties to recieve via API on update

class LoginUser(BaseModel):
    email:str#EmailStr
    password:str