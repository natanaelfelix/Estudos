num1 = input('Digite um numero inteiro:')
if not num1.isdigit(): #exeplo para fazer verificação antes e depois colocar o else com as outras funções
    num1 = int (num1)
    if num1 % 2 == 0:
       print('O numero digitado é par!')
    else:
        print('O numero digitado é impar!')
else:
    print("Diite um valor válido!")
