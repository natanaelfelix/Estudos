"""
Split, join, enumerate em Python

* split - Dividir uma string #Str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elemento da lista #list / objetos iteráveis



string = "O Brasil é o país do futebol, o Brasil é penta."
lista_1 = string.split(" ") #Divide uma string gerando uma lista
lista_2 = string.split(",")

palavra  = ""
contagem = 0
for valor in lista_2:
    print (valor.strip().capitalize()) #Strip remove espaço do fim e do inicio da string #capitalize, deixa leita maiscula(inicial)

    #qtd_vezes = lista_1.count(valor)
    #if qtd_vezes > contagem:
        #contagem = qtd_vezes
        #palavra = valor
#print(f'A Palavra que apareceu mais vezes é:{palavra} ({contagem} x)')
    #print(f' A palavra {valor} apareceu {lista_1.count(valor)} x na frase') #Contando quantas x apareceu na frase


string = "O Brasil é penta."
lista = string.split(" ")
lista_2 = " , ". join(lista) #Fez a junção com virgulas, ou com o caractere que queremos
print(lista_2)


string = "O Brasil é penta."
lista = string.split(" ")

for indice, valor in enumerate(lista): #desempacotando e mostrando os valores, iterando
    print(indice, valor)

#Colocanod uma lista dentro de outra lista
lista = [
    [1,'Luiz'],
    [3,'João'],
    [5,'Maria'],
]
for v in lista:
    print (v[0], v[1]) #acessando os indices dos indices a cada iteração da lista

#Função enumerate retorna tuplas
"""
#desempacotando

lista = ['Luiz', 'João', 'Maria']

n1 , n2, n3 = lista #Desenpacotando e agregando cada valor numa variável
print (n2)
