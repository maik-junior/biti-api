#==> Importando biblotecas 
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#==> Configuracao do banco de dados
sqlite_Name = 'musicas_favoritas.sqlite'
base_dir = os.path.dirname(os.path.realpath(__file__))
data_base_url = f"sqlite:///{os.path.join(base_dir, sqlite_Name)}"

#==> Criando a conexao com o banco de dados
engine = create_engine(data_base_url, echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

#==> Funcao para obter a sessao do banco de dados
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
