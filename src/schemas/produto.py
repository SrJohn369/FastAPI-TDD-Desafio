from pydantic import BaseModel
from typing import Optional


class ProdutoBase(BaseModel):
    # base fields
    pass


class PordutoCreate(ProdutoBase):
    # create fields
    pass


class Produto(ProdutoBase):
    # produto filds
    
    class Config:
        orm_mode = True