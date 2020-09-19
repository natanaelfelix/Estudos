"""
associação - usa | agragação - tem | Composição - é dono | Herança - é |


"""
from classes import *

c1 = Cliente('Luiz', 23)
c1.comprar()

c2 = ClienteVip('Ana' , 20, 'rosa') #uma classe herdando da outra as classes sempre vem de cima para baixo, quando subescrevemos algum metodo, por exemplo falar que já existe e é herdado, ele sobrepoe
c2.falar()

