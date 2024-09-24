from tests.config_test import *

from src.repo.repo_user import RepoUser

from src.schemas.schema_user import UserSchema, UserCreate

### Fixtures para usuários ###
@pytest.fixture
def repo_user(session):
    return RepoUser(db=session)

@pytest.fixture
def create_users():
    list_users = [UserCreate(name="Alan"), UserCreate(name="Clara"),
                    UserCreate(name="João"), UserCreate(name="Maria")]
    return list_users

@pytest.fixture
def update_user():
    list_update = [UserSchema(id=1, email="jose.julio@gmail.com", name="Alan"), UserSchema(id=2, name="Júla")]
    return list_update

@pytest.fixture
def schema_users():
    list_schema = [UserSchema(id=1, name="Alan"), UserSchema(id=2, name="Clara"),
                    UserSchema(id=3, name="João"), UserSchema(id=4, name="Maria")]
    return list_schema

####### mocks #######