import pytest

from src.repo.repo_user import RepoUser
from src.schemas.schema_user import UserCreate
from tests.config_test import test_db

class TestRepoUser:
    
    @pytest.fixture
    def repo_user(self, test_db):
        return RepoUser(db=test_db)
    
    @pytest.fixture
    def alan(self):
        return UserCreate(name="Alan")
    
    def test_create_user(self, repo_user, alan):
        result = repo_user.criar(alan)
        assert result.name == "Alan"