perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2 ?',
        'respostas' : {'a': '1', 'b': '4', 'c' : '5',},
        'respostas_certa':'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3 * 2 ?',
        'respostas' : {'a': '4', 'b': '10', 'c' : '6',},
        'respostas_certa':'c',
    },
}
print()

for pk, pv in perguntas.items():
    print (f'{pk}:{pv["pergunta"]}')
    print ('Escolha uma das respostas abaixo')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}] : {rv}')
    print()
    rep = input('Qual sua resposta?')
    if rep == pv['respostas_certa']:
        print('Ehhhh"" Voce acertou!')
    else:
        print('Voce errou')
