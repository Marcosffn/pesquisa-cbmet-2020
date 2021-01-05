import os
import pandas as pd

caminho = "/home/marcos/Python/pesquisa/arquivos/arquivos_teste"

arquivos = os.scandir(caminho)

for csv in arquivos:
    a = pd.read_csv(csv.path, sep=";", header=8,)
