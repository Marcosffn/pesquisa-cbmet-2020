import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sul_fronteira = pd.read_csv(
    "/home/marcos/Python/pesquisa/somas_tudo/sul_fronteira.csv", sep=";"
)

years = list(range(2010, 2020))

janeiro = sul_fronteira.loc[sul_fronteira["MES"] == 1]
janeiro.loc[janeiro["ANO"] == 2010]["PRECIPITACAO TOTAL"]
janeiro = janeiro.sort_values("ANO")

fevereiro = sul_fronteira.loc[sul_fronteira["MES"] == 2]
fevereiro = fevereiro.sort_values("ANO")

março = sul_fronteira.loc[sul_fronteira["MES"] == 3]
março = março.sort_values("ANO")

abril = sul_fronteira.loc[sul_fronteira["MES"] == 4]
abril = abril.sort_values("ANO")

maio = sul_fronteira.loc[sul_fronteira["MES"] == 5]
maio = maio.sort_values("ANO")

junho = sul_fronteira.loc[sul_fronteira["MES"] == 6]
junho = junho.sort_values("ANO")

julho = sul_fronteira.loc[sul_fronteira["MES"] == 7]
julho = julho.sort_values("ANO")

agosto = sul_fronteira.loc[sul_fronteira["MES"] == 8]
agosto = agosto.sort_values("ANO")

setembro = sul_fronteira.loc[sul_fronteira["MES"] == 9]
setembro = setembro.sort_values("ANO")

outubro = sul_fronteira.loc[sul_fronteira["MES"] == 10]
outubro = outubro.sort_values("ANO")

novembro = sul_fronteira.loc[sul_fronteira["MES"] == 11]
novembro = novembro.sort_values("ANO")

dezembro = sul_fronteira.loc[sul_fronteira["MES"] == 12]
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
plt.title("Precipitação total por mês da região Sul-Fronteira de 2010 a 2019")
plt.show()
