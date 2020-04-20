from abc import ABCMeta, abstractmethod


class EstadoOrcamento(metaclass=ABCMeta):
    @abstractmethod
    def aplica_desconto(self, orcamento):
        pass

    @abstractmethod
    def aprova(self, orcamento):
        pass

    @abstractmethod
    def reprova(self, orcamento):
        pass

    @abstractmethod
    def finaliza(self, orcamento):
        pass


class EmAprovacao(EstadoOrcamento):
    def aplica_desconto(self, orcamento):
        orcamento.adiciona_desconto(orcamento.total * 0.02)

    def aprova(self, orcamento):
        orcamento.estado = Aprovado()

    def reprova(self, orcamento):
        orcamento.estado = Reprovado()

    def finaliza(self, orcamento):
        raise Exception("Orcamento em aprovacao nao pode ser finalizado")


class Aprovado(EstadoOrcamento):
    def aplica_desconto(self, orcamento):
        orcamento.adiciona_desconto(orcamento.total * 0.05)

    def aprova(self, orcamento):
        raise Exception("Orcamento aprovado nao pode ser aprovado novamente")

    def reprova(self, orcamento):
        raise Exception("Orcamento aprovado nao pode ser reprovado")

    def finaliza(self, orcamento):
        orcamento.estado = Finalizado()


class Reprovado(EstadoOrcamento):
    def aplica_desconto(self, orcamento):
        raise Exception("Orcamento reprovado nao recebe desconto extra")

    def aprova(self, orcamento):
        raise Exception("Orcamento reprovado nao pode ser aprovado")

    def reprova(self, orcamento):
        raise Exception("Orcamento reprovado nao pode ser reprovado novamente")

    def finaliza(self, orcamento):
        orcamento.estado = Finalizado()


class Finalizado(EstadoOrcamento):
    def aplica_desconto(self, orcamento):
        raise Exception("Orcamento finalizado nao recebe desconto extra")

    def aprova(self, orcamento):
        raise Exception("Orcamento finalizado nao pode ser aprovado")

    def reprova(self, orcamento):
        raise Exception("Orcamento finalizado nao pode ser reprovado")

    def finaliza(self, orcamento):
        raise Exception(
            "Orcamento finalizado nao pode ser finalizado novamente"
        )


class Orcamento:
    def __init__(self):
        self.__itens = list()
        self.estado = EmAprovacao()
        self.__desconto = 0

    def aprova(self):
        self.estado.aprova(self)

    def reprova(self):
        self.estado.reprova(self)

    def finaliza(self):
        self.estado.finaliza(self)

    def adiciona_desconto(self, desconto):
        self.__desconto += desconto

    def aplica_desconto(self):
        self.estado.aplica_desconto(self)

    @property
    def total(self):
        return sum([x for _, x in self.__itens]) - self.__desconto

    def add_item(self, item, valor):
        self.__itens.append((item, valor))

    def show(self):
        print("Estado:", self.estado.__class__.__name__)
        print("Desconto:", self.__desconto)
        print("Total:", self.total)


if __name__ == "__main__":

    orcamento = Orcamento()
    orcamento.add_item("item 0", 100.0)
    orcamento.add_item("item 1", 50.0)
    orcamento.add_item("item 2", 400.0)
    orcamento.show()

    orcamento.aprova()
    orcamento.aplica_desconto()
    orcamento.show()

    orcamento.finaliza()
    orcamento.show()
