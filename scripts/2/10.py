import oito as oi
import pandas as pd
import os
import matplotlib.pyplot as plt

bolsao = []
campo_grande = []
grande_dourados = []
leste = []
norte = []
pantanal = []
regiao_cone_sul = []
sudoeste = []
sul_fronteira = []

arquivos = os.scandir(r'/home/marcos/Python/pesquisa/somas_tudo')

for arquivo in arquivos:
    for mes in range(1, 13):
        media = oi.PrecipMediaMes(arquivo.path, mes)
        if arquivo.name.replace('.csv', '') == 'bolsao':
            bolsao.append(media)
        if arquivo.name.replace('.csv', '') == 'campo_grande':
            campo_grande.append(media)
        if arquivo.name.replace('.csv', '') == 'grande_dourados':
            grande_dourados.append(media)
        if arquivo.name.replace('.csv', '') == 'leste':
            leste.append(media)
        if arquivo.name.replace('.csv', '') == 'norte':
            norte.append(media)
        if arquivo.name.replace('.csv', '') == 'pantanal':
            pantanal.append(media)
        if arquivo.name.replace('.csv', '') == 'regiao_cone_sul':
            regiao_cone_sul.append(media)
        if arquivo.name.replace('.csv', '') == 'sudoeste':
            sudoeste.append(media)
        if arquivo.name.replace('.csv', '') == 'sul_fronteira':
            sul_fronteira.append(media)

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto',
         'Setembro', 'Outubro', 'Novembro', 'Dezembro']
plt.legend(['Bolsão'])
plt.scatter(y=bolsao, x=meses, label="Bolsão")
plt.scatter(y=campo_grande, x=meses, label='Campo Grande')
plt.scatter(y=grande_dourados, x=meses, label='Grande Dourados')
plt.scatter(y=leste, x=meses, label='Leste')
plt.scatter(y=norte, x=meses, label='Norte')
plt.scatter(y=pantanal, x=meses, label='Pantanal')
plt.scatter(y=regiao_cone_sul, x=meses, label='Regão do cone do Sul')
plt.scatter(y=sudoeste, x=meses)
plt.scatter(y=sul_fronteira, x=meses)
plt.plot(meses, bolsao, '--', label="Bolsão")
plt.plot(meses, campo_grande, '--')
plt.plot(meses, grande_dourados, '--')
plt.plot(meses, leste, '--')
plt.plot(meses, norte, '--')
plt.plot(meses, pantanal, '--')
plt.plot(meses, regiao_cone_sul, '--')
plt.plot(meses, sudoeste, '--')
plt.plot(meses, sul_fronteira, '--')
plt.title("Preciptação média em cada região do estado do Mato Grosso do Sul")
plt.show()
