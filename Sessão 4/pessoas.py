from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
    #metodos são funçãoes que pertencem a classe, quando está dentro da classe é metodo
    #self são referenciados as instancias, para que quando chamarmos ele saber de qual instancias é
    """
    def falar(self):
        print('A pessoas está falando...')
    """
    #metodo especial é o init
    def __init__(self, nome, idade, comendo=False, falando=False):# o self sempre vem antes para referenciar a instancia
        #utilizando a estrutura abaixo pois é como se criasse uma variáriavel q receberá o valor de cada parametro
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self. falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return
        if self.falando:
            print(f'{self.nome} já está falando')
            return
        print(f'{self.nome} está falando {assunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} ele não está falando')
            return
        print (f'{self.nome} parou de falar')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print((f'{self.nome} já está comendo'))
            return
        if self.falando:
            print(f'{self.nome} não pode comer falando')
            return
        print(f'{self.nome} está comendo {alimento}')
        self.comendo =True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return
        print(f'{self.nome} parou de comer.')
        self.comendo = False
    def get_ano_nacimento(self):
        return self.ano_atual - self.idade



        # todas as variáveis que utilizam o self, podem ser acessadas por outro metodo(função) dentro da classe
"""
    def outro_metodo(self):
        print(self.nome)
"""
