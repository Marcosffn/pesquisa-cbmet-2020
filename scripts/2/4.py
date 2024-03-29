import pandas as pd
import os

path = "/home/marcos/Python/pesquisa/arquivos/norte/"

bolsao = os.scandir(path)
novo = pd.DataFrame()

for municipios_pasta in bolsao:
    for municipios_arquivos in (os.scandir(municipios_pasta.path)):
        df = pd.read_csv(municipios_arquivos.path, skiprows=8, sep=";")
        x = df[['DATA (YYYY/MM/DD)', 'PRECIPITACÃO TOTAL. HORARIO (mm)']]
        y = x.dropna()
        novo = novo.append(y)

        novo.to_csv(
            "/home/marcos/Python/pesquisa/arquivos/novos/norte.csv", sep=";", index=False)

print(novo)
# dia = list(range(1, 32))
# ano = list(range(2010, 2020))
# jan = []
# fev = []
# mar = []
# abr = []
# mai = []
# jun = []
# jul = []
# ago = []
# set = []
# out = []
# nov = []
# dez = []
# for d in dia:
#     for a in ano:
#         m1 = str(a) + "/" + "01" + "/" + str(d).zfill(2)
#         m2 = str(a) + "/" + "02" + "/" + str(d).zfill(2)
#         m3 = str(a) + "/" + "03" + "/" + str(d).zfill(2)
#         m4 = str(a) + "/" + "04" + "/" + str(d).zfill(2)
#         m5 = str(a) + "/" + "05" + "/" + str(d).zfill(2)
#         m6 = str(a) + "/" + "06" + "/" + str(d).zfill(2)
#         m7 = str(a) + "/" + "07" + "/" + str(d).zfill(2)
#         m8 = str(a) + "/" + "08" + "/" + str(d).zfill(2)
#         m9 = str(a) + "/" + "09" + "/" + str(d).zfill(2)
#         m10 = str(a) + "/" + "10" + "/" + str(d).zfill(2)
#         m11 = str(a) + "/" + "11" + "/" + str(d).zfill(2)
#         m12 = str(a) + "/" + "12" + "/" + str(d).zfill(2)
#         jan.append(m1)
#         fev.append(m2)
#         mar.append(m3)
#         abr.append(m4)
#         mai.append(m5)
#         jun.append(m6)
#         jul.append(m7)
#         ago.append(m8)
#         set.append(m9)
#         out.append(m10)
#         nov.append(m11)
#         dez.append(m12)
#
# print(y["DATA (YYYY/MM/DD)" == m1[:]])
