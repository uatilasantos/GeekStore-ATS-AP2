Feature: Compra de produto

  Scenario: Compra com sucesso

    Given que existe um produto "teclado"

    When eu realizar uma compra do produto "teclado"

    Then a compra deve ser aprovada