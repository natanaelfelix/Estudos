def saudacao (saudacao, nome):
    print(saudacao, nome)

ola = saudacao('Bom dia', 'Otávio')


def soma(num1, num2, num3):
    print(num1+num2+num3)

numeros = soma (2,2,2,)

def aumento(valor1, porcentual):
    return ((valor1 * porcentual) / 100) + valor1
valores = aumento(50,10)
print(valores)

def jogo (n1):
    if  n1 % 3 == 0 and n1 % 5 == 0 :
        resp = 'FizzBuzz'
    elif n1 % 3 == 0:
        resp = 'Fizz'
    elif n1 % 5 == 0:
        resp = 'Buzz'
    else:
        resp = n1
    return (resp)

valores = jogo(1)
print(valores)
