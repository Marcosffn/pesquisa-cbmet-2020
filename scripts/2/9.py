import oito as oi
import pandas as pd
import numpy as np
import os
import random as rnd
import matplotlib.pyplot as plt


medias = []
meses = []
for m in range(1, 13):
    media = oi.PrecipMediaMes(
        '/home/marcos/Python/pesquisa/somas_tudo/campo_grande.csv', m)
    mes = oi.ColocarMes(m)
    medias.append(media)
    meses.append(mes)

cor = rnd.choice(['b', 'r', 'g', 'c', 'm', 'y', 'brown', 'gray', 'tan',
                  'black', '#ff5733', '#0000ff', '#808000', '#cd5c5c',
                  '#daf7a6', '#9b59b6', '#f5b041', '#00ff00'
                  ])
plt.bar(list(range(1, 13)), medias, color=cor)
plt.ylabel("Precipitação média em mm")
plt.xlabel('Mês')
plt.title("Campo Grande")
plt.style.use("ggplot")
plt.savefig('/home/marcos/Python/pesquisa/medias/campo_grande.png')
