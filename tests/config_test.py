import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database.conection import Base

# Engine SQLite em memória
engine = create_engine('sqlite:///:memory:')

# Sessão de banco de dados
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope='function')
def test_db():
    """Configura o banco de dados e fornece uma sessão para cada teste."""
    # Cria o schema do banco de dados
    Base.metadata.create_all(bind=engine)
    
    # Cria uma nova conexão e transação para o teste
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    
    yield session
    
    # Limpa após o teste
    session.close()
    transaction.rollback()
    connection.close()
    
    # Remove o schema do banco de dados
    Base.metadata.drop_all(bind=engine)
