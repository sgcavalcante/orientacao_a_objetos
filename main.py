from lampada import Lampada
from conta import Conta
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


conta_pedro = Conta(123,147,"Pedro")
conta_jose = Conta(123,147,"José")
print(f'{25*"-"}Deposito{25*"-"}')
print(f"Saldo da conta de {conta_pedro.titular} é {conta_pedro.saldo}!")
conta_pedro.depositar(1000)
print(f"Novo Saldo da conta de {conta_pedro.titular} é {conta_pedro.saldo}!")
print(f'{25*"-"}Deposito{25*"-"}')
print(f"Saldo da conta de {conta_jose.titular} é {conta_jose.saldo}!")
conta_jose.depositar(500)
print(f"Novo Saldo da conta de {conta_jose.titular} é {conta_jose.saldo}!")

#conta_jose.sacar(450)
#print(f"Novo Saldo da conta de {conta_pedro.titular} é {conta_pedro.saldo}!")
print(f'{25*"-"}Transferência{25*"-"}')

conta_pedro.transferir(500,conta_jose)   
print(f"Novo Saldo da conta de {conta_pedro.titular} é {conta_pedro.saldo}!")
print(f"Novo Saldo da conta de {conta_jose.titular} é {conta_jose.saldo}!")