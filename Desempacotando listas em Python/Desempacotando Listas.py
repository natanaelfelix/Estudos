lista = ['Luiz', 'João', 'Maria', 0,1,2,3,4,5]

#n1 , n2, n3 = lista #Desempacotando e agregando cada valor numa variável, caso seja menos variável do que o valor da listas o codigo abaixo resolve

n1 , n2, *outra_lista, ultimodalista = lista #o restante dos valores acaba por ir para outra lista, e pegando já o ultimo valor apos a virgula, ou qualquer outro valor

print (n2, outra_lista, ultimodalista)
