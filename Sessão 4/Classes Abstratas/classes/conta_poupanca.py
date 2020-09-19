from classes.conta import Conta


class ContaPoupanca(Conta):
    def saque(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
            return
        self.saldo = self.saldo - valor
        self.detalhes()

