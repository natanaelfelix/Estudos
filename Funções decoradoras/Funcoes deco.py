#vão envolver as funções que quisermos mudando ou não o comportamento
"""
def fala_oi():
    print('Fala OI')

variavel = fala_oi
print(type(variavel))
"""

def master(funcao):
    def slave():#função escrava
        funcao()
    return slave

@master #esse é o decorador, faz o mesmo que o codigo comentado abaixo
def fala_oi():
    print('Fala OI')

fala_oi()
#variavel = master(fala_oi) #está retornando a função escrava, nesse formato é função ecorada
#variavel()
