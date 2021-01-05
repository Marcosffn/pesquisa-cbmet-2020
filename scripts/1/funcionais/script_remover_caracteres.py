import os
import pandas as pd
import numpy as np
import fileinput as fi

path = "/home/marcos/Python/pesquisa/arquivos"

arquivos = os.scandir(path)

for regioes in arquivos:
    # regiao = os.scandir(regioes.path)
    print(regioes)
    # for municipios in regiao:
    # for arquivo in municipios:
    # print(municipios)
    # fin = open(arquivo.path, "r")
    # data = fin.read()
    # data = data.replace(',', ".")
    # data = data.replace(",", ".")
    # data = data.replace("REGI�O:", "REGIAO")
    # data = data.replace("PRECIPITAÇÃO", "PRECIPITACAO")
    # data = data.replace("PRESSÃO", "PRESSAO")
    # data = data.replace("°C", "C")
    # data = data.replace("MÍNIMA", "MINIMA")
    # data = data.replace("DIREÇÃO", "DIRECAO")
    # data = data.replace("°", "grau")
    #
    # fin = open(
    #     "/home/marcos/Python/pesquisa/arquivos/ms_novo/ambos/data_hora_preci.csv", "w")
    # fin.write(data)

    # fin.close()
