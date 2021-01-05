import pandas as pd
import os


# def alterar_linha(path, index_linha, nova_linha):
#    with open(path, 'r') as f:
#        texto = f.readlines()
#    with open(path, 'w') as f:
#        for i in texto:
#            if texto.index(i) == index_linha:
#                f.write(nova_linha + '\n')
#            else:
#                f.write(i)


arquivos_path = os.scandir("/home/marcos/Python/pesquisa/arquivos/ms/ambos")

j = pd.DataFrame()

for arquivo in arquivos_path:
    # df = pd.read_csv(arquivo.path, skiprows=8, sep=";", names=['DATA (YYYY/MM/DD)', 'HORA (UTC)', 'PRECIPITACAO TOTAL, HORARIO (mm)',
    # 'PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA (mB)',
    # 'PRESSAO ATMOSFERICA MAX.NA HORA ANT. (AUT) (mB)',
    # 'PRESSAO ATMOSFERICA MIN. NA HORA ANT. (AUT) (mB)',
    # 'RADIACAO GLOBAL (W/m2)', 'TEMPERATURA DO AR / BULBO SECO, HORARIA (C)',
    # 'TEMPERATURA DO PONTO DE ORVALHO (C)',
    # 'TEMPERATURA MAXIMA NA HORA ANT. (AUT) (C)',
    # 'TEMPERATURA MINIMA NA HORA ANT. (AUT) (C)',
    # 'TEMPERATURA ORVALHO MAX. NA HORA ANT. (AUT) (C)',
    # 'TEMPERATURA ORVALHO MIN. NA HORA ANT. (AUT) (C)',
    # 'UMIDADE REL. MAX. NA HORA ANT. (AUT) (%)',
    # 'UMIDADE REL. MIN. NA HORA ANT. (AUT) (%)',
    # 'UMIDADE RELATIVA DO AR, HORARIA (%)',
    # 'VENTO, DIRECAO HORARIA (gr) (grau (gr))', 'VENTO, RAJADA MAXIMA (m/s)',
    # 'VENTO, VELOCIDADE HORARIA (m/s)', 'Unnamed: 19'])
    # df.drop(['PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA (mB)',
    # 'PRESSAO ATMOSFERICA MAX.NA HORA ANT. (AUT) (mB)',
    # 'PRESSAO ATMOSFERICA MIN. NA HORA ANT. (AUT) (mB)',
    # 'RADIACAO GLOBAL (W/m2)', 'TEMPERATURA DO AR / BULBO SECO, HORARIA (C)',
    # 'TEMPERATURA DO PONTO DE ORVALHO (C)',
    # 'TEMPERATURA MAXIMA NA HORA ANT. (AUT) (C)',
    # 'TEMPERATURA MINIMA NA HORA ANT. (AUT) (C)',
    # 'TEMPERATURA ORVALHO MAX. NA HORA ANT. (AUT) (C)',
    # 'TEMPERATURA ORVALHO MIN. NA HORA ANT. (AUT) (C)',
    # 'UMIDADE REL. MAX. NA HORA ANT. (AUT) (%)',
    # 'UMIDADE REL. MIN. NA HORA ANT. (AUT) (%)',
    # 'UMIDADE RELATIVA DO AR, HORARIA (%)',
    # 'VENTO, DIRECAO HORARIA (gr) (grau (gr))', 'VENTO, RAJADA MAXIMA (m/s)',
    # 'VENTO, VELOCIDADE HORARIA (m/s)', 'Unnamed: 19'], inplace=True, axis=1)

    j = j.append(df)


j.to_csv("/home/marcos/Python/pesquisa/arquivos/ms_novo/ambos/data_hora_preci.csv", index=False)


print(j)
print(df.columns)
