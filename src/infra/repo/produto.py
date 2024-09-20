from sqlalchemy.orm import Session

from src.schemas.produto import ProdutoSchema
from src.infra.models.produto import Produtos as ProdutoModel


class RepoProduto():
    
    def __init__(self, db: Session):
        self.db = db
    
    def criar(self, produto: ProdutoSchema):
        db_produto = ProdutoModel(
            # dados do schema para model  
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