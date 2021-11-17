

class cliente ():

    def __init__(self,
                 nome,
                 nick,
                 tipo):

        self.__nome = nome
        self.__nick = nick
        self.__tipo = tipo

    @property
    def nome(self):
        return self.__nome

    @property
    def nick(self):
        return self.__nick

    @property
    def tipo(self):
        return self.__tipo
