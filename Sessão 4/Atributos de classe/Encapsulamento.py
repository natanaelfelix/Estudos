#esconde codigos em python

'''
public, # metodos e atributos podem ser acesso dentro e fora da class,
protect # atributos que podem ser acesso apenas dentro da classe ou nas filhas da classe
private # atributo ou metodo só está disponível dentro da classe

em python:
isso é chamado de convenção

_ = é o mesmo que é privado, as é um protected mais fraco
__  = é o mesmo que privado, diz que não se deve usar em hipotese nenhuma

para acessar o real do pivado:
(instancia_nomedaclasse__nomedoatributo)

#tudo isso para proteger a aplicação
'''
class BaseDeDados:
    def __init__(self):
        #self.dados = {} # essa é publica, acessada de dentro e fora da classe, caso seja mudado esse valor de variável quebra toda a classe
        #self.__dados = {} #usando o _ na frente do nome ele diz q é privado e não consiguimos utilizar de fora
        self.__dados = {} #usando so dois __ ele não deixa utilizar, se caso utilizarmo sd fora ele cria outro atributo
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)
    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]

bd = BaseDeDados()

bd.inserir_cliente(1, 'Adriano')
bd.inserir_cliente(2, 'Ronaldo')
bd.inserir_cliente(3, 'Priscila')
bd.apaga_cliente(2)
bd.lista_clientes()
print(bd.__dados)
