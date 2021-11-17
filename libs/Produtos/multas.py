
class Multa():

    def __init__(self,
    id,
    cliente,
    valor,
    pago):

        self.__id = id
        self.__cliente = cliente
        self.__valor = valor
        self.__pago = pago


    @property
    def id (self):
        return self.__id
        
    @property
    def cliente (self):
        return self.__cliente
        
    @property
    def valor (self):
        return self.__valor
        
    @property
    def pago (self):
        return self.__pago
        