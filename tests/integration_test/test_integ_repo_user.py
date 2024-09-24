from tests.config_repo_user_test import *


class TestIntegRepoUser:
    
    def test_get_user_by_id(self, repo_user, create_users):
        user = repo_user.create(create_users[0])
        result = repo_user.get_user_by_id(user.id)
        assert result.id == user.id
        assert result.name == user.name
        
    def test_update_user(self, repo_user, create_users, update_user):
        usr_update = update_user[1]
        repo_user.create(create_users[0])
        result = repo_user.update_user(usr_update)
        assert result.id == usr_update.id
        assert result.name == usr_update.name
        
    def test_update_user_partial(self, repo_user, create_users, update_user):
        usr_update = update_user[0]
        repo_user.create(create_users[0])
        result = repo_user.update_user(usr_update)
        assert result.id == usr_update.id
        assert result.email == usr_update.email
        
        
        
