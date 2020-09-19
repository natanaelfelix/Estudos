from Map import produtos, pessoas, lista

#iremos criar uma nova lista, dicionário filtrando coisas de outra lista

#nova_lista = filter(lambda x: x >5, lista) #o filter retorna verdadeiro ou falso, os que forem falso são removidos da nova lista
#nova_lista = [ x for x in lista if x >5] #utilizando o list comprehension

nova_lista = filter(lambda p: p['preco'] >50, produtos) # como estamos pegando de dicionário, podemos iterar sobre ele

for produto in nova_lista:
    print(produto)

