from services import calcular_desconto


def test_calcular_desconto_com_cupom():

    resultado = calcular_desconto(100, "GEEK20")

    assert resultado == 80


def test_calcular_desconto_sem_cupom():

    resultado = calcular_desconto(100, "")

    assert resultado == 100