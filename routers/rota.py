#==> Bibliotecas
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List
# from sqlalchemy.orm import Session

#==> Componentes
from bd.database import get_db
from bd.database import Session, Base
from models.musicas import Musicas_Favoritas
from models. validate import Lista_Musicas, Sucesso

#==> Instancia
router = APIRouter()

#==> Rota para salvar musicas
@router.post("/salvar/", response_model=Sucesso)
def save_songs(faixas: List[Lista_Musicas], db: Session = Depends(get_db)):
    try:
        for faixa in faixas:
            #==> Verifica se o id ja existe
            existente = db.query(Musicas_Favoritas).filter(Musicas_Favoritas.id == faixa.id).first()
            if existente:
                continue  #==> Pula faixas duplicadas

            #==> Adiciona a nova faixa
            nova_faixa = Musicas_Favoritas(id=faixa.id, name=faixa.name, artist=faixa.artist)
            db.add(nova_faixa)

        db.commit()  #==> Salva alteracoes
        return Sucesso(message="Lista de musicas salva com sucesso!")

    except Exception as e:
        db.rollback()  #==> Desfaz alteracoes em caso de erro
        raise HTTPException(status_code=400, detail=f"Erro ao salvar músicas: {str(e)}")
