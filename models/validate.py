#==> Importando biblotecas
from pydantic import BaseModel
from typing import List

#==> Modelo para validacao de entrada
class Lista_Musicas(BaseModel):
    id: str
    name: str
    artist: str

    class Config:
        orm_mode = True

#==> Modelo de resposta staus '200'
class Sucesso(BaseModel):
    message: str
