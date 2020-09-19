from Map import produtos, pessoas, lista

nova_lista = map(lambda x: x * 2, lista) #mapeando os valores utiliando o mapeamento de dados no caso estou colocando o x para receber cada valor e multiplico esse valor por2, e o map só aceita função, por isso estamos utilianzod lambda que é uma funçãoa aninima
print(list(nova_lista))

precos = map(lambda p: p ['preco'], produtos) #retornando apenas o valor de uma chave q eu quero no dicionário

print(list(precos))

#aumentando % desses valores dentro do dicionário

def aumenta_preco (p):
    p['preco'] = round(p['preco'] * 1.10 ) #estou acessando o dicionário direto da função e alterando o valor do dicionário, dicionário e lista podem ser alteradas menos tuplas
    return p

precos = map(aumenta_preco, produtos)
for produtos in precos:
    print(produtos)


nomes = map(lambda p : p['nome'], pessoas) #pegamos apenas o nome a chave nome do dicionário

for pessoas in nomes:
    print(pessoas)
