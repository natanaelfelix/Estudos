from Map import produtos, pessoas, lista
from functools import reduce #função de acumulação de valores

acumula = 0
for item in lista:
    acumula = acumula + item
print (acumula)

#utilizando a função reduce

soma_lista = reduce(lambda ac, i: i + ac, lista, 0) # o ac é um acumulador, o i e ou outro i é ao que eu irei pegar da minha lista, e o 0 é de qual valor irá começar
print(soma_lista)

soma_precos = reduce(lambda ac, p: p["preco"] + ac , produtos, 0)
print(soma_precos / len(produtos)) #soma de todos os preços do dicionário, nesse caso tbm estamos pegando a média dos produtos

soma_idades = reduce(lambda ac, i: i['idade']+ ac , pessoas, 0)
print(soma_idades / len(pessoas))
