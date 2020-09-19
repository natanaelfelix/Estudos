"""
é quando uma classe conversa com outra, mas nenhuma depende da outra
"""
from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever


escritor = Escritor('João')
#print(escritor.nome)
caneta = Caneta('Bic')
#print(caneta.marca)
maquina = MaquinaDeEscrever()
print(maquina)
