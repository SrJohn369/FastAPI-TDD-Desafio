from sqlalchemy.orm import Session

from src.schemas.schema_user import UserSchema
from src.models.model_user import UserModel


class RepoUser():
    
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, user: UserSchema):
        db_produto = UserModel(
            name=user.name
        )
        
        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        
        return db_produto
    
    def get_user_by_id(self, user_id: int):
        try:
            cosult = self.db.query(UserModel).filter(UserModel.id == user_id).first()
            if cosult is None:
                raise Exception("User not found")
            return cosult
        except Exception as e:
            raise e
    
    def list_users(self):
        try:
            return self.db.query(UserModel).all()
        except Exception as e:
            raise e
    
    def update_user(self, user: UserSchema):
        try:
            user_up = self.db.query(UserModel).filter(UserModel.id == user.id).first()
            [setattr(user_up, key, value) for key, value in user.model_dump().items()]
            self.db.commit()
            return user_up
        except Exception as e:
            raise e
    
    def delete(self, user: UserSchema):
        try:
            self.db.query(UserModel).filter(UserModel.id == user.id).delete()
            self.db.commit()
            return user
        except Exception as e:
            raise e