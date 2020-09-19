from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite):
        super().__init__(self,agencia, conta, saldo, limite)

    @property
    def limite(self):
        return(self._limite)

    def deposito (self, valor):
        self.saldo =  self.saldo + valor

    def sacar(self, valor):
        print('Seu saldo anterior:', self.saldo)
        self.saldo = self.saldo - valor
        print('Foi sacado', valor)
        print('Seu saldo atual é de:', self.saldo)

    def consulta(self):
        print(self.saldo)

class ContaPoupanca(Conta):
    def __init__(self, agencia, nconta, saldo,):
        super().__init__(self, agencia, nconta, saldo)

    def deposito (self, valor):
        print('Foi depositado', valor)
        self.saldo =  self.saldo + valor
        print('O Saldo atual é de:', self.saldo)
        return

    def sacar(self, valor):
        print('Seu saldo anterior:', self.saldo)
        self.saldo = self.saldo - valor
        print('Foi sacado', valor)
        print('Seu saldo atual é de:', self.saldo)
        return

    def consulta(self):
        print(self.saldo)
        return
