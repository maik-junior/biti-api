import os
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI, APIRouter, HTTPException, Depends
from typing import List
from pydantic import BaseModel

# Configuração do banco de dados
sqlite_Name = 'musicas_favoritas.sqlite'
base_dir = os.path.dirname(os.path.realpath(__file__))
data_base_url = f"sqlite:///{os.path.join(base_dir, sqlite_Name)}"
engine = create_engine(data_base_url, echo=True)

# Sessão e Base
Session = sessionmaker(bind=engine)
Base = declarative_base()

# Modelo SQLAlchemy
class Musicas_Favoritas(Base):
    __tablename__ = 'tracks'

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    artist = Column(String, nullable=False)

    def __repr__(self):
        return f"<Musicas_Favoritas(name={self.name}, artist={self.artist}, id={self.id})>"

# Modelo Pydantic
class Lista_Musicas(BaseModel):
    id: str
    name: str
    artist: str

    class Config:
        orm_mode = True

class Sucesso(BaseModel):
    message: str

# Inicialização do FastAPI e APIRouter
app = FastAPI()
router = APIRouter()

# Dependência para obter sessão
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

# Rota POST para salvar músicas
@router.post("/salvar/", response_model=Sucesso)
def save_songs(faixas: List[Lista_Musicas], db: Session = Depends(get_db)):
    try:
        for faixa in faixas:
            # Verifica se o ID já existe
            existente = db.query(Musicas_Favoritas).filter(Musicas_Favoritas.id == faixa.id).first()
            if existente:
                # Pula para a próxima faixa, pois o ID já existe
                continue

            # Cria a nova faixa caso não exista
            nova_faixa = Musicas_Favoritas(id=faixa.id, name=faixa.name, artist=faixa.artist)
            db.add(nova_faixa)

        # Confirma as alterações
        db.commit()
        return Sucesso(message="Lista de músicas salva com sucesso, ignorando duplicatas!")

    except Exception as e:
        db.rollback()  # Desfaz as alterações em caso de erro
        raise HTTPException(status_code=400, detail=f"Erro ao salvar músicas: {str(e)}")


# Configuração do banco de dados
Base.metadata.create_all(bind=engine)

# Incluindo rotas
app.include_router(router)