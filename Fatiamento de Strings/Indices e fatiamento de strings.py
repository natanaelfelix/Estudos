"""
Manipulando arquvios

*fatiamento indices
*fatiamento de strings [inicio:fim:passo]
* função built-in len, abs, type, print, etc..
essas funções podem ser usadas diretamente em cada tipo

podemor ver isso no site do py

"""

#positivos
texto = "Python s2" #Cada caractere dentro dessa string tem um indice
print (len (texto)) #apenas para saber o tamanho da string o temanho é o mesmo que o indice e a posição que queremos
print (texto[8]) #Acesso qualquer indice que quero colocando o numero começando de 0 e considera até espaço

#para removermos uma palvra da str utlizando indices

url = "www.google.com/" #iremos remover a barra, para isso deve ser contado de t´ras para frente, com numeros negativos
print (url[:-1]) # -1 é a posição onde está a /

#Fatiando uma string


texto = "Python s2"
novastring = texto[0:6] #estou escolhendo de onde até onde eu quero pegar o texto, sempre com um numero a mais se não não pega.
print(novastring)
novastring = texto[7:] #vai até o fim da string, isso é uma fatia da string
print(novastring)
novastring = texto[0::2] # vai pulando de 2 em 2, mudar o 2 ele pula conforme a quantidade que queremos
print(novastring)
