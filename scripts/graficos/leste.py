import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

leste = pd.read_csv(
    "/home/marcos/Python/pesquisa/somas_tudo/leste.csv", sep=";"
)

years = list(range(2010, 2020))

janeiro = leste.loc[leste["MES"] == 1]
janeiro = janeiro.sort_values("ANO")

fevereiro = leste.loc[leste["MES"] == 2]
fevereiro = fevereiro.sort_values("ANO")

março = leste.loc[leste["MES"] == 3]
março = março.sort_values("ANO")

abril = leste.loc[leste["MES"] == 4]
abril = abril.sort_values("ANO")

maio = leste.loc[leste["MES"] == 5]
maio = maio.sort_values("ANO")

junho = leste.loc[leste["MES"] == 6]
junho = junho.sort_values("ANO")

julho = leste.loc[leste["MES"] == 7]
julho = julho.sort_values("ANO")

agosto = leste.loc[leste["MES"] == 8]
agosto = agosto.sort_values("ANO")

setembro = leste.loc[leste["MES"] == 9]
setembro = setembro.sort_values("ANO")

outubro = leste.loc[leste["MES"] == 10]
outubro = outubro.sort_values("ANO")

novembro = leste.loc[leste["MES"] == 11]
novembro = novembro.sort_values("ANO")

dezembro = leste.loc[leste["MES"] == 12]
dezembro = dezembro.sort_values("ANO")


plt.scatter(years, janeiro["PRECIPITACAO TOTAL"], c="black", label="Janeiro")
plt.plot(years, janeiro["PRECIPITACAO TOTAL"], c="black")


plt.scatter(
    years, fevereiro["PRECIPITACAO TOTAL"], c="gray", label="Fevereiro"
)
plt.plot(years, fevereiro["PRECIPITACAO TOTAL"], c="gray")


plt.scatter(years, março["PRECIPITACAO TOTAL"], c="lightcoral", label="Março")
plt.plot(years, março["PRECIPITACAO TOTAL"], c="lightcoral")


plt.scatter(years, abril["PRECIPITACAO TOTAL"], c="brown", label="Abril")
plt.plot(years, abril["PRECIPITACAO TOTAL"], c="brown")


plt.scatter(years, maio["PRECIPITACAO TOTAL"], c="darkred", label="Maio")
plt.plot(years, maio["PRECIPITACAO TOTAL"], c="darkred")


plt.scatter(years, junho["PRECIPITACAO TOTAL"], c="red", label="Junho")
plt.plot(years, junho["PRECIPITACAO TOTAL"], c="red")


plt.scatter(years, julho["PRECIPITACAO TOTAL"], c="orangered", label="Julho")
plt.plot(years, julho["PRECIPITACAO TOTAL"], c="orangered")


plt.scatter(years, agosto["PRECIPITACAO TOTAL"], c="sienna", label="Agosto")
plt.plot(years, agosto["PRECIPITACAO TOTAL"], c="sienna")


plt.scatter(
    years, setembro["PRECIPITACAO TOTAL"], c="orange", label="Setembro"
)
plt.plot(years, setembro["PRECIPITACAO TOTAL"], c="orange")


plt.scatter(years, outubro["PRECIPITACAO TOTAL"], c="gold", label="Outubro")
plt.plot(years, outubro["PRECIPITACAO TOTAL"], c="gold")


plt.scatter(years, novembro["PRECIPITACAO TOTAL"], c="olive", label="Novembro")
plt.plot(years, novembro["PRECIPITACAO TOTAL"], c="olive")


plt.scatter(years, dezembro["PRECIPITACAO TOTAL"], c="green", label="Dezembro")
plt.plot(years, dezembro["PRECIPITACAO TOTAL"], c="green")


plt.legend(bbox_to_anchor=(1.001, 1))
plt.xlabel("Ano")
plt.ylabel("Precipitação total em milímetros (mm)")
plt.title("Precipitação total por mês da região do Leste de 2010 a 2019")
plt.show()
