class Lampada():
    #atributos
    potencia = 0
    tensao = 220
    cor = "branca"
    estado = False




    #métodos
    def ligar(self): #sempre temm que passar o contexto
        self.estado = True

    def desligar(self): #sempre temm que passar o contexto
        self.estado = False
    
    
    
    def iluminar(self):
        pass    

    def aquecer(self):
        pass


