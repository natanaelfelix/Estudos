file = open ('abc.txt', 'w+') #quando se colocar o w+ ele tem a funçã de leitura e escrita
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')
print(file.read())
# se eu quiser ler o arquvio novamento é necessário abri ele de novo ou voltar do inicio
file.seek(0,0) # está indo pro topo do arquivo e buscando os caracteres 0 a 0 ou seja tudo
print(file.read())
file.seek(0,0)
print(file.readline(), end="")# só lê uma linha, por estar com quebra de linha, o end tira isso
print(file.readline(), end= '')

file.seek(0,0)
print((file.readlines())) # se pedimos todas as linhas vem uma lista
#podemos utilizar um for tambem
file.close

# melhor maneira de se trabalhar com arquivo no python

#with é um gerador de contexto, a diferença é que ele fecha o arquivo automaticamente asism que terminar o uso

with open ('abc.txt', 'w+') as file:
    file.write('Linha 4\n')
    file.write('Linha 4\n')
    file.write('Linha 4\n')

    file.seek(0)
    print(file.read())

with open ('abc.txt', 'r') as file: # só lendo
    print(file.read())

with open ('abc.txt', 'a+') as file: # adiona informações sem apagar nada, colocando o cursor no fim do arquivo
    file.write('Outra Linha\n')
    file.seek(0)
    print(file.read())
#import os
#os.remove(nome do arquivo) para remover o arquivo ou excluir
