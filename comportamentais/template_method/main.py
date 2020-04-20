from abc import ABC, abstractmethod


class Orcamento:
    def __init__(self):
        self.__itens = list()

    @property
    def total(self):
        return sum([valor for _, valor in self.__itens])

    @property
    def total_itens(self):
        return len(self.__itens)

    def adiciona_item(self, item, valor):
        self.__itens.append((item, valor))


class TemplateImpostosCondicional(ABC):
    def calcula(self, orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento)
        return self.minima_taxacao(orcamento)

    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def minima_taxacao(self, orcamento):
        pass


class ICPP(TemplateImpostosCondicional):
    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.total > 500

    def maxima_taxacao(self, orcamento):
        return orcamento.total * 0.07

    def minima_taxacao(self, orcamento):
        return orcamento.total * 0.05


class IKCV(TemplateImpostosCondicional):
    def _item_maior_que_cem_reais(self, orcamento):
        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True
        return False

    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.total > 500 and self._item_maior_que_cem_reais(
            orcamento
        )

    def maxima_taxacao(self, orcamento):
        return orcamento.total * 0.1

    def minima_taxacao(self, orcamento):
        return orcamento.total * 0.06


class CalculadoraImpostos:
    def realiza_calculo(self, orcamento, imposto):
        print(imposto.__class__.__name__, ":", imposto.calcula(orcamento))


if __name__ == "__main__":

    orcamento = Orcamento()
    orcamento.adiciona_item("item 0", 50.0)
    orcamento.adiciona_item("item 1", 200.0)
    orcamento.adiciona_item("item 2", 250.0)

    calculadora = CalculadoraImpostos()
    calculadora.realiza_calculo(orcamento, ICPP())
    calculadora.realiza_calculo(orcamento, IKCV())
