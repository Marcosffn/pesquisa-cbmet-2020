import pandas as pd
import numpy as np
import os


def NomeArquivo(r: str, m):
    lis = []
    n = r + '_somas'
    for i in range(1, 13):
        for x in range(2010, 2020):
            if i == m:
                lis.append(n + str(i) + str(x) + ".csv")
    return lis


def abrir(caminho):
    abre = open(caminho, "r")
    cont = abre.readline()
    return cont
    abre.close()


def LerArq(arq, r, m, a):
    valor = abrir(arq.path)
    novo = [r, str(m).zfill(2), str(a), valor]
    return novo


def AdicDataf(df, v):
    if len(df) == 0:
        df.loc[0] = v
    else:
        df.loc[len(df)] = v


def Ano(n, mes, reg):
    nom = reg + '_somas'
    for a in range(2010, 2020):
        if n == (nom + str(mes) + str(a) + ".csv"):
            return a


def AbrirCsvDataf(pasta_caminho, regiao, mes):
    data = pd.DataFrame(columns=['REGIAO', 'ANO', 'MES', 'PRECIPITACAO TOTAL'])
    arquivos = os.scandir(pasta_caminho)
    nomes = NomeArquivo(regiao, mes)
    for arquivo in arquivos:
        for nome in nomes:
            if arquivo.name == nome:
                ano = Ano(nome, mes, regiao)
                val = LerArq(arquivo, regiao, ano, mes)
                AdicDataf(data, val)
    return data


data = pd.DataFrame(columns=['REGIAO', 'MES', 'ANO', 'PRECIPITACAO TOTAL'])

regioes = ['pantanal', 'regiao_cone_sul', 'sul_fronteira', 'sudoeste']

for regiao in regioes:
    for mes in range(1, 13):
        path = "/home/marcos/Python/pesquisa/somas/" + regiao
        df = AbrirCsvDataf(path, regiao, mes)
        data = data.append(df)
    nome = "/home/marcos/Python/pesquisa/somas_tudo/" + regiao + ".csv"
    data.to_csv(nome, sep=";", index=False)
    data = data.drop(data.index)
