d1 = {"chave1": "Valor da chave"}
d1 ["nova_chave"] = "Valor da nova chave" #adicionando uma nova chave, podemos utilizar o update tambem
print(d1)
print(d1["chave1"]) #acessando só um valor da chave

#outra maneira de criar um dicionário
#podemos utilizar como chaves, tuplas, inteiro, e str

d2 = dict(chave1 = "valor da chave", chave2 = "valor da outra chave") #chaves no dicionário precisam ser unicas, não podem ser repetir
print(d2)

del d1 ["nova_chave"] #deletando um item do dicionário
print (d1)

#para iterar sobre os itens:

d3 = {"Chave1": "valor", 'chave2': 'outro valor', 'chave3': 'tupla'}

for k in d3.items(): #iterando para ver todos os itens, para ver só chave utilizar o k, para valor, v e depois do in d3.values
    print(k)

for k, v  in d3.items(): #iterando para ver todos os itens, para ver só chave utilizar o k, para valor, v e depois do in d3.values, no caso acessando os dois separados
    print(k, v)
#para copiar um dicionário, utilizar o modulo copy
#é possivel converter listas e tuplas para dicionários, contanto que tenham dois valores foramando pares.
