
class cliente_interno():

    def __init__(self,
    nome,
    idade,
    id):

        self.__nome = nome
        self.__idade = idade
        self.__id = id

    
    @property
    def nome (self):
        return self.__nome

    @property
    def idade (self):
        return self.__idade

    @property
    def id (self):
        return self.__id