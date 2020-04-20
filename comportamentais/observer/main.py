from abc import ABC, abstractmethod


class Observador(ABC):
    @abstractmethod
    def update(self, nota_fiscal):
        pass


class Cliente(Observador):
    def __init__(self, name):
        self.__name = name

    def update(self, pedido):
        print(self.__name, "seu pedido", pedido.numero, "esta", pedido.estado)


class Pedido:
    def __init__(self, numero, itens):
        self.__numero = numero
        self.__itens = itens
        self.__estado = "CRIADO"
        self.__observadores = list()

    @property
    def numero(self):
        return self.__numero

    @property
    def estado(self):
        return self.__estado

    def add_observador(self, observador):
        self.__observadores.append(observador)

    def remove_observador(self, observador):
        self.__observadores.remove(observador)

    def atualiza_estado(self):
        print("Atualizando estado...")
        if self.__estado == "CRIADO":
            self.__estado = "EM ANDAMENTO"
        elif self.__estado == "EM ANDAMENTO":
            self.__estado = "CONCLUIDO"
        self.notifica()

    def notifica(self):
        print("Notificando observadores...")
        for observador in self.__observadores:
            observador.update(self)


if __name__ == "__main__":

    pedido = Pedido(numero=1120, itens=[("Item A", 100)])

    # Adiciona os observadores
    pedido.add_observador(Cliente("Ana"))
    pedido.add_observador(Cliente("Pedro"))
    pedido.add_observador(Cliente("Carla"))

    pedido.notifica()
    pedido.atualiza_estado()
    pedido.atualiza_estado()
