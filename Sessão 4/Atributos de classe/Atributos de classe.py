class A:
    vc = 123

a1 = A()
a2 = A()

A.vc = 321 # eu consigo mudar todos os valores da variável , mas não da classe, mesmo que já tenha lá
#se eu quiser realmente alterar o valor de uma variável de classe:

A.vc = "Alterado"

print(a1.vc) # pegando o valor da variavel da classe q está disponível para todas as instancias
print(a2.vc)
print(A.vc)
