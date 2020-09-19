while True:
    cpf = input(str("Digite o cpf, com os pontos e traços:"))
    primarynumber = cpf[0:11:1]
    secondarynumber = cpf[12:14:1]
    contador = 11
    soma = 0
    for n in primarynumber:
        if n.isdigit():
            n = int(n)
            contador = contador -1
            mult = n * contador
            soma = soma + mult
    novocpf= []
    conta = (11 - (soma % 11))
    if conta > 9:
        digito = '0'
        novocp = (primarynumber.replace(".", "") + digito)
        novocpf.append(novocp)
    elif conta <=9:
        digito = str (conta)
        novocp = primarynumber.replace(".", "") + digito
        novocpf.append(novocp)
    lista_string = novocpf[0]
    novocpf_2=[]
    vetnewcpf=[]
    contador = 12
    soma_2 = 0
    for n in lista_string:
        if n.isdigit():
            n = int(n)
            contador = contador -1
            mult = n * contador
            soma_2 = soma_2 + mult
    conta = (11 - (soma_2 % 11))
    if conta > 9:
        digito = '0'
        lista_stringnew = lista_string + digito
        vetnewcpf.append(lista_stringnew)
    elif conta <=9:
        digito = str(conta)
        lista_stringnew = lista_string + digito
        vetnewcpf.append(lista_stringnew)

    antigocpf = []
    concatenar = primarynumber.replace(".", "")
    concatenarofim = concatenar + secondarynumber
    antigocpf.append(concatenarofim)

    stringlistacpfat = antigocpf[0]
    stringlistacpfnw = vetnewcpf[0]

    if stringlistacpfat == stringlistacpfnw:
        print('CPF VÁLIDO!')
    else:
        print('CPF INVALIDO!')



