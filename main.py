from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

vendas = {
    1: {"item": "lata", "preco_unitario": 4, "quantidade": 5},
    2: {"item": "garrafa 2L", "preco_unitario": 15, "quantidade": 5},
    3: {"item": "garrafa 750ml", "preco_unitario": 10, "quantidade": 5},
    4: {"item": "lata mini", "preco_unitario": 2, "quantidade": 5},
}

# Definindo o modelo de dados para o corpo da requisição
class Venda(BaseModel):
    item: str
    preco_unitario: float
    quantidade: int

# Método GET para a home
@app.get("/")
def home():
    return {"Vendas": len(vendas)}

# Método GET para pegar uma venda pelo ID
@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda: int):
    if id_venda in vendas:
        return vendas[id_venda]
    raise HTTPException(status_code=404, detail="Venda não encontrada")

# Método POST para adicionar uma nova venda
@app.post("/vendas/")
def adicionar_venda(venda: Venda):
    novo_id = max(vendas.keys()) + 1  # Gera um novo ID para a venda
    vendas[novo_id] = venda.dict()  # Adiciona a nova venda ao dicionário
    return {"id": novo_id, "mensagem": "Venda adicionada com sucesso!"}
