"""
nome = input('Qual o seu Nome?')
if nome:
    print(nome)
else:
    print('Voce não digitou nada!')

"""

#Simplificando as coisas

nome = input('Qual o seu Nome?')
print(nome or 'Voce não digitou nada!')
#Verifica se o que tem na variável foir verdadeiro mostra caso contrário mostra a mensagem, ele para sempre na primeira opção verdadeira, e podemos usar vários Ors
