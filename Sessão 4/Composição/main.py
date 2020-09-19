"""
uma classe será dona de outros objetivos, se uma classe for apagada outra classe perde todos os objetos
"""

from classes import Cliente
cliente1 = Cliente('Luiz', 32)
cliente1.insere_endereco('Belo Horizonte' , 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
print()


cliente2 = Cliente('Maria', 55)
cliente2.insere_endereco('Salvador Bahia' , 'BA')
cliente2.insere_endereco('Rio de Janeiro' , 'RJ')
print(cliente2.nome)
cliente2.lista_enderecos()
print()
