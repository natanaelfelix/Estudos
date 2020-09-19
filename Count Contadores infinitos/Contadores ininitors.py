#count gera um contador que é um iterador
from itertools import count

contador = count(start =5, step = 2) #iterador, tomar cuidado para não dar loop, nesse exemplo começará a partir do 5, e pulando de dois em dois
print(contador)
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
