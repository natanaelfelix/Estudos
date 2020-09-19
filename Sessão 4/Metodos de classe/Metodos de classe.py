from random import randint


class Pessoa:
    ano_atual = 2019
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def get_ano_nascimento(self):
        print (self.ano_atual - self.idade)


    #o metodo abaixo precisa da classe pra ser executado, e abaixo é um decorador
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento): #cls se refere a classe pessoa, o metodo da classe fabrica o objeto pra gente, não é um metodo de instancia, ele se referecia a classe inteira
        idade = cls.ano_atual - ano_nascimento
        return cls(nome,idade)
    #static metodo não precisa nem da instancia nem da classe, seria uma função normal, mas precisa estar dentro da classe
    @staticmethod
    def gera_id():
        rand = randint(1000, 19999)
        return rand




p1 = Pessoa.por_ano_nascimento('Luiz' , 1987)
print(p1)
print(p1.nome, p1.idade)
print(p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gera_id()) #chamando direto
print(p1.gera_id()) #chamando pela instancia, mas esse metodo é idependente
