from fastapi.testclient import TestClient

from main import app
from database import get_db_connection

client = TestClient(app)


def test_listar_produtos():

    response = client.get("/api/produtos")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

    assert len(data) > 0

    assert "nome" in data[0]
    assert "preco" in data[0]
    assert "estoque" in data[0]


def test_compra_com_sucesso():

    conn = get_db_connection()

    conn.execute(
        """
        UPDATE produtos
        SET estoque = 10
        WHERE nome = 'teclado'
        """
    )

    conn.commit()
    conn.close()

    response = client.post(
        "/api/comprar",
        json={
            "produto": "teclado",
            "cartao": "123456789",
            "cupom": "GEEK20"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "sucesso"
    assert data["mensagem"] == "Compra aprovada!"
    assert data["valor_pago"] == 160.0


def test_produto_inexistente():

    response = client.post(
        "/api/comprar",
        json={
            "produto": "cadeira",
            "cartao": "123456789"
        }
    )

    assert response.status_code == 404

    data = response.json()

    assert data["detail"] == "Produto não encontrado"


def test_produto_sem_estoque():

    conn = get_db_connection()

    conn.execute(
        """
        UPDATE produtos
        SET estoque = 0
        WHERE nome = 'mouse'
        """
    )

    conn.commit()
    conn.close()

    response = client.post(
        "/api/comprar",
        json={
            "produto": "mouse",
            "cartao": "123456789"
        }
    )

    assert response.status_code == 400

    data = response.json()

    assert data["detail"] == "Sem estoque"