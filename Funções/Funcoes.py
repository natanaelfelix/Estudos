"""
Funções py - Def em python (Parte 1)
"""
"""
#definindo função
def funcao():
    print('Olá Mundo!')

#Chamando a função:
funcao()

#definindo função
def funcao(msg):
    print(msg)

#Chamando a função passando string como parametro:
funcao('Mensagem')

def saudacao(msg, nome):
    print(msg, nome)

#Chamando a função passando string como parametro:
nome = "nome"
saudacao('Mensagem', nome)

def saudacao(msg = 'mensagem', nome = "nome"): # definindo como padrão caso não seja passado nenhum parametro
    print(msg, nome)

#Chamando a função passando string como parametro:
saudacao('Mensagem', nome)

lista = [1,2,3,4,5] #Fazendo um desempacotamento e empacotamento
n1, n2, *n = lista
print(n1, n2, n)

lista = [1,2,3,4,5] #Fazendo um desempacotamento e empacotamento
print(*lista) #desempacoto tudo que está dentro da lista

"""

# *args e **kwargs esse segundo é para argumentos nomeados
def func(*args): #é um empacotamento e desempacotamento o * desempacota
    args = list(args) #fazendo cashing e transformando em lista
    print(args[0])
    print(args[-1])
    print(args)
    print(len(args))

func (1,2,3,4,5)

variavel = 'valor'




