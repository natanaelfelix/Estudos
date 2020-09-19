#todos os pacotes tem que ter o arquivo init

import VENDAS.Calcula_preco #importante de um pacote de um modulo ou
from VENDAS import Calcula_preco

preco = 49.90
preco_com_aumento = VENDAS.Calcula_preco.aumento(preco, 15)
print(preco_com_aumento)

