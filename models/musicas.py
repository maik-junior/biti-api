#==> Importando biblotecas
from sqlalchemy import Column, String
from bd.database import Base

#==> Criando tabela
class Musicas_Favoritas(Base):
    __tablename__ = 'tracks'

    id = Column(String, primary_key=True)  
    name = Column(String, nullable=False)  
    artist = Column(String, nullable=False) 

    def __repr__(self):
        return f"<MusicasFavoritas(name={self.name}, artist={self.artist}, id={self.id})>"
