import pandas as pd


bolsao_path = "/home/marcos/Python/pesquisa/arquivos/novos/bolsao.csv"


bolsao = pd.read_csv(bolsao_path, sep=";")

bolsao = bolsao.sort_values(by=['DATA (YYYY/MM/DD)'])

bolsao = bolsao[:][103963:207926]

jan_valores = []

for index, row in bolsao.iterrows():
    for i in jan:
        if row['DATA (YYYY/MM/DD)'] == i:
            jan_valores.append(row['PRECIPITACÃO TOTAL. HORARIO (mm)'])


with open("/home/marcos/Python/pesquisa/somas/bolsao/2010_jan14.csv", "r+") as media:
    d = int(media.read())
    d += sum(jan_valores)
    media.write(str(d))
    # media.write(str(sum(jan_valores)))
