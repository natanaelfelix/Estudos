class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse  = self.__class__.__name__

    def falar (self):
        print(f'{self.nomeclasse} falando...')

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando...')

class ClienteVip(Cliente):
    def falar(self):
        super().falar() #ele busca nas super classes primeiro, e então executa depois ele desce
        Pessoa.falar(self) # odemos chamar diretamente da classe
        print('outra coisa qualquer')
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome =sobrenome

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')
