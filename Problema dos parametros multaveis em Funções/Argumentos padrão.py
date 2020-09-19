#lista e dicionários

def lista_de_cliente(clientes_iteravel, lista=[]): #por ser multavel adiciona valores mas copia os anteriores
    lista.extend(clientes_iteravel)
    return lista

clientes1 = lista_de_cliente(['João', 'Maia', 'Eduardo'])
clientes2= lista_de_cliente(['Marcos', 'jonas', 'felipe'])
print(clientes1, clientes2)

# Mutável: Listas, dicionários
# Imutável: Tuplas, strings, números, True, False, None


def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista


lista_clientes_1 = ['Fabrício']
clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'], lista_clientes_1)
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'])
clientes3 = lista_de_clientes(['José'])

print(clientes1)
print(clientes2)
print(clientes3)
