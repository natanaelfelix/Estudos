def convert_numero (valor):
    try:
        valor = int (valor)
        return valor
    except ValueError as erro:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass

numero = convert_numero((input('Digite um numero:')))
print(numero * 5)
