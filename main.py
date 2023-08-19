from lampada import Lampada

#chamada da Class Lampada()


#sem construtor
#lampada1 = Lampada()
#lampada1.cor = "amarela"
#lampada1.potencia = 20
#lampada1.tensao = 220
#lampada1.ligar()

#com construtor

lampada1 = Lampada("amarela", 500, 240)
lampada1.ligar()



print(lampada1.get_tensao())
print(lampada1.get_cor())
print(lampada1.get_potencia())
print(lampada1.get_estado())

print(f'Minha lampada é {lampada1.get_cor()}, de potencia {lampada1.get_cor()} para ser usada em {lampada1.get_tensao()} volts e está {lampada1.get_estado()}.')