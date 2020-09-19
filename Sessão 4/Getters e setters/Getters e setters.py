class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto (self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))
    #é um filtro

    #getter # depois passa por esse
    @property
    def nome(self): # nesse caso o nome tem q ser o mesmo do atributo q queremos trabalhar
        return self._nome #aqui temos q colocar um nome, não precisar se igual ao valor passado

    #setter # passa por esse primeiro
    def nome (self, valor): # aqui esse valor é o valor do atributoq  será pego
        self._nome = valor.replace('A', '@') # aqui o valor será substituido e adicinado ao _nome do property acima, ai é devolvido ao atributo



p1 = Produto('Camiseta', 50)
p1.desconto(10)
print (p1.preco)

p2 = Produto('Caneca', 15)
p2.desconto(10)
print (p2.preco)
