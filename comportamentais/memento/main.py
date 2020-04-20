from datetime import date


class Contrato:
    def __init__(self, data, cliente, tipo):
        self.data = data
        self.cliente = cliente
        self.tipo = tipo

    def avanca(self):
        tipos = {
            "NOVO": "EM ANDAMENTO",
            "EM ANDAMENTO": "ACERTADO",
            "ACERTADO": "CONCLUIDO"
        }
        self.tipo = tipos[self.tipo]

    def salva(self):
        # Não podemos passar o self para o Estado pois se o contrato fosse
        # alterado o estado anterior dele tambem seria alterado
        return Estado(Contrato(self.data, self.cliente, self.tipo))

    def restaura(self, estado):
        self.cliente = estado.contrato.cliente
        self.data = estado.contrato.data
        self.tipo = estado.contrato.tipo

    def show(self):
        print("Cliente:", self.cliente)
        print("Data:", self.data)
        print("Tipo:", self.tipo)


class Estado:
    def __init__(self, contrato):
        self.__contrato = contrato

    @property
    def contrato(self):
        return self.__contrato


class Historico:
    def __init__(self):
        self.__estados = list()

    def obtem_estado(self, indice):
        return self.__estados[indice]

    def adiciona_estado(self, estado):
        self.__estados.append(estado)


if __name__ == "__main__":

    contrato = Contrato(data=date.today(), cliente="Kelvin", tipo="NOVO")
    contrato.avanca()

    historico = Historico()
    historico.adiciona_estado(contrato.salva())

    contrato.avanca()
    contrato.cliente = "Joao da Silva"

    historico.adiciona_estado(contrato.salva())
    contrato.avanca()
    historico.adiciona_estado(contrato.salva())

    for i in range(3):
        contrato.restaura(historico.obtem_estado(i))
        contrato.show()
