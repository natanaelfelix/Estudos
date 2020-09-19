"""
Zip - Unindo iteráveis
Zip_Longest - interatools
"""
from itertools import zip_longest
### Codigo
cidades = ['São Paulo', 'Belo Horizonte', 'Salavdor', 'Monte Belo']
estados = ['SP', 'MG', 'BA']
#cidades_e_estados = zip(estados, cidades) #uni as duas listas nmas um por vez, pois são iteráveis, o zip uni até a menor lista de todos
cidades_e_estados = zip_longest(estados, cidades) #uni as duas listas nmas um por vez, pois são iteráveis, o zip_longest uni toda lista mesmo incompleta

#for valor in idades_e_estados:
    #print(valor)

#podemos converter esse zip em lista, nas união das listas
l = list(cidades_e_estados)
# gerando dicionario = di = dict(cidades_e_estados)
print(l)
