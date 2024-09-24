from tests.config_repo_user_test import *

class TestRepoUser:
    
    def test_create_user(self, repo_user, create_users):
        result = repo_user.create(create_users[0])
        assert result.id is not None
        assert result.name == "Alan"
        
    def test_get_erro_user_not_found(self, repo_user):
        with pytest.raises(Exception):
            repo_user.get_user_by_id(1)
    
    