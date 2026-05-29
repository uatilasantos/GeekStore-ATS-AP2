class GatewayPagamento:

    def cobrar(self, cartao: str, valor: float):
        return True


def get_gateway():
    return GatewayPagamento()