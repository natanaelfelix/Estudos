"""
numeros = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

progressivo = -1
inverso = numeros[-1]
inverso_2 = 0
for num in numeros:
    progressivo = progressivo + 1
    inverso_2 = inverso - progressivo
    print(progressivo, inverso_2)


for p , r in enumerate(range (10, 1, -1)):
    print (p, r)
    """
for  r in range (5, 0, -1):
    print ( r)
l2 = (x for x in range (5, 0, -1))
prox = int((hasattr(l2, '__next__')))
print (prox)
