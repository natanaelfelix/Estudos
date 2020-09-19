'''
from abc import ABC, abstractmethod

class A (ABC):
    # faz com que todas as classes que heredem de A tenham o metodo que foi atribuido como abstrato no caso no metodo Falar, abaixo.
    @abstractmethod
    def falar(self):
        pass
# não é possível instanciar classe que usam metodos abstartos
class B (A):
    def falar(self):
        print('Falando... B...') # como estamos sobescrevendo o metodo acima, então podemos utilizar
    pass


a = A() # QUANDO TEMOS METODO ABSTARTO EM CLASSES, NÃO PODEMOS INSTANCIAR A CLASSE
a.falar()
'''
'''
from classes.conta_poupanca import ContaPoupanca

cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(10)
cp.saque(5)
cp.saque(5)
cp.saque(1)

'''
from classes.cc import ContaCorrente

cc= ContaCorrente(1111, 3333, 0 , 500)
cc.depositar(100)
cc.saque(250)


