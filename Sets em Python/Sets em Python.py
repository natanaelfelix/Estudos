s1 = {1,2,3,4,5,6} #é um set e não tem pares, são conjuntos , e recebem valores e não são multaveis, não tem indice , não tem como acessar um valor especifico

for v in s1: #iterando
    print(v)

#para add
s1 = set () #adicionando elemento eme um set vazio
s1.add(1) #ou update, mas o update adicona tudo quebrado dentro do python
s1.add(2)
s1.add(3)
s1.discard(2) #eliminando um elemnto

print(s1)

#set não respeita ordem, podem aparecer em qualquer ordem, e o set não aceita elemento duplicados
#geralmente utilizaremos set para eliminar elemento duplicados numa lista, só fazer um cast da lista para o set

s1 = {1,2,3,4,5}
s2 = {1,2,3,4,5,6,}
se3 = s1 | s2 #colocando os dois sets juntos, é pip ou union
print(se3)
