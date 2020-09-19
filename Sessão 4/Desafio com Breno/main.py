from classes.conta import Conta
from classes.banco import Banco
from classes.classes import Pessoa, Cliente
from classes.ccpp import ContaCorrente

CO = Conta(123, 21, 0000)
CL = Cliente(CO, 'João', 21)
IT = Banco(CO, CL)
CG = ContaCorrente(CO.agencia, CO.conta, CO.saldo, CO.limite)

decisao = input('O que voce pretende fazer agora, consultar saldo (c), sacar (s), depositar(d)? ')
if decisao == 'c':
    CG.consulta()

elif decisao == 's':
    IT.autenticacao(CL, CO._conta, CO._agencia)
    if IT == False:
        saqu = int(input('Digite o valor para saque:'))
        CG.sacar(saqu)

if decisao == 'd':
    dep = int(input('Digite o valor para deposito'))
    CG.depositar(dep)


