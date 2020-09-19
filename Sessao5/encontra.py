import os

caminho_procura = 'E:\Filmes'
termo_procura = '720'

for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            caminho_completo = os.path.join(raiz,arquivo)
            nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
            tamanh = os.path.getsize(caminho_completo)
            print(nome_arquivo, ext_arquivo)
