import pandas as pd
from numpy import mean


def read_write(path, valor):
    arquivo = open(path, "w")
    arquivo.write(str(valor))
    arquivo.close()


# def separar(dataf, inicio, fim, ano):
    # dataf = dataf[:][inicio:fim]
    # for index, row in dataf.iterrows():
    #     if row['ANO'] == ano:
    #         if row['MES'] == 1:
    #             jan.append(row['PRECIPITACÃO TOTAL. HORARIO (mm)'])
    #         if row['MES'] == 2:
    #             fev.append(row['PRECIPITACÃO TOTAL. HORARIO (mm)'])
    #         if row['MES'] == 3:
    #             mar.append(row['PRECIPITACÃO TOTAL. HORARIO (mm)'])
    #         if row['MES'] == 4:
    #             abr.append(row['PRECIPITACÃO TOTAL. HORARIO (mm)'])
    #         if row['MES'] == 5:
    #             mai.append(row['PRECIPITACÃO TOTAL. HORARIO (mm)'])
    #         if row['MES'] == 6:
    #             jun.append(row['PRECIPITACÃO TOTAL. HORARIO (mm)'])
    #         if row['MES'] == 7:
    #             jul.append(row['PRECIPITACÃO TOTAL. HORARIO (mm)'])
    #         if row['MES'] == 8:
    #             ago.append(row['PRECIPITACÃO TOTAL. HORARIO (mm)'])
    #         if row['MES'] == 9:
    #             set.append(row['PRECIPITACÃO TOTAL. HORARIO (mm)'])
    #         if row['MES'] == 10:
    #             out.append(row['PRECIPITACÃO TOTAL. HORARIO (mm)'])
    #         if row['MES'] == 11:
    #             nov.append(row['PRECIPITACÃO TOTAL. HORARIO (mm)'])
    #         if row['MES'] == 12:
    #             dez.append(row['PRECIPITACÃO TOTAL. HORARIO (mm)'])


def escrever(ano):
    for i in range(1, 13):
        if i == 1:
            read_write("/home/marcos/Python/pesquisa/somas/sul_fronteira/sul_fronteira_somas" +
                       str(i)+ano+".csv", sum(jan))
        if i == 2:
            read_write("/home/marcos/Python/pesquisa/somas/sul_fronteira/sul_fronteira_somas" +
                       str(i)+ano+".csv", sum(fev))
        if i == 3:
            read_write("/home/marcos/Python/pesquisa/somas/sul_fronteira/sul_fronteira_somas" +
                       str(i)+ano+".csv", sum(mar))
        if i == 4:
            read_write("/home/marcos/Python/pesquisa/somas/sul_fronteira/sul_fronteira_somas" +
                       str(i)+ano+".csv", sum(abr))
        if i == 5:
            read_write("/home/marcos/Python/pesquisa/somas/sul_fronteira/sul_fronteira_somas" +
                       str(i)+ano+".csv", sum(mai))
        if i == 6:
            read_write("/home/marcos/Python/pesquisa/somas/sul_fronteira/sul_fronteira_somas" +
                       str(i)+ano+".csv", sum(jun))
        if i == 7:
            read_write("/home/marcos/Python/pesquisa/somas/sul_fronteira/sul_fronteira_somas" +
                       str(i)+ano+".csv", sum(jul))
        if i == 8:
            read_write("/home/marcos/Python/pesquisa/somas/sul_fronteira/sul_fronteira_somas" +
                       str(i)+ano+".csv", sum(ago))
        if i == 9:
            read_write("/home/marcos/Python/pesquisa/somas/sul_fronteira/sul_fronteira_somas" +
                       str(i)+ano+".csv", sum(set))
        if i == 10:
            read_write("/home/marcos/Python/pesquisa/somas/sul_fronteira/sul_fronteira_somas" +
                       str(i)+ano+".csv", sum(out))
        if i == 11:
            read_write("/home/marcos/Python/pesquisa/somas/sul_fronteira/sul_fronteira_somas" +
                       str(i)+ano+".csv", sum(nov))
        if i == 12:
            read_write("/home/marcos/Python/pesquisa/somas/sul_fronteira/sul_fronteira_somas" +
                       str(i)+ano+".csv", sum(dez))


def limpar():
    jan.clear()
    fev.clear()
    mar.clear()
    abr.clear()
    mai.clear()
    jun.clear()
    jul.clear()
    ago.clear()
    set.clear()
    out.clear()
    nov.clear()
    dez.clear()


jan = []
fev = []
mar = []
abr = []
mai = []
jun = []
jul = []
ago = []
set = []
out = []
nov = []
dez = []

arquivo_path = "/home/marcos/Python/pesquisa/arquivos/novos/sul_fronteira.csv"

df = pd.read_csv(arquivo_path, sep=";")

for ano in range(2010, 2020):
    # separar(df, 0, 89211, ano)
    # separar(df, 89211, 178422, ano)
    # separar(df, 178422, 267633, ano)
    escrever(str(ano))
    limpar()
