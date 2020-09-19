"""
For / Else em Python


variavel = ["Luiz Otáveio", "João", "Maria"]


for valor in variavel:
    print(valor)
    #break #quebra o laço
    continue #Continua pro proximo laço
"""
variavel = ["Luiz Otáveio", "João", "Maria"]
for valor in variavel:
    if valor.startwith("J"):
        print("Começa com J", valor)
    else:
        print("Não começa com J")
