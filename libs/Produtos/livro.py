
class Livro():

    def __init__(self,
    id,
    nome,
    genero,
    quantidade_loco,
    quantidade_cliente,
    autor,
    ano,
    edicao,
    paginas):

        self.__id = id
        self.__nome = nome
        self.__genero = genero
        self.__quantidade_loco = quantidade_loco
        self.__quantidade_cliente = quantidade_cliente
        self.__autor = autor
        self.__ano = ano
        self.__edicao = edicao
        self.__paginas = paginas


    @property
    def id (self):
        return self.__id

    @property
    def nome (self):
        return self.__nome

    @property
    def genero (self):
        return self.__genero

    @property
    def quantidade_loco (self):
        return self.__quantidade_loco

    @property
    def quantidade_cliente (self):
        return self.__quantidade_cliente

    @property
    def autor (self):
        return self.__autor

    @property
    def ano (self):
        return self.__ano

    @property
    def edicao (self):
        return self.__edicao

    @property
    def paginas (self):
        return self.__paginas

