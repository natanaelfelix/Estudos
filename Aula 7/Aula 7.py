nome = "Natanael"
idade = 23
altura = 1.80
e_maior = idade >18
peso = 96
imc = peso / altura **2
print(nome, 'tem', idade, 'anos de idade e seu imc é:', imc)
#utilizando f string para evitar usar virgulas
print (f"{nome} tem {idade} anos de idade e seu imc é: {imc:.2f}")
#para exibir apenas 2 casas decimais {imc:.2f}")
print ("{} tem {} anos de idade e seu imc é: {}".format(nome, idade, imc)) #utilizando o .format
