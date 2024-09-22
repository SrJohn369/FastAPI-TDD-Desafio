from pydantic import BaseModel, ConfigDict
from typing import Optional


class UserBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str


class UserCreate(UserBase):
    pass


class UserSchema(UserBase):
    id: int
    
    # Se você tiver campos adicionais, adicione-os aqui
    # Por exemplo:
    # email: Optional[str] = None

