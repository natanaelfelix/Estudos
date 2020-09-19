def funcao (arg, arg2):
    return arg * arg2
var = funcao (2,2)
print (var)

#ou com expressoes lambda, é a mesma coisa do que essa de cima, essa de baixo é anonima

a = lambda x, y : x * y
print(a(2,2))

lista = [ ['P1', 13],['P2', 6],['P3', 7],['P4', 50],['P5', 8]]
#sUPONHAMOS QUE QUEIREMOS ORDENAR, COM A EXPRESSÃOES LAMBDAS FICA MAIS FACIL.
lista.sort(key= lambda intem: intem [1]) #estamos ordenando a partir do item 1 da lista

print(lista)
print(sorted(lista, key= lambda i: i [0]))
