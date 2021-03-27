from abc import ABCMeta, abstractmethod
from datetime import datetime


class ChatRoomMediator(metaclass=ABCMeta):
    @abstractmethod
    def show_message(self, user, message):
        pass


class ChatRoom(ChatRoomMediator):
    """Mediator"""

    def show_message(self, user, message):
        time = datetime.now()
        sender = user.name
        print(f'{time} [{sender}]: {message}')


class User:
    def __init__(self, name, chat_mediator):
        self.name = name
        self.chat_mediator = chat_mediator

    def send(self, message):
        self.chat_mediator.show_message(self, message)


if __name__ == '__main__':

    mediator = ChatRoom()

    john = User('John', mediator)
    jane = User('Jane', mediator)
    josh = User('Josh', mediator)

    john.send('Hi there!')
    jane.send('Hi!')
    john.send('How are you?')
    jane.send("I'm great, thanks!")
    josh.send('Hi guys!')
