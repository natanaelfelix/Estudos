'''
class A:
    def falar(self):
        print('Falando, estou em A')


class B(A):
    def falar(self):
        print('Falando, estou em B')

class C(A):
    def falar(self):
        print('Falando, estou em C')


class D (B, C): # Herda tudo que tem nas classes que foram passadas, essa é multipla, mas tem o problema de diamanda porque as outras tbm herdam e não sabe de onde pegar
    # nesse caso ele procura primeiro no B que foi passado, se não for encontrado em B, ai é encontrado no proximo, C
    # se colocarmo um metodo nesse classe, ele pega dela.
    pass
# quando utilizamos herança multipla, devemos utilizar uma classe mixing, tem uma função adicional e não está presente na hierarquia de classes

d = D()
d.falar()
'''
from smartphone import Smartphone

smartphone = Smartphone ('Pocophone F1')
smartphone.conectar()
smartphone.desligar()
smartphone.ligar()
smartphone.conectar()
smartphone.conectar()
smartphone.conectar()
smartphone.desligar()
smartphone.conectar()
smartphone.desconectar()
