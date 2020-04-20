from abc import ABC, abstractmethod


class Orcamento:
    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor


class Desconto(ABC):
    @abstractmethod
    def calcula(self, orcamento):
        pass


class ISS(Desconto):
    def calcula(self, orcamento):
        return orcamento.valor * 0.1


class ICMS(Desconto):
    def calcula(self, orcamento):
        return orcamento.valor * 0.06


class CalculadoraImpostos:
    def __init__(self):
        self.imposto = None

    def calcula(self, orcamento):
        print("Imposto Calculado:", self.imposto.calcula(orcamento))


if __name__ == "__main__":

    orcamento = Orcamento(500)
    calculadora = CalculadoraImpostos()
    calculadora.imposto = ISS()
    calculadora.calcula(orcamento)
    calculadora.imposto = ICMS()
    calculadora.calcula(orcamento)
