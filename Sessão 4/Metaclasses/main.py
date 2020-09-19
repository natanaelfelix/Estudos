"""
Em pyhton tudo é um objeto: incluindo classes
metaclasses são as "classes" que criam classes.
type é uma metaclasse
"""
"""
class A:
    attr = 'Valor'
a = A()
b = A()
c = A()

"""
class Meta(type):
    def __new__(mcs, name, bases, namespace):
        print(name)
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)
        if 'b_fala' not in namespace:
            print(f'Oi voce precisa criar o metodo b_fala {name}')
        else:
            if not callable(namespace['b_fala']):
                print(f'O metodo b_fala precisa ser um metodo não atributo {name}')
        return type.__new__(mcs, name, bases, namespace)

class A (metaclass=Meta):# toda classe que herdar de A vai se comportar da maneira que eu falar na metaclasse
    def fala(self):
        self.b_fala() # estou chamando um metodo da classe filha

class B(A): # ta herdando a classe de cima
    b_fala = 'Wow'
    pass

    #def b_fala(self):
        #print('Oi')

# crianda classe com o type:
class Pai:
    nome = 'Teste'

A = type('A', (Pai,), {'attr': 'Olá Mundo!'}) #parece list conpreenção

a = A()
print(a.nome)

