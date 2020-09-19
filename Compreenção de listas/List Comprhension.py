l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [variavel for variavel in l1] #iterando de forma mais rapida
ex2 = [v * 2 for v in l1]
ex3 = [(v, v2) for v in l1 for v2 in range(3)]

l2 = ['Luiz', 'Mauro', 'Maria']
ex4 = [v.replace('a', '@').upper() for v in l2]

tupla = (('chave', 'valor'), ("chave2", "valor2"),)
ex5 = [(y, x) for x, y in tupla]
ex5 = dict (ex5)
print(ex5['valor2'])

l3 = list(range(100))
ex6 = [v for v in l3 if v % 2 == 0] #numeros divisiveis por 2
ex7 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
ex8 = [v if v %3 == 0 else 'não é' for v in l3]

print(ex8)
