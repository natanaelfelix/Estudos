"""
def saudacao():
    primeiro = 'Olá'
    return primeiro
def nome(var):
    segundo = 'Joana'
    return f'{segundo} , {var}'

var = saudacao()
fun = nome(var)
print(fun)
"""
def mestre (funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'oi{nome}'

def saudacao (nome, saudacao):
    return f'{saudacao} {nome}'

executando = mestre(fala_oi, 'Natanael')
executando2 = mestre (saudacao, 'Natanael', saudacao = 'Bom dia')
print(executando)
print (executando2)
