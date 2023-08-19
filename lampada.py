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
    
    #métodos de acessos - acessores
    #get = ler
    #set = alterar
    #decorator property faz com que o metdodo se comporte como atributo
    @property
    def potencia(self):
        return self.__potencia
    @potencia.setter
    def potencia(self,nova_potencia):
        if nova_potencia >0:
            self.__potencia = nova_potencia
        else:
            raise TypeError ("Potencia inválida!")       
    
    @property
    def tensao(self):
        return self.__tensao
    @tensao.setter
    def tensao(self,nova_tensao):
        self.__tensao = nova_tensao
    
    @property
    def cor(self):
        return self.__cor
    @cor.setter
    def cor(self,nova_cor):
        self.__cor = nova_cor

    @property    
    def estado(self):
        return self.__estado
    @estado.setter
    def estado(self,novo_estado):
        self.__estado = novo_estado
    

    def iluminar(self):
        pass    

    def aquecer(self):
        pass


