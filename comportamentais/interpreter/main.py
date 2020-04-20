class Expressao:
    def __init__(self, exp_esquerda, exp_direita):
        self._exp_esquerda = exp_esquerda
        self._exp_direita = exp_direita


class Subtracao(Expressao):
    def avalia(self):
        return self._exp_esquerda.avalia() - self._exp_direita.avalia()


class Soma(Expressao):
    def avalia(self):
        return self._exp_esquerda.avalia() + self._exp_direita.avalia()


class Numero:
    def __init__(self, numero):
        self.__numero = numero

    def avalia(self):
        return self.__numero


if __name__ == "__main__":

    exp_esquerda = Soma(Numero(10), Numero(20))
    exp_direita = Soma(Numero(5), Numero(2))
    exp_conta = Soma(exp_esquerda, exp_direita)
    print("Expressao: (10 + 20) + (5 + 2) =", exp_conta.avalia())

    exp_esquerda = Soma(Numero(20), Numero(80))
    exp_conta = Subtracao(exp_esquerda, Numero(70))
    print("Expressao: (20 + 80) - 70 =", exp_conta.avalia())
