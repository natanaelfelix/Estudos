from itertools import groupby


alunos = [
    {'nome': 'Luiz', 'nota' : 'A'},
    {'nome': 'João', 'nota' : 'B'},
    {'nome': 'Peres', 'nota' : 'A'},
    {'nome': 'Lucio', 'nota' : 'C'},
    {'nome': 'Rodolfo', 'nota' : 'D'},
    {'nome': 'Larissa', 'nota' : 'E'},
]
ordena = lambda item: item ['nota'] #para agrupar é necessáro orbigatóriamnete ordenar o dados
alunos.sort(key = ordena)
alunosagrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunosagrupados:
    print(f'agrupamento:{agrupamento}')
    for aluno in valores_agrupados:
        print(aluno)


