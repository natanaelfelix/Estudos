from abc import ABC, abstractmethod

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

class Conta:
    @abstractmethod
    def saque (self, valor):
        if not isinstance(valor, (int, float)): # verificação se o valor e uma instacia de int ou float
            raise ValueError ('Valor do depósito Precisa ser numéro')


class Cliente(Pessoa):
    pass

