from pydantic import BaseModel, ConfigDict
from typing import Optional


class UserBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class UserCreate(UserBase):
    name: str


class UserUpdate(UserBase):
    email: Optional[str] = None


class UserSchema(UserBase):
    id: int
    email: Optional[str] = None
