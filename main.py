from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from typing import Optional

from database import init_db, get_db_connection
from gateway import GatewayPagamento, get_gateway
from services import (
    calcular_desconto,
    processar_pedido,
    buscar_produto,
    reduzir_estoque
)

app = FastAPI()


class CompraRequest(BaseModel):
    produto: str
    cartao: str
    cupom: Optional[str] = ""


@app.on_event("startup")
def startup_event():
    init_db()


@app.get("/api/produtos")
def listar_produtos():

    conn = get_db_connection()

    produtos = conn.execute(
        "SELECT * FROM produtos"
    ).fetchall()

    conn.close()

    return [dict(p) for p in produtos]


@app.post("/api/comprar")
def comprar(
    req: CompraRequest,
    gateway: GatewayPagamento = Depends(get_gateway)
):

    produto = buscar_produto(req.produto)

    if not produto:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    if produto["estoque"] <= 0:
        raise HTTPException(
            status_code=400,
            detail="Sem estoque"
        )

    valor_final = calcular_desconto(
        produto["preco"],
        req.cupom
    )

    try:

        mensagem = processar_pedido(
            valor_final,
            req.cartao,
            gateway
        )

        reduzir_estoque(req.produto)

        return {
            "status": "sucesso",
            "mensagem": mensagem,
            "valor_pago": valor_final
        }

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@app.get("/", response_class=HTMLResponse)
def frontend():

    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()