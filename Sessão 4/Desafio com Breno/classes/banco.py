class Banco:
    def __init__(self, conta, cliente):
        self.conta = conta
        self.cliente = cliente
        c = []
        cl = []

        c.append(self.conta)
        cl.append(self.cliente)

        return


    def autenticacao (self, cliente, conta, agencia):
        if cliente not in self.cliente :
            print('Esse cliente não faz parte do banco')
            return

        if conta not in self.conta and agencia not in self.agencia:
            print('Esse cliente não faz parte do banco')
            return




