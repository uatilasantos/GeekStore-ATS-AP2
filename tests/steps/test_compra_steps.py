from pytest_bdd import scenarios, given, when, then
from fastapi.testclient import TestClient

from main import app
from database import get_db_connection

client = TestClient(app)

scenarios("../features/compra_sucesso.feature")


@given('que existe um produto "teclado"')
def produto_existe():

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


@when('eu realizar uma compra do produto "teclado"')
def realizar_compra():

    global response

    response = client.post(
        "/api/comprar",
        json={
            "produto": "teclado",
            "cartao": "123456789",
            "cupom": "GEEK20"
        }
    )


@then("a compra deve ser aprovada")
def validar_compra():

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "sucesso"

    assert data["mensagem"] == "Compra aprovada!"