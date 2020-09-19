string = '01234567890123456789012345678901234567890123456789'
virgula = [string[0:10:1],string [10:20:1],string [20:30:1], string[30:40:1]]
ponto = f"'{virgula[0]}.{virgula[1]}.{virgula[2]}.{virgula[3]}'"
#print(ponto)
#resolução
string = '01234567890123456789012345678901234567890123456789'
n = 10
lista = [string[i:i + n] for i in range (0, len(string), n)]
retorno = ','.join(lista)
print(lista)
print(retorno)
