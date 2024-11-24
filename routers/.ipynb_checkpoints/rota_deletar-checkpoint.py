#==> Bibliotecas
from fastapi import APIRouter, Depends

#==> Componentes
from bd.database import Session, Base
from bd.database import get_db
from models.musicas import Musicas_Favoritas

router = APIRouter()

@router.delete("/deleta_todas", tags=["Tracks"])
def delete_all_tracks(db: Session = Depends(get_db)):
    """
    Rota para deletar todas as músicas do banco de dados.
    """
    # Verificar se há músicas na tabela antes de tentar deletar
    tracks = db.query(Musicas_Favoritas).all()
    if not tracks:
        return {"message": "Não há músicas para deletar."}

    db.query(Musicas_Favoritas).delete()
    db.commit()
    return {"message": "Todas as músicas foram deletadas com sucesso."}