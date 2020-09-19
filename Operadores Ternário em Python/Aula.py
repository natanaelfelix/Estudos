"""
Operador ternário em python

logged_user = True
if logged_user:
    msg = "Usuário Logado"
else:
    msg = "Usuário precisa logar"
print(msg)
"""

logged_user = False
msg = "Usuário Logado" if( logged_user ==True) else "Usuário precisa logar"
#é desse jeito que se usa operador ternário em py
print(msg)
