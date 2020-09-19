# a diferença da tupla pra lista é que não podemos editar os valores da tupla
t1 = (1,2,3, 'Natanael') #Tupla, depois de criadonão podemos modificar, para acessar esse elemento, devemos acesso o indice, começando do 0

print(t1[3])

t1 = list(t1) #Fazendo cast para lista, e agora podemos alterar os valores
t1 = tuple(t1) #Fazendo cast para voltar a ser tupla
#podemos criar tupla sem os parenteses tbm
