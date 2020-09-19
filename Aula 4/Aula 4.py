#Tipos de dados
#str = string - ('Assim' ou "Assim"
#int = inteiro - 123456 0 -10 -20 -50 (positivos ou negativos)
#float = real/ponto flutante - 10 10.50 1.5 -10.10 (valores com ponto)
#bool = booleano/lógico - True/false 10 == 10

print('Luiz', type('Luiz')) #Mostra o tipo primitivo de dado
print('10', type(10))
print("10.50", type(10.50))
print(10 ==10, type(10 == 10))
print('L' == 'L', type('L' == 'L'))
#Convertendo para outro tipo primitivo no caso o boleano
print('Luiz', type('Luiz'), bool('Luiz'))
#Convertendo para outro tipo primitivo no caso o int, chama-se caching
print('10', type('10'), type(int('10')))
