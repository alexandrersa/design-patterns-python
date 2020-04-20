class Impressao:
    def visita_soma(self, soma):
        print("(", end=" ")
        soma.esquerda.aceita(self)
        print("+", end=" ")
        soma.direita.aceita(self)
        print(")", end=" ")

    def visita_subtracao(self, subtracao):
        print("(", end=" ")
        subtracao.esquerda.aceita(self)
        print("-", end=" ")
        subtracao.direita.aceita(self)
        print(")", end=" ")

    def visita_numero(self, numero):
        print(numero.avalia(), end=" ")


class Subtracao:
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def avalia(self):
        return self.esquerda.avalia() - self.direita.avalia()

    def aceita(self, visitor):
        visitor.visita_subtracao(self)


class Soma:
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def avalia(self):
        return self.esquerda.avalia() + self.direita.avalia()

    def aceita(self, visitor):
        visitor.visita_soma(self)


class Numero:
    def __init__(self, numero):
        self.__numero = numero

    def avalia(self):
        return self.__numero

    def aceita(self, visitor):
        visitor.visita_numero(self)


if __name__ == "__main__":

    esquerda = Soma(Numero(10), Numero(20))
    direita = Soma(Numero(5), Numero(2))
    expressao_conta = Soma(esquerda, direita)

    impressao = Impressao()
    expressao_conta.aceita(impressao)

    print()

    esquerda = Subtracao(Numero(100), Numero(20))
    direita = Soma(Numero(5), Numero(5))
    expressao_conta = Soma(esquerda, direita)
    expressao_conta.aceita(impressao)
