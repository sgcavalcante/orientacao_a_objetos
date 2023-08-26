from lampada import Lampada
from conta import ContaPoupanca, ContaCorrente

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

#métodos para pegar atributos e alterar atributos
lampada1.potencia = 30
print(lampada1.potencia)

lampada1.tensao=13800
print(lampada1.tensao)

lampada1.cor="preta"
print(lampada1.cor)

lampada1.estado=True
print(lampada1.estado)

#print(f'Minha lampada é {lampada1.cor}, de potencia {lampada1.cor} para ser usada em {lampada1.tensao} volts e está {lampada1.estado}.')

print(f'{25*"-"}Deposito{25*"-"}')

conta_pedro = ContaCorrente(123,147,"Pedro",0.0)
conta_jose = ContaCorrente(123,147,"José",1000)
conta_daniele = ContaPoupanca(963,854,"Daniele")
conta_manoel = ContaCorrente(555,123,"Manoel",500)

conta_daniele.depositar(1000)
print(conta_daniele)
conta_jose.sacar(500)
print(conta_jose)