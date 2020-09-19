"""

iterando strings com while em Python
que é percorrer cada elemento do objeto


"""


minha_string = 'O rato roeu a roupa do rei de roma.'
tamanhodastring = len(minha_string)
c = 0
while c <tamanhodastring:
    print(c, minha_string[c])
    c = c +1

minha_string = 'O rato roeu a roupa do rei de roma.'
tamanhodastring = len(minha_string)

print(minha_string.count('a')) #paracontar quantas vezes ocorre
c = 0
novastring = '' #Strig vazia mas é string por conta das aspas
while c <tamanhodastring:
    if minha_string[c] == "r":
        novastring = novastring + minha_string[c].upper() #aqui está concatenando e trocando o valor de c pelo mesmo valor do contador para percorrer os indices da string
    else:
        novastring = novastring + minha_string[c]
    c = c +1
print(novastring)

 #Conta a quantidade de vezes que uma letra é repetida
#utilizamos indices, contadores e acessandos os indices e utilizando os contadores como indices
minha_string = 'O rato roeu a roupa do rei de roma.'
tamanhodastring = len(minha_string)
print(minha_string.count('a')) #paracontar quantas vezes ocorre

c = 0
contagem = 0
letra = '' #Strig vazia mas é string por conta das aspas
while c <tamanhodastring:
    conta = minha_string.count(minha_string[c])

    if contagem < conta and minha_string[c].strip(): #strip tira os espaços de inicio e sim da string
        letra = minha_string[c]
        contagem = conta
    c = c + 1
print(letra, contagem)
