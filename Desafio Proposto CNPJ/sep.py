def separador(cnpj):
    import re
    cnpj_seprado = re.sub(r'[^0-9]', "", cnpj)
    return cnpj_seprado
