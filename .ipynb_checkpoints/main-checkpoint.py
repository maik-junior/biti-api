#==> Importando biblotecas
from fastapi import FastAPI

#==> Componentes
from bd.database import Base, engine
from models.validate import Lista_Musicas, Sucesso
from routers.rota import router as salva_favoritas
from routers.rota_leitura import router as lista_todas
from routers.rota_deletar import router as deletar_todas

#==> Criando tabelas no banco de dados
Base.metadata.create_all(bind=engine)

#==> Instanciando 
app = FastAPI()

#==> Configuracao do banco de dados
Base.metadata.create_all(bind=engine)

#==> Incluindo rotas
app.include_router(lista_todas, tags=["Tracks"])
app.include_router(salva_favoritas, tags=["Tracks"])
app.include_router(deletar_todas, tags=["Tracks"])


# http POST http://127.0.0.1:4000/salvar/ < ./files/data.json
# http --pretty=all GET http://127.0.0.1:4000/listar/
# http DELETE http://127.0.0.1:4000/deleta_todas/