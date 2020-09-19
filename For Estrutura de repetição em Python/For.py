"""

For in em python
Iterando strings com for
Funçã o range(start=0, stop, step =1)

Utilizado para coisas finitas

For não tem contador, mas podemos incrementar um contador com #Enumerate que enumera cada volta do laço

"""

texto = "python"

for n, letra in enumerate(texto):
    print(n, letra)

#Range
#Funçã o range   (start=0, stop, step =1)
#for numero in range (0, (começa)   10, (termina)    1 (de quanto em quanto em pula)    ):
for numero in range (10):
    print(numero)

#Não depende do laço for e o for não depende do range, porem podemos utilizar juntos
