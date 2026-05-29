from unittest.mock import Mock

from services import processar_pedido


def test_processar_pedido_com_sucesso():

    # Mock do gateway
    mock_gateway = Mock()

    # Simula pagamento aprovado
    mock_gateway.cobrar.return_value = True

    resultado = processar_pedido(
        100,
        "123456789",
        mock_gateway
    )

    assert resultado == "Compra aprovada!"

    # Verifica se o método foi chamado
    mock_gateway.cobrar.assert_called_once_with(
        "123456789",
        100
    )


def test_processar_pedido_pagamento_recusado():

    mock_gateway = Mock()

    # Simula falha
    mock_gateway.cobrar.return_value = False

    try:

        processar_pedido(
            100,
            "123456789",
            mock_gateway
        )

    except ValueError as e:

        assert str(e) == "Pagamento recusado pelo Gateway."

    # Verifica chamada
    mock_gateway.cobrar.assert_called_once()


def test_processar_pedido_valor_invalido():

    mock_gateway = Mock()

    try:

        processar_pedido(
            0,
            "123456789",
            mock_gateway
        )

    except ValueError as e:

        assert str(e) == "O valor deve ser maior que zero."

    # Não deve chamar gateway
    mock_gateway.cobrar.assert_not_called()