#excessões são erros que ocorrer no python, que faz parar o  funcionámento do condigo

try: #vai tentar executar o codigo, é como se fosse if e else
    print('a')
except: # caso o codigo acima der erro, entra na excessão
    print('erro')
#podemos criar um filtro para quando der esse erro, como se fosse um report

try: #vai tentar executar o codigo, é como se fosse if e else
    print('a')
except NameError as erro: # caso o codigo acima der erro, entra na excessão
    print('erro', erro) #mostra exatamente onde está o erro
except Exception as erro: # pega qualquer tipo de erro que não sabemos o tipo
    print('ocorreu um erro inexperado')
else: # vai ser executado sempre que o try der certo
    print('Seu codigo foi executado com sucesso, caso contrário ele não executa')
finally:#sempre executada, se ocorreu ou não o erro, sempre executado
    print("boraa")

print("o codigo não para por conta do erro, nesse caso continua")
