

class cliente ():

    def __init__(self,
    nome,
    idade,
    id,
    livros_alugados):

        self.__nome = nome
        self.__idade = idade
        self.__id = id
        self.__livros_alugados = livros_alugados

    
    @property
    def nome (self):
        return self.__nome

    @property
    def idade (self):
        return self.__idade

    @property
    def id (self):
        return self.__id

    @property
    def livros_alugados (self):
        return self.__livros_alugados
