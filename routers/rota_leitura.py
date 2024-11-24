#==> Bibliotecas
from fastapi import APIRouter, HTTPException, Depends
from typing import List
# from sqlalchemy.orm import Session

#==> Componentes
from bd.database import Session, Base
from bd.database import get_db
from models.musicas import Musicas_Favoritas
from models.validate import Lista_Musicas, Sucesso

#==> Instancia
router = APIRouter()

#==> Para ler favoritas
@router.get("/listar/", response_model=List[Lista_Musicas])
def recupera_todas(db: Session = Depends(get_db)):
    try:
        #==> Consulta todas as musicas no banco de dados
        musicas = db.query(Musicas_Favoritas).all()
        return musicas
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao listar musicas: {str(e)}")
