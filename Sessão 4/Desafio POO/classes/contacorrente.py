from conta import Conta



class ContaCorrente(Conta):
    def __init__(self, agencia, nconta, saldo, limite = 1000):
        super().__init__(agencia, conta, saldo)
        self.agencia = agencia
        self.nconta = nconta
        self.saldo = saldo

    def saque(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente')
            return
        self.saldo = self.saldo - valor
        self.detalhes()


    def depositar (self, valor):
        self.saldo =  self.saldo + valor

