import pandas as pd
import numpy as np
import os
import random as rnd
import matplotlib.pyplot as plt


def PrecipMediaMes(caminho, mes, sep=";"):
    arq = pd.read_csv(caminho, sep=sep)
    x = arq.loc[arq['MES'] == mes]
    return np.mean(x['PRECIPITACAO TOTAL'])


def ColocarMes(m):
    if m == 1:
        return "Janeiro"
    elif m == 2:
        return "Fevereiro"
    elif m == 3:
        return "Março"
    elif m == 4:
        return "Abril"
    elif m == 5:
        return "Maio"
    elif m == 6:
        return "Junho"
    elif m == 7:
        return "Julho"
    elif m == 8:
        return "Agosto"
    elif m == 9:
        return "Setembro"
    elif m == 10:
        return "Outubro"
    elif m == 11:
        return "Novembro"
    elif m == 12:
        return "Dezembro"


arquivos = os.scandir("/home/marcos/Python/pesquisa/somas_tudo")

for arquivo in arquivos:
    medias = []
    meses = []
    for mes in range(1, 13):
        media = PrecipMediaMes(
            '/home/marcos/Python/pesquisa/somas_tudo/campo_grande.csv', mes)
        m = ColocarMes(mes)
        medias.append(media)
        meses.append(m)

    nome = arquivo.name.replace('.csv', '')
    path = "/home/marcos/Python/pesquisa/medias/" + nome + '.png'
    titulo = (str(nome[0]).upper() + str(nome[1:])).replace("_", ' ').replace('Bolsao', 'Bolsão').replace('grande',
                                                                                                          'Grande').replace('dourados', 'Dourados').replace('Regiao cone sul', 'Região Cone Sul').replace('fronteira', 'Fronteira')
    cor = rnd.choice(['b', 'r', 'g', 'c', 'm', 'y', 'brown', 'gray', 'tan',
                      'black', '#ff5733', '#0000ff', '#808000', '#cd5c5c',
                      '#daf7a6', '#9b59b6', '#f5b041', '#00ff00'
                      ])
    plt.bar(meses, medias, color=cor)
    plt.ylabel("Precipitação média em mm")
    plt.xlabel('Mês')
    plt.title(titulo)
    plt.style.use("seaborn")
    plt.savefig(path)
    plt.clf()
    medias.clear()
    meses.clear()
