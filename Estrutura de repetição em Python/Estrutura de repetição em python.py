"""
Temos duas maneiras de fazer repetição:
Laço while e for

*While em python
utilizado para realizar ações enquanto uma condição for verdadeira

Requisitos: Entender condições e operadores


Debug passa linha por linha no pycharm para debugar

podemos ter um laço dentro do outro

"""
x = 0
while x < 10:
    if x == 3:
         x = x + 1
         continue #ele pula para o proximo laço, ou seja nesse caso pulamos o 3
    print(x)
    x = x + 1
print("Acabou!")

x = 0
while x < 10:
    if x == 3:
         x = x + 1
         break #ele para nesse loop e termina o programa
    print(x)
    x = x + 1
print("Acabou!")

##########################################################3
#Calculadora

while True:
    print()
    num1 = input('Digite um numero:')
    operador = input('Digite um operador:')
    num2 = input('Digite outro numero:')



    if not num1.isnumeric() or not num2.isnumeric():
        print('Você precisa digitar um número!')
        continue

    num1 = int(num1)
    num2= int (num2)

    if operador == '+':
        print( num1 + num2)
        sair = input('Você deseja sair? [s] ou [n]ão ')
        if sair == 's':
            break
    elif operador == '-':
        print( num1 - num2)
        sair = input('Você deseja sair? [s] ou [n]ão ')
        if sair == 's':
            break
    elif operador == '*':
        print( num1 * num2)
        sair = input('Você deseja sair? [s] ou [n]ão ')
        if sair == 's':
            break
    elif operador == '/':
        print(num1 / num2)
        sair = input('Você deseja sair? [s] ou [n]ão ')
        if sair == 's':
            break
    else:
        print('Operador invalido!')
