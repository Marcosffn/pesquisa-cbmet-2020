import pandas as pd
import os

path = "/home/marcos/Python/pesquisa/arquivos"

pastas_regioes = os.scandir(path)

for regiao in pastas_regioes:
    new_path = regiao.path
    new_arquivos = os.scandir(new_path)
    for pastas_cidade in new_arquivos:
        arquivos_path = os.scandir(pastas_cidade.path)
        for arquivo in arquivos_path:  # aqui eu consigo dar open() nos arquivos
            pass
