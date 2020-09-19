""""
Formatando valores com modificadores:

:s - Texto (Strings)
:d - Inteiros (Int)
:f - Numero de ponto flutuante (Float)
:.(numero)f -
:(caractere)

*Posição

> - esquerda
< - direita
^ - centro


utilizando as funções format e f strings
"""
num1 = 10
num2 = 3
divisão = num1 / num2
print('{:.2f}'. format(divisão)) #Irá formatar com duas casas decimais para numeros flutiantes depois do ponto, e por isso está 2(casas decimais) f (para numero flutuante)
print(f'{divisão:.2f}') #Utilizando f strings para formatar para casas decimais

nome = "Natanael"
print(f'{nome:s}') #Utilizando a fomatação apenas para dizer que string, o restante tem a mesma ideia

num1 = 1
print(f'{num1:0>10}') # colocando para ser exibido 10 casas de 0, a esqueda do numero 1, usando f strings

num1 = 1150
print(f'{num1:0<10}') # para mudar a posição do 0 só alterar o sinal, mas ele mostra contando com as casas já existentes

num1 = 1150
print(f'{num1:0>10.2f}') #juntando os dois tipo de formatação, colocando casas e separando por  casas decimais o numero inteiro.

nome = 'Natanael'
print(f'{nome:#^50}') #para colocar o numero de caracteres que queremos em um print, no caso o nome irá aparecer no meio

nome = 'Natanael'
print(len(nome)) #Contando o tamanho da string, podemos contar e tambem tirar saber quantos caracteres foram adcionados e quantos ficam em casa posição do print
nomeformatado = '{:@>50}'.format(nome) #Adicionou os @ a esquerda do nome e formatando já.
print(nomeformatado)

nome = 'Natanael'
nomeformatado = '{n:#^20}'.format( n = nome) #Chamando variável dentro do print e podemos mostar quantas vezes queremos(iteravel)
print(nomeformatado)

nome = 'Natanael'
sobrenome = "silva"
nomeformatado = '{1} {0:#>50}'.format(nome, sobrenome) # usando indice, apenas colocamos a posição, que começa sempre de 0, para cada variável devemos abrir um colchetes
print(nomeformatado)
