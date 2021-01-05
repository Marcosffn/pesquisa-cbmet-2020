import matplotlib.pyplot as plt
from numpy import mean, std

# # Aqui vai ser onde eu vou armazenar os valores direto do arquivo txt
temp_inst: list = []
min_max_temps: list = []

# # Aqui é o contexto em que vou abrir o arquivo
# # o método vai ser read, pois só vou ler e não modificar nada
# # vou usar o laço for para ler linha a linha do arquivo e pegar somente os dados que eu quero
# # o line.split(","), serve para separar em uma variável cada item de cada linha
# # cada valor vai ser adicionado a sua variavel pelo método append
with open("Python Meteorologia\\Manipulando arquivos\\aguas_claras_01_01_20_26_02_20.txt", "r") as arquivo:
    for line in arquivo:
        linhas = line.split(",")
        temp_inst.append(linhas[3])


# # Agora, vou remover a string: "temp_inst" para fazer os cálculos sem problemas
temp_inst.remove("temp_inst")

# # Achar os valores mínimos e máximos de cada 1 dos 178 dias
y = 0
z = 24
x = 0
k = (len(temp_inst) / 24) - 1

while x <= k:
    if x == k:
        z = z + 1
    menor = min(temp_inst[y:z])
    maior = max(temp_inst[y:z])
    min_max_temps.append(menor)
    min_max_temps.append(maior)
    x += 1
    z = z + 24
    y = y + 24

# # agora eu ja tenho a menor temperatura e a maior temperatura de cada dia
# # é preciso somar o primeiro número com o segundo e fazer a média deles
# # com todos as 356 temperaturas
min_max_media: list = []

j = 0
i0 = 0
i1 = 1
while j <= k:
    media = (float(min_max_temps[i0]) + float(min_max_temps[i1])) / 2
    j += 1
    i0 = i0 + 2
    i1 = i1 + 2
    min_max_media.append(media)


# # Agora que eu ja tenho as médias de cada um dos 178 dias é só separá-las cada uma
# # em seu devido mês
janeiro = min_max_media[0:31]
fevereiro = min_max_media[31:60]
março = min_max_media[60:91]
abril = min_max_media[91:121]
maio = min_max_media[121:152]
junho = min_max_media[152:]


# # agora é necessário fazer a média de cada mês
media_janeiro = mean(janeiro)
media_fevereiro = mean(fevereiro)
media_março = mean(março)
media_abril = mean(abril)
media_maio = mean(maio)
media_junho = mean(junho)


# # Agora tem que fazer o gráfico
eixo_y_temperaturas = media_janeiro, media_fevereiro, media_março, media_abril, media_maio, media_junho

eixo_x_meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho")

eixo_x_janeiro = list(range(1, 32))
eixo_x_feveiro = list(range(1, 30))
eixo_x_março = list(range(1, 32))
eixo_x_abril = list(range(1, 31))
eixo_x_maio = list(range(1, 32))
eixo_x_junho = list(range(1, 27))

# # Mas antes vou colocar todas essas listas e variáveis em arquivos separados
with open("min_max_temps.txt", "w") as temps:
    temps.write(str(min_max_temps))

with open("min_max_media.txt", "w") as medias:
    medias.write(str(min_max_media))

with open("media_mes.txt", "w") as media_mes:
    media_mes.write(str(eixo_y_temperaturas))


# # Cálculo desvio padrão
desvio = std(eixo_y_temperaturas)


# # Agora voltando ao gráfico
plt.style.use("ggplot")
plt.plot(eixo_x_junho, junho, color="g")
plt.scatter(eixo_x_junho, junho, color="orange", marker="o")
plt.title("Temperatura instantânea média Junho")
plt.ylabel("Temperatura (°C)")
plt.xlabel("Dias")
plt.ylim(0, 40)
plt.show()
