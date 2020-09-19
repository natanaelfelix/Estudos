from abc import abstractmethod


class Conta:
    def __init__(self, agencia, nconta, saldo):
        self.agencia = agencia
        self.conta = nconta
        self.saldo = saldo
        self.limite = 1000


    @abstractmethod
    def sacar (self):
        return self.sacar
