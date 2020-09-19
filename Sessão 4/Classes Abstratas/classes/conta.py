from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)): # verificação se o valor e uma instacia de int ou float
            raise ValueError ('Saldo Precisa ser numéro')
        self._saldo = valor
    def depositar (self, valor):
        if not isinstance(valor, (int, float)): # verificação se o valor e uma instacia de int ou float
            raise ValueError ('Valor do depósito Precisa ser numéro')
        self.saldo =  self.saldo + valor
        self.detalhes()

    def detalhes(self):
        print(f'Agencia:{self.agencia}', end = " ")
        print(f'Agencia:{self.conta}', end = " ")
        print(f'Agencia:{self.saldo}', end = " ")

    @abstractmethod # estamos forçcando que as classes filhas tenham o metodo saque
    def saque (self, valor):
        if not isinstance(valor, (int, float)): # verificação se o valor e uma instacia de int ou float
            raise ValueError ('Valor do depósito Precisa ser numéro')

