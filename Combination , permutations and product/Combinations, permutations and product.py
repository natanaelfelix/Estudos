from itertools import combinations, permutations, product


#pessoas = ['Luiz', 'André', 'Eduardo', 'Leticia', 'Fabricio', 'Rose']
#for grupo in combinations(pessoas,2):# modulo combinations verifica quantas combinações podem ser feitas com base no pasres que queremos dentro da lista
    #print(grupo)
#usando o combinations, não importa a ordem, caso for necessario que a ordem importe, utilizaremos o permutation
#pessoas = ['Luiz', 'André', 'Eduardo', 'Leticia', 'Fabricio', 'Rose']
#for grupo in permutations(pessoas,2):# modulo combinations verifica quantas combinações podem ser feitas com base no pasres que queremos dentro da lista
    #print(grupo)
pessoas = ['Luiz', 'André', 'Eduardo', 'Leticia', 'Fabricio', 'Rose']
for grupo in product(pessoas, repeat = 2): # verifica todas combinações possiveis com a ordem importantando e mesmo repetindo valores
    print(grupo)
