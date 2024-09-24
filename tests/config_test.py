import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.database.conection import Base


# Engine SQLite baseado em arquivo para persistência durante os testes
TEST_DATABASE_URL = "sqlite:///./test_db.sqlite3"

engine = create_engine(
    TEST_DATABASE_URL, connect_args={"check_same_thread": False}
)
# Sessão de banco de dados
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

### Fixtures para criar o banco de dados
@pytest.fixture(scope='session')
def setup_test_database():
    """Cria o schema do banco de dados uma vez no início dos testes e remove ao final."""
    # Cria todas as tabelas
    Base.metadata.create_all(bind=engine)
    yield
    # Remove todas as tabelas
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope='function')
def session(setup_test_database):
    """Fornece uma sessão de banco de dados para cada teste."""
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()

