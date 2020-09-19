carrinho = []

carrinho.append(('Produto 1 ', 30.))
carrinho.append(('Produto 2 ', 30))
carrinho.append(('Produto 3 ', 40))

resu = sum([ float(x) for  y, x in carrinho])
print(resu)
