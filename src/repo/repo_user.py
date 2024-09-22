from sqlalchemy.orm import Session

from src.schemas.schema_user import UserSchema
from src.models.model_user import UserModel


class RepoUser():
    
    def __init__(self, db: Session):
        self.db = db
    
    def criar(self, user: UserSchema):
        db_produto = UserModel(
            name=user.name
        )
        
        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        
        return db_produto
    
    def obter(self):
        pass
    
    def listar(self):
        pass
    
    def alterar(self):
        pass
    
    def deletar(self):
        pass