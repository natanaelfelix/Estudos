"""
Listas em Pyhton
fatiamento
append, insert, pop, del, clear, extend, +
min, max,
range
"""
booleanos = True
inteiro = 10
flutuante = -10.10
strings = "textos"

#para criar listas, só colocar o nome da variavel recebendo colchetes
#         0    1    2    3     4    5
lista = ['a', 'jumento', 'c', 'd', 'e'] #as listas tem indices como as strings, suportam vários valores e esses valores podem ser de vários tipos diferentes
#    -     6     5    4    3    2    1

for enu, nume in enumerate(lista): #acessei a lista e enumerei os indices da lista
    print(enu, nume)
print(lista[1]) #pega o indice da lista

print(lista) #para ver a lista inteira
#ex:
string= 'abcde'
print(string[3]) #Acessando o indice de uma string apenas um indice não uma lista


#         0    1    2    3     4    5
lista = ['a', 'jumento', 'c', 'd', 'e']
print (lista)
fat = lista[::2] #fatiamento de strings, o ultimo seria o salto
print (fat)
lista[4] = "Qualquer outra coisa" #Trocando o valor do indice 5 da lista por qualquer outra coisa, suporta também fatiamento de strings
print (lista)
fatia = lista[::-1] #para inverter valores na lista e começar de tras para frente, só colocar o -1 no fim
print (fatia)

#######################################################3

l1 =[1,2,3]
l2 =[4,5,6]
l3 = [l1+l2] #cocatenando as duas listas, poderia ser feito com a função extend, igual abaixo
l1.extend(l2) #função extend
l2.append("b") #função append que insere no fim da lista(vetor), nesse caso estamos utilizando umas string
l2.insert(0, "b") #inserindo o valor na posição que queremos, nesse caso posição 0, e todos os demais valores mudam o indice
l2.pop() #deleta o ultimo indice, no caso B
l2 =[1,2,3,4,5,6]
del(l2[3:5]) #excluindo uma fatia que escolhemos utilizando o del, para isso coloquei de qual indice até qual indice eu quero remover os valores
l2 =[1,2,3,4,5,6]
del(l2[0]) #deletando apenas um intem da lista que está no indice 0
print(l2)
print(max(l2)) #pega o maior valor da lista que está armazenados nos indices
print(min(l2)) #pega o menor valor da lista que está armazenados nos indices

################################

l2 = list(range(0,10)) #list é a função que converte objetos iteráveis em uma lista
for num in l2:
    print(num)          #iterando com a lista


###################################################
secreto = "Perfume"
digitadas = []
chances = 3

while True:
    if chances <=0:
        print("voce perdeu!!")
        break
    letra = input("digite uma letra:")

    if len (letra)>1:
        print("isso não vale, digite apenas uma letra.")
        continue
    digitadas.append(letra)
    if letra in secreto:
        print(f"uhull, a letra '{letra}' existe na palavra secreta.")
    else:
        print(f"Afff a letra '{letra}' não existe na palavra secreta:.")
    secretotemp = ""
    for letrasecreta in secreto:
        if letrasecreta in digitadas:
            secretotemp + letrasecreta
        else:
            secretotemp += "*"
    if secretotemp == secreto:
        print(f'Que legal, voce ganhou a palavra secreta era {secretotemp}.')
        break
    else:
        print(f'A palavra secreta está assim: {secretotemp} ')
    if letra not in secreto:
        chances = chances -1
    print(f'Voce ainda tem {chances}.')
    print ()
