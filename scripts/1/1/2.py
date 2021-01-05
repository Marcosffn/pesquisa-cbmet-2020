import os

paths = "/home/marcos/Python/pesquisa/arquivos/ms/normal"

scan = os.scandir(paths)

for file in scan:
    with open(file.path, "r") as arquivo:
        for line in arquivo:
            linhas = line.split("\n")
            for elemento in linhas:
                a = elemento.split(";")
                with open("/home/marcos/Python/pesquisa/arquivos/ms_novo/normal/teste.csv", "w") as teste:
                    teste.write(a)
