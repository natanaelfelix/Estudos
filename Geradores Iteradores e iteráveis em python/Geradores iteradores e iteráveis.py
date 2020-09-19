"""
lista = [0,1,2,3,4,5,] #é iterável
lista = 'string' #tambem iterável e podemos utilizar o for para exibir os valores dessa lista
for v in lista: #tranforma nossa lista em um iterador, porque lista não é
    print (v)
lista2 = iter(lista) #agora a lista se tornou iteravel e já um iterador, que dá um valor de cada vez

print (next(lista2))
print (next(lista2))
print (next(lista2))
print(hasattr(lista, '_next_')) #verifica se é um iterador

"""
import sys
import time
lista = list(range(1000)) # a lista está toa salva na memoria, no caso os 1000 valores
print(sys.getsizeof(lista)) #pegando o valor que ocupa na memoria, no caso a lista

def gera():
    r = []
    for n in range(100):
        r.append(n)
        time.sleep(0.1)
    return r
g= gera()

for v in g:
    print(v)
#Valores sendo gerados um de cada vez

def gerador():
    for n in range(100):
        yield n
        time.sleep(0.1)
g= gerador()

print(hasattr(g, '__next__'))

for v in g:
    print(v)
#dá para utilizar o valor gerado a cada vez, utilizando a função next

l1 = [x for x in range (1000)] # lista normal com tamno grande e todos os valores
l2 = (x for x in range (1000)) #tranformei em gerador utilizando list compreensão, aqui entrega um valor por vez e é pequeno uso de memoria
