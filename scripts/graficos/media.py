import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def mes(mes, arquivo):
    return arquivo.loc[arquivo["MES"] == mes]


def preciAnoMes(m, a, arq):
    arquivo = mes(m, arq)
    return arquivo.loc[arquivo["ANO"] == a]["PRECIPITACAO TOTAL"]


def mediaMesesAno(mes, ano, arquivos):
    """
    Retorna a média entre todas as regiões de um certo ano
    """
    valores = []
    for i in arquivos:
        preci = preciAnoMes(mes, ano, i)
        preci = preci.values[0]
        valores.append(preci)

    return np.mean(valores)


years = list(range(2010, 2020))
meses = list(range(1, 13))

bolsao = pd.read_csv(
    "/home/marcos/Python/pesquisa/somas_tudo/bolsao.csv", sep=";"
)


campo_grande = pd.read_csv(
    "/home/marcos/Python/pesquisa/somas_tudo/campo_grande.csv", sep=";"
)


grande_dourados = pd.read_csv(
    "/home/marcos/Python/pesquisa/somas_tudo/grande_dourados.csv", sep=";"
)


leste = pd.read_csv(
    "/home/marcos/Python/pesquisa/somas_tudo/leste.csv", sep=";"
)


norte = pd.read_csv(
    "/home/marcos/Python/pesquisa/somas_tudo/norte.csv", sep=";"
)


pantanal = pd.read_csv(
    "/home/marcos/Python/pesquisa/somas_tudo/pantanal.csv", sep=";"
)


regiao_cone_sul = pd.read_csv(
    "/home/marcos/Python/pesquisa/somas_tudo/regiao_cone_sul.csv", sep=";"
)


sudoeste = pd.read_csv(
    "/home/marcos/Python/pesquisa/somas_tudo/sudoeste.csv", sep=";"
)


sul_fronteira = pd.read_csv(
    "/home/marcos/Python/pesquisa/somas_tudo/sul_fronteira.csv", sep=";"
)

media_janeiro = []
media_fevereiro = []
media_marco = []
media_abril = []
media_maio = []
media_junho = []
media_julho = []
media_agosto = []
media_setembro = []
media_outubro = []
media_novembro = []
media_dezembro = []


for y in years:
    for m in meses:
        x = mediaMesesAno(
            m,
            y,
            [
                bolsao,
                campo_grande,
                grande_dourados,
                leste,
                norte,
                pantanal,
                regiao_cone_sul,
                sudoeste,
                sul_fronteira,
            ],
        )
        if m == 1:
            media_janeiro.append(x)
        elif m == 2:
            media_fevereiro.append(x)
        elif m == 3:
            media_marco.append(x)
        elif m == 4:
            media_abril.append(x)
        elif m == 5:
            media_maio.append(x)
        elif m == 6:
            media_junho.append(x)
        elif m == 7:
            media_julho.append(x)
        elif m == 8:
            media_agosto.append(x)
        elif m == 9:
            media_setembro.append(x)
        elif m == 10:
            media_outubro.append(x)
        elif m == 11:
            media_novembro.append(x)
        elif m == 12:
            media_dezembro.append(x)

plt.scatter(years, media_janeiro, c="black", label="Janeiro")
plt.plot(years, media_janeiro, c="black")

plt.scatter(years, media_fevereiro, c="gray", label="Fevereiro")
plt.plot(years, media_fevereiro, c="gray")

plt.scatter(years, media_marco, c="lightcoral", label="Março")
plt.plot(years, media_marco, c="lightcoral")

plt.scatter(years, media_abril, c="brown", label="Abril")
plt.plot(years, media_abril, c="brown")

plt.scatter(years, media_maio, c="darkred", label="Maio")
plt.plot(years, media_maio, c="darkred")

plt.scatter(years, media_junho, c="red", label="Junho")
plt.plot(years, media_junho, c="red")

plt.scatter(years, media_julho, c="orangered", label="Julho")
plt.plot(years, media_julho, c="orangered")

plt.scatter(years, media_agosto, c="sienna", label="Agosto")
plt.plot(years, media_agosto, c="sienna")

plt.scatter(years, media_setembro, c="orange", label="Setembro")
plt.plot(years, media_setembro, c="orange")

plt.scatter(years, media_outubro, c="gold", label="Outubro")
plt.plot(years, media_outubro, c="gold")

plt.scatter(years, media_novembro, c="olive", label="Novembro")
plt.plot(years, media_novembro, c="olive")

plt.scatter(years, media_dezembro, c="green", label="Dezembro")
plt.plot(years, media_dezembro, c="green")


plt.legend(bbox_to_anchor=(1.001, 1))
plt.xlabel("Ano")
plt.ylabel("Precipitação total em milímetros (mm)")
plt.title(
    "Média da precipitação total por mês das regiões do estado de MS de 2010 a 2019"
)
plt.show()
