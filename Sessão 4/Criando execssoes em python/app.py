class TaErrado(Exception): #foi criado uma excessão
    pass

def testar():
    raise TaErrado('Errado')
try:
    testar()
except TaErrado as error:
    print(f'Erro {error}')

