from database import get_db_connection

def calcular_desconto(valor: float, cupom: str) -> float:
    if cupom == "GEEK20":
        return valor * 0.8
    return valor

def processar_pedido(valor: float, cartao: str, gateway):
    if valor <= 0:
        raise ValueError("O valor deve ser maior que zero.")
    sucesso = gateway.cobrar(cartao, valor)
    if not sucesso:
        raise ValueError("Pagamento recusado pelo Gateway.")
    return "Compra aprovada!"

def buscar_produto(nome_produto: str):
    conn = get_db_connection()
    produto = conn.execute(
        "SELECT * FROM produtos WHERE nome = ?",
        (nome_produto.lower(),)
    ).fetchone()
    conn.close()
    return produto


def reduzir_estoque(nome_produto: str):
    conn = get_db_connection()
    conn.execute(
        """
        UPDATE produtos
        SET estoque = estoque - 1
        WHERE nome = ?
        """,
        (nome_produto.lower(),)
    )
    conn.commit()
    conn.close()