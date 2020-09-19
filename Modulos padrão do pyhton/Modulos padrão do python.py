import sys

print(sys.platform)

from sys import platform as so  # apelidando o que foi importando

print(so)

import random

print(random.randint(0, 10))

from random import randint, random  # importando mais de uma função

print(random.randint(0, 10))

# pip intall (nome do modulo) # para instalar um novo modulo, caso não tenha
# pip uninstall (nome do modulo) que será removido
# (__name__) ele mostra o nome do modulo
# todo modulo que está executando diretamente chama main se vir: if __name__ == __main__: tudo o q estiver abaixo não será executado só se for direto do modulo
