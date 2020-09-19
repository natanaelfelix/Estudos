from pessoas import Pessoa
#p1 = Pessoa() #instanciando, criando um objeto a partir de uma classe, estamos utilizando um monlde para criar uma pessoa
#p2 = Pessoa()

#p1.nome = ('Luiz', 29) #ESSAS VARIÁVEIS DE INSTANCIAS, CRIADAS EM CADA OBJETO SÃO OS ATRIBUTOS DA CLASSE, NESSE CASO CRIANDO UM ATRIBUTO DA PESSOA 1
#p2.nome = ('João', 40)
# p1.falar(p1), na teoria funcionário assim
#p1.falar() # estou chamando a classe e o metodo que eu quero da classe

p1 = Pessoa ('Luiz', 24) # essas variáveis foram para dentro da classe eu só passa os valores como argumento, ou seja todas as instancias terão o q tiver na classe como parâmetro
p2 = Pessoa ('Fernando', 29)
"""
p1.comer('Maçã')
#p1.falar('oi')
p1.parar_comer()
p1.parar_comer()
p1.falar('oi')
p1.comer('Maçã')
p1.parar_comer()
p1.falar('oi')
p1.parar_falar()
p1.falar('mudou')
"""
p1.falar('Olá')
p2.falar('Bom Dia')
print(p1.get_ano_nacimento())
