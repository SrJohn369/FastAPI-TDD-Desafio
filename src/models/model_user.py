from sqlalchemy import Column, Integer, String

from src.database.conection import Base 


# your code here
class UserModel(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    