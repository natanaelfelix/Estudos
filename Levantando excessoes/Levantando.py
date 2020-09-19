def divide(n1, n2):
    try:
        return n1 /n2
    except ZeroDivisionError as error:
        print(error)
        raise #estou repassando essa excessão para o primerio try

try:
    print(divide(2,0))
except ZeroDivisionError as error:
    print(error)

#tendo nossa propria mensagem de erro
def divide(n1, n2):
    if n2 == 0:
        raise ValueError('N2 não pode ser 0')
    return n1 /n2
try:
    print(divide(2,0))
except ValueError as erro: # capiturando as excessões, tratando as própras excessões
    print(erro)


