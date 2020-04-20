
class DescontoCincoItens:
    """Aplica desconto para orcamentos com mais de 5 itens."""

    def __init__(self, proximo):
        self.__proximo = proximo

    def calcula(self, orcamento):
        if orcamento.total_itens > 5:
            return orcamento.valor * 0.1
        return self.__proximo.calcula(orcamento)


class DescontoMaisDeQuinhentosReais:
    """Aplica desconto para orcamentos com mais de quinhentos reais."""

    def __init__(self, proximo):
        self.__proximo = proximo

    def calcula(self, orcamento):
        if orcamento.valor > 500.0:
            return orcamento.valor * 0.07
        return self.__proximo.calcula(orcamento)


class SemDesconto:
    """Sem desconto, fim da cadeia."""

    def calcula(self, orcamento):
        return 0


def calcula_desconto(orcamento):
    return DescontoCincoItens(
        DescontoMaisDeQuinhentosReais(
            SemDesconto()
        )
    ).calcula(orcamento)


def mostra_orcamento(orcamento):
    print("Quantidade Itens:", orcamento.total_itens)
    print("Valor Total:", orcamento.valor)
    print("Desconto calculado:", calcula_desconto(orcamento))


if __name__ == "__main__":

    from orcamento import Orcamento, Item

    print("Sem desconto:")
    orcamento = Orcamento()
    orcamento.adiciona_item(Item("item 1", 100.0))
    mostra_orcamento(orcamento)

    print("\nDesconto de 5 itens:")
    orcamento = Orcamento()
    for _ in range(10):
        orcamento.adiciona_item(Item("item x", 100.0))
    mostra_orcamento(orcamento)

    print("\nDesconto mais de 500 reais:")
    orcamento = Orcamento()
    orcamento.adiciona_item(Item("item 1", 1000.0))
    mostra_orcamento(orcamento)
