class Lampada():
    #atributos
    __potencia = 0  #dois underlines torna o atributo privado
    __tensao = 220
    __cor = "branca"
    __estado = False


    #construtor
    def __init__(self, cor, potencia, tensao):
        self.__cor = cor
        self.__potencia = potencia
        self.__tensao = tensao

    #métodos
    def ligar(self): #sempre temm que passar o contexto
        self.__estado = True

    def desligar(self): #sempre temm que passar o contexto
        self.__estado = False
    
    def get_tensao(self):
        return self.__tensao
    
    def get_cor(self):
        return self.__cor
    
    def get_potencia(self):
        return self.__potencia
    
    def get_estado(self):
        return self.__estado
    
    def iluminar(self):
        pass    

    def aquecer(self):
        pass


