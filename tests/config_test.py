import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database import Base

# Engine SQLite em memória
engine = create_engine('sqlite:///:memory:')

# Sessão de banco de dados
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope='session')
def setup_database():
    """Cria o schema do banco de dados uma vez por sessão de testes."""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)  # Remove ao final da sessão de testes


@pytest.fixture(scope='function')
def test_db(setup_database):
    """Inicia uma nova transação para cada teste."""
    connection = engine.connect()
    transaction = connection.begin()

    # Faz bind da sessão com a conexão do teste
    TestingSession = sessionmaker(bind=connection)
    db = TestingSession()

    yield db

    # Fecha a sessão e reverte a transação
    db.close()
    transaction.rollback()
    connection.close()
