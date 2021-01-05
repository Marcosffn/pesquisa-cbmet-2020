###########################
#      Autor: Igor        #
###########################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import pathlib
import os
from decimal import Decimal

######################################
#      Criação das listas  2010      #
######################################
###############
#   Janeiro   #
###############

janh11_2010 = []
janh12_2010 = []
janh13_2010 = []
janh14_2010 = []
janh15_2010 = []
janh16_2010 = []
janh17_2010 = []
janh18_2010 = []
janh19_2010 = []
janh20_2010 = []
janh21_2010 = []
janh22_2010 = []
janh23_2010 = []

#################
#   Fevereiro   #
#################

fevh11_2010 = []
fevh12_2010 = []
fevh13_2010 = []
fevh14_2010 = []
fevh15_2010 = []
fevh16_2010 = []
fevh17_2010 = []
fevh18_2010 = []
fevh19_2010 = []
fevh20_2010 = []
fevh21_2010 = []
fevh22_2010 = []
fevh23_2010 = []

###############
#   Março     #
###############

marh11_2010 = []
marh12_2010 = []
marh13_2010 = []
marh14_2010 = []
marh15_2010 = []
marh16_2010 = []
marh17_2010 = []
marh18_2010 = []
marh19_2010 = []
marh20_2010 = []
marh21_2010 = []
marh22_2010 = []
marh23_2010 = []

#############
#   Abril   #
#############

abrh11_2010 = []
abrh12_2010 = []
abrh13_2010 = []
abrh14_2010 = []
abrh15_2010 = []
abrh16_2010 = []
abrh17_2010 = []
abrh18_2010 = []
abrh19_2010 = []
abrh20_2010 = []
abrh21_2010 = []
abrh22_2010 = []

############
#   Maio   #
############

maih11_2010 = []
maih12_2010 = []
maih13_2010 = []
maih14_2010 = []
maih15_2010 = []
maih16_2010 = []
maih17_2010 = []
maih18_2010 = []
maih19_2010 = []
maih20_2010 = []
maih21_2010 = []
maih22_2010 = []

#############
#   Junho   #
#############

junh11_2010 = []
junh12_2010 = []
junh13_2010 = []
junh14_2010 = []
junh15_2010 = []
junh16_2010 = []
junh17_2010 = []
junh18_2010 = []
junh19_2010 = []
junh20_2010 = []
junh21_2010 = []
junh22_2010 = []

#############
#   Julho   #
#############

julh11_2010 = []
julh12_2010 = []
julh13_2010 = []
julh14_2010 = []
julh15_2010 = []
julh16_2010 = []
julh17_2010 = []
julh18_2010 = []
julh19_2010 = []
julh20_2010 = []
julh21_2010 = []
julh22_2010 = []

##############
#   Agosto   #
##############

agoh11_2010 = []
agoh12_2010 = []
agoh13_2010 = []
agoh14_2010 = []
agoh15_2010 = []
agoh16_2010 = []
agoh17_2010 = []
agoh18_2010 = []
agoh19_2010 = []
agoh20_2010 = []
agoh21_2010 = []
agoh22_2010 = []

################
#   Setembro   #
################

seth11_2010 = []
seth12_2010 = []
seth13_2010 = []
seth14_2010 = []
seth15_2010 = []
seth16_2010 = []
seth17_2010 = []
seth18_2010 = []
seth19_2010 = []
seth20_2010 = []
seth21_2010 = []
seth22_2010 = []

###############
#   Outubro   #
###############

outh11_2010 = []
outh12_2010 = []
outh13_2010 = []
outh14_2010 = []
outh15_2010 = []
outh16_2010 = []
outh17_2010 = []
outh18_2010 = []
outh19_2010 = []
outh20_2010 = []
outh21_2010 = []
outh22_2010 = []

################
#   Novembro   #
################

novh11_2010 = []
novh12_2010 = []
novh13_2010 = []
novh14_2010 = []
novh15_2010 = []
novh16_2010 = []
novh17_2010 = []
novh18_2010 = []
novh19_2010 = []
novh20_2010 = []
novh21_2010 = []
novh22_2010 = []

################
#   Dezembro   #
################

dezh11_2010 = []
dezh12_2010 = []
dezh13_2010 = []
dezh14_2010 = []
dezh15_2010 = []
dezh16_2010 = []
dezh17_2010 = []
dezh18_2010 = []
dezh19_2010 = []
dezh20_2010 = []
dezh21_2010 = []
dezh22_2010 = []
dezh23_2010 = []
####################################################
#      Preenchimeto das listas com os dados        #
####################################################

###############
#   Janeiro   #
###############

arquivos = r'C:\Users\igorb\OneDrive\Desktop\Projetos\ESTAÇÃO_METEOROLÓGICA\Rad_MS_2010_2020\Regiões\Bolsão\Bolsão.csv'
with open(arquivos) as csv_estacao:
    csv_reader_estacao = csv.reader(csv_estacao, delimiter=',')

    for linha in csv_reader_estacao:

        dia = int(linha[1])
        mes = int(linha[2])
        ano = int(linha[3])
        hora = int(linha[4])
        rad = float(linha[9])
        if ano == 2010:
            if mes == 1:
                if hora == 11:
                    if rad != 0.0:
                        janh11_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 1:
                if hora == 12:
                    if rad != 0:
                        janh12_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 1:
                if hora == 13:
                    if rad != 0:
                        janh13_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 1:
                if hora == 14:
                    if rad != 0:
                        janh14_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 1:
                if hora == 15:
                    if rad != 0:
                        janh15_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 1:
                if hora == 16:
                    if rad != 0:
                        janh16_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 1:
                if hora == 17:
                    if rad != 0:
                        janh17_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 1:
                if hora == 18:
                    if rad != 0:
                        janh18_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 1:
                if hora == 19:
                    if rad != 0:
                        janh19_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 1:
                if hora == 20:
                    if rad != 0:
                        janh20_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 1:
                if hora == 21:
                    if rad != 0:
                        janh21_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 1:
                if hora == 22:
                    if rad != 0:
                        janh22_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 1:
                if hora == 23:
                    if rad != 0:
                        janh23_2010.append([dia, mes, ano, hora, rad])

#################
#   Fevereiro   #
#################

arquivos = r'C:\Users\igorb\OneDrive\Desktop\Projetos\ESTAÇÃO_METEOROLÓGICA\Rad_MS_2010_2020\Regiões\Bolsão\Bolsão.csv'
with open(arquivos) as csv_estacao:
    csv_reader_estacao = csv.reader(csv_estacao, delimiter=',')

    for linha in csv_reader_estacao:

        dia = int(linha[1])
        mes = int(linha[2])
        ano = int(linha[3])
        hora = int(linha[4])
        rad = float(linha[9])
        if ano == 2010:
            if mes == 2:
                if hora == 11:
                    if rad != 0.0:
                        fevh11_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 2:
                if hora == 12:
                    if rad != 0:
                        fevh12_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 2:
                if hora == 13:
                    if rad != 0:
                        fevh13_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 2:
                if hora == 14:
                    if rad != 0:
                        fevh14_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 2:
                if hora == 15:
                    if rad != 0:
                        fevh15_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 2:
                if hora == 16:
                    if rad != 0:
                        fevh16_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 2:
                if hora == 17:
                    if rad != 0:
                        fevh17_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 2:
                if hora == 18:
                    if rad != 0:
                        fevh18_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 2:
                if hora == 19:
                    if rad != 0:
                        fevh19_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 2:
                if hora == 20:
                    if rad != 0:
                        fevh20_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 2:
                if hora == 21:
                    if rad != 0:
                        fevh21_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 2:
                if hora == 22:
                    if rad != 0:
                        fevh22_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 2:
                if hora == 23:
                    if rad != 0:
                        fevh23_2010.append([dia, mes, ano, hora, rad])

###############
#   Março     #
###############

arquivos = r'C:\Users\igorb\OneDrive\Desktop\Projetos\ESTAÇÃO_METEOROLÓGICA\Rad_MS_2010_2020\Regiões\Bolsão\Bolsão.csv'
with open(arquivos) as csv_estacao:
    csv_reader_estacao = csv.reader(csv_estacao, delimiter=',')

    for linha in csv_reader_estacao:

        dia = int(linha[1])
        mes = int(linha[2])
        ano = int(linha[3])
        hora = int(linha[4])
        rad = float(linha[9])
        if ano == 2010:
            if mes == 3:
                if hora == 11:
                    if rad != 0.0:
                        marh11_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 3:
                if hora == 12:
                    if rad != 0:
                        marh12_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 3:
                if hora == 13:
                    if rad != 0:
                        marh13_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 3:
                if hora == 14:
                    if rad != 0:
                        marh14_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 3:
                if hora == 15:
                    if rad != 0:
                        marh15_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 3:
                if hora == 16:
                    if rad != 0:
                        marh16_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 3:
                if hora == 17:
                    if rad != 0:
                        marh17_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 3:
                if hora == 18:
                    if rad != 0:
                        marh18_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 3:
                if hora == 19:
                    if rad != 0:
                        marh19_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 3:
                if hora == 20:
                    if rad != 0:
                        marh20_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 3:
                if hora == 21:
                    if rad != 0:
                        marh21_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 3:
                if hora == 22:
                    if rad != 0:
                        marh22_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 3:
                if hora == 23:
                    if rad != 0:
                        marh23_2010.append([dia, mes, ano, hora, rad])
#############
#   Abril   #
#############

arquivos = r'C:\Users\igorb\OneDrive\Desktop\Projetos\ESTAÇÃO_METEOROLÓGICA\Rad_MS_2010_2020\Regiões\Bolsão\Bolsão.csv'
with open(arquivos) as csv_estacao:
    csv_reader_estacao = csv.reader(csv_estacao, delimiter=',')

    for linha in csv_reader_estacao:

        dia = int(linha[1])
        mes = int(linha[2])
        ano = int(linha[3])
        hora = int(linha[4])
        rad = float(linha[9])
        if ano == 2010:
            if mes == 4:
                if hora == 11:
                    if rad != 0.0:
                        abrh11_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 4:
                if hora == 12:
                    if rad != 0:
                        abrh12_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 4:
                if hora == 13:
                    if rad != 0:
                        abrh13_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 4:
                if hora == 14:
                    if rad != 0:
                        abrh14_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 4:
                if hora == 15:
                    if rad != 0:
                        abrh15_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 4:
                if hora == 16:
                    if rad != 0:
                        abrh16_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 4:
                if hora == 17:
                    if rad != 0:
                        abrh17_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 4:
                if hora == 18:
                    if rad != 0:
                        abrh18_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 4:
                if hora == 19:
                    if rad != 0:
                        abrh19_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 4:
                if hora == 20:
                    if rad != 0:
                        abrh20_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 4:
                if hora == 21:
                    if rad != 0:
                        abrh21_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 4:
                if hora == 22:
                    if rad != 0:
                        abrh22_2010.append([dia, mes, ano, hora, rad])
############
#   Maio   #
############

arquivos = r'C:\Users\igorb\OneDrive\Desktop\Projetos\ESTAÇÃO_METEOROLÓGICA\Rad_MS_2010_2020\Regiões\Bolsão\Bolsão.csv'
with open(arquivos) as csv_estacao:
    csv_reader_estacao = csv.reader(csv_estacao, delimiter=',')

    for linha in csv_reader_estacao:

        dia = int(linha[1])
        mes = int(linha[2])
        ano = int(linha[3])
        hora = int(linha[4])
        rad = float(linha[9])
        if ano == 2010:
            if mes == 5:
                if hora == 11:
                    if rad != 0.0:
                        maih11_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 5:
                if hora == 12:
                    if rad != 0:
                        maih12_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 5:
                if hora == 13:
                    if rad != 0:
                        maih13_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 5:
                if hora == 14:
                    if rad != 0:
                        maih14_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 5:
                if hora == 15:
                    if rad != 0:
                        maih15_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 5:
                if hora == 16:
                    if rad != 0:
                        maih16_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 5:
                if hora == 17:
                    if rad != 0:
                        maih17_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 5:
                if hora == 18:
                    if rad != 0:
                        maih18_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 5:
                if hora == 19:
                    if rad != 0:
                        maih19_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 5:
                if hora == 20:
                    if rad != 0:
                        maih20_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 5:
                if hora == 21:
                    if rad != 0:
                        maih21_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 5:
                if hora == 22:
                    if rad != 0:
                        maih22_2010.append([dia, mes, ano, hora, rad])
#############
#   Junho   #
#############

arquivos = r'C:\Users\igorb\OneDrive\Desktop\Projetos\ESTAÇÃO_METEOROLÓGICA\Rad_MS_2010_2020\Regiões\Bolsão\Bolsão.csv'
with open(arquivos) as csv_estacao:
    csv_reader_estacao = csv.reader(csv_estacao, delimiter=',')

    for linha in csv_reader_estacao:

        dia = int(linha[1])
        mes = int(linha[2])
        ano = int(linha[3])
        hora = int(linha[4])
        rad = float(linha[9])
        if ano == 2010:
            if mes == 6:
                if hora == 11:
                    if rad != 0.0:
                        junh11_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 6:
                if hora == 12:
                    if rad != 0:
                        junh12_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 6:
                if hora == 13:
                    if rad != 0:
                        junh13_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 6:
                if hora == 14:
                    if rad != 0:
                        junh14_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 6:
                if hora == 15:
                    if rad != 0:
                        junh15_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 6:
                if hora == 16:
                    if rad != 0:
                        junh16_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 6:
                if hora == 17:
                    if rad != 0:
                        junh17_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 6:
                if hora == 18:
                    if rad != 0:
                        junh18_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 6:
                if hora == 19:
                    if rad != 0:
                        junh19_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 6:
                if hora == 20:
                    if rad != 0:
                        junh20_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 6:
                if hora == 21:
                    if rad != 0:
                        junh21_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 6:
                if hora == 22:
                    if rad != 0:
                        junh22_2010.append([dia, mes, ano, hora, rad])
#############
#   Julho   #
#############

arquivos = r'C:\Users\igorb\OneDrive\Desktop\Projetos\ESTAÇÃO_METEOROLÓGICA\Rad_MS_2010_2020\Regiões\Bolsão\Bolsão.csv'
with open(arquivos) as csv_estacao:
    csv_reader_estacao = csv.reader(csv_estacao, delimiter=',')

    for linha in csv_reader_estacao:

        dia = int(linha[1])
        mes = int(linha[2])
        ano = int(linha[3])
        hora = int(linha[4])
        rad = float(linha[9])
        if ano == 2010:
            if mes == 7:
                if hora == 11:
                    if rad != 0.0:
                        julh11_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 7:
                if hora == 12:
                    if rad != 0:
                        julh12_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 7:
                if hora == 13:
                    if rad != 0:
                        julh13_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 7:
                if hora == 14:
                    if rad != 0:
                        julh14_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 7:
                if hora == 15:
                    if rad != 0:
                        julh15_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 7:
                if hora == 16:
                    if rad != 0:
                        julh16_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 7:
                if hora == 17:
                    if rad != 0:
                        julh17_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 7:
                if hora == 18:
                    if rad != 0:
                        julh18_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 7:
                if hora == 19:
                    if rad != 0:
                        julh19_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 7:
                if hora == 20:
                    if rad != 0:
                        julh20_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 7:
                if hora == 21:
                    if rad != 0:
                        julh21_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 7:
                if hora == 22:
                    if rad != 0:
                        julh22_2010.append([dia, mes, ano, hora, rad])
##############
#   Agosto   #
##############

arquivos = r'C:\Users\igorb\OneDrive\Desktop\Projetos\ESTAÇÃO_METEOROLÓGICA\Rad_MS_2010_2020\Regiões\Bolsão\Bolsão.csv'
with open(arquivos) as csv_estacao:
    csv_reader_estacao = csv.reader(csv_estacao, delimiter=',')

    for linha in csv_reader_estacao:

        dia = int(linha[1])
        mes = int(linha[2])
        ano = int(linha[3])
        hora = int(linha[4])
        rad = float(linha[9])
        if ano == 2010:
            if mes == 8:
                if hora == 11:
                    if rad != 0.0:
                        agoh11_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 8:
                if hora == 12:
                    if rad != 0:
                        agoh12_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 8:
                if hora == 13:
                    if rad != 0:
                        agoh13_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 8:
                if hora == 14:
                    if rad != 0:
                        agoh14_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 8:
                if hora == 15:
                    if rad != 0:
                        agoh15_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 8:
                if hora == 16:
                    if rad != 0:
                        agoh16_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 8:
                if hora == 17:
                    if rad != 0:
                        agoh17_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 8:
                if hora == 18:
                    if rad != 0:
                        agoh18_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 8:
                if hora == 19:
                    if rad != 0:
                        agoh19_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 8:
                if hora == 20:
                    if rad != 0:
                        agoh20_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 8:
                if hora == 21:
                    if rad != 0:
                        agoh21_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 8:
                if hora == 22:
                    if rad != 0:
                        agoh22_2010.append([dia, mes, ano, hora, rad])
################
#   Setembro   #
################

arquivos = r'C:\Users\igorb\OneDrive\Desktop\Projetos\ESTAÇÃO_METEOROLÓGICA\Rad_MS_2010_2020\Regiões\Bolsão\Bolsão.csv'
with open(arquivos) as csv_estacao:
    csv_reader_estacao = csv.reader(csv_estacao, delimiter=',')

    for linha in csv_reader_estacao:

        dia = int(linha[1])
        mes = int(linha[2])
        ano = int(linha[3])
        hora = int(linha[4])
        rad = float(linha[9])
        if ano == 2010:
            if mes == 9:
                if hora == 11:
                    if rad != 0.0:
                        seth11_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 9:
                if hora == 12:
                    if rad != 0:
                        seth12_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 9:
                if hora == 13:
                    if rad != 0:
                        seth13_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 9:
                if hora == 14:
                    if rad != 0:
                        seth14_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 9:
                if hora == 15:
                    if rad != 0:
                        seth15_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 9:
                if hora == 16:
                    if rad != 0:
                        seth16_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 9:
                if hora == 17:
                    if rad != 0:
                        seth17_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 9:
                if hora == 18:
                    if rad != 0:
                        seth18_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 9:
                if hora == 19:
                    if rad != 0:
                        seth19_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 9:
                if hora == 20:
                    if rad != 0:
                        seth20_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 9:
                if hora == 21:
                    if rad != 0:
                        seth21_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 9:
                if hora == 22:
                    if rad != 0:
                        seth22_2010.append([dia, mes, ano, hora, rad])
###############
#   Outubro   #
###############

arquivos = r'C:\Users\igorb\OneDrive\Desktop\Projetos\ESTAÇÃO_METEOROLÓGICA\Rad_MS_2010_2020\Regiões\Bolsão\Bolsão.csv'
with open(arquivos) as csv_estacao:
    csv_reader_estacao = csv.reader(csv_estacao, delimiter=',')

    for linha in csv_reader_estacao:

        dia = int(linha[1])
        mes = int(linha[2])
        ano = int(linha[3])
        hora = int(linha[4])
        rad = float(linha[9])
        if ano == 2010:
            if mes == 10:
                if hora == 11:
                    if rad != 0.0:
                        outh11_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 10:
                if hora == 12:
                    if rad != 0:
                        outh12_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 10:
                if hora == 13:
                    if rad != 0:
                        outh13_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 10:
                if hora == 14:
                    if rad != 0:
                        outh14_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 10:
                if hora == 15:
                    if rad != 0:
                        outh15_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 10:
                if hora == 16:
                    if rad != 0:
                        outh16_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 10:
                if hora == 17:
                    if rad != 0:
                        outh17_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 10:
                if hora == 18:
                    if rad != 0:
                        outh18_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 10:
                if hora == 19:
                    if rad != 0:
                        outh19_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 10:
                if hora == 20:
                    if rad != 0:
                        outh20_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 10:
                if hora == 21:
                    if rad != 0:
                        outh21_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 10:
                if hora == 22:
                    if rad != 0:
                        outh22_2010.append([dia, mes, ano, hora, rad])

################
#   Novembro   #
################

arquivos = r'C:\Users\igorb\OneDrive\Desktop\Projetos\ESTAÇÃO_METEOROLÓGICA\Rad_MS_2010_2020\Regiões\Bolsão\Bolsão.csv'
with open(arquivos) as csv_estacao:
    csv_reader_estacao = csv.reader(csv_estacao, delimiter=',')

    for linha in csv_reader_estacao:

        dia = int(linha[1])
        mes = int(linha[2])
        ano = int(linha[3])
        hora = int(linha[4])
        rad = float(linha[9])
        if ano == 2010:
            if mes == 11:
                if hora == 11:
                    if rad != 0.0:
                        novh11_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 11:
                if hora == 12:
                    if rad != 0:
                        novh12_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 11:
                if hora == 13:
                    if rad != 0:
                        novh13_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 11:
                if hora == 14:
                    if rad != 0:
                        novh14_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 11:
                if hora == 15:
                    if rad != 0:
                        novh15_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 11:
                if hora == 16:
                    if rad != 0:
                        novh16_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 11:
                if hora == 17:
                    if rad != 0:
                        novh17_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 11:
                if hora == 18:
                    if rad != 0:
                        novh18_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 11:
                if hora == 19:
                    if rad != 0:
                        novh19_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 11:
                if hora == 20:
                    if rad != 0:
                        novh20_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 11:
                if hora == 21:
                    if rad != 0:
                        novh21_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 11:
                if hora == 22:
                    if rad != 0:
                        novh22_2010.append([dia, mes, ano, hora, rad])
################
#   Dezembro   #
################

arquivos = r'C:\Users\igorb\OneDrive\Desktop\Projetos\ESTAÇÃO_METEOROLÓGICA\Rad_MS_2010_2020\Regiões\Bolsão\Bolsão.csv'
with open(arquivos) as csv_estacao:
    csv_reader_estacao = csv.reader(csv_estacao, delimiter=',')

    for linha in csv_reader_estacao:

        dia = int(linha[1])
        mes = int(linha[2])
        ano = int(linha[3])
        hora = int(linha[4])
        rad = float(linha[9])
        if ano == 2010:
            if mes == 12:
                if hora == 11:
                    if rad != 0.0:
                        dezh11_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 12:
                if hora == 12:
                    if rad != 0:
                        dezh12_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 12:
                if hora == 13:
                    if rad != 0:
                        dezh13_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 12:
                if hora == 14:
                    if rad != 0:
                        dezh14_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 12:
                if hora == 15:
                    if rad != 0:
                        dezh15_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 12:
                if hora == 16:
                    if rad != 0:
                        dezh16_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 12:
                if hora == 17:
                    if rad != 0:
                        dezh17_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 12:
                if hora == 18:
                    if rad != 0:
                        dezh18_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 12:
                if hora == 19:
                    if rad != 0:
                        dezh19_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 12:
                if hora == 20:
                    if rad != 0:
                        dezh20_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 12:
                if hora == 21:
                    if rad != 0:
                        dezh21_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 12:
                if hora == 22:
                    if rad != 0:
                        dezh22_2010.append([dia, mes, ano, hora, rad])
        if ano == 2010:
            if mes == 12:
                if hora == 23:
                    if rad != 0:
                        dezh23_2010.append([dia, mes, ano, hora, rad])

                #################################################
                #      Criação de matrizes com as listas        #
                #################################################
###############
#   Janeiro   #
###############

jan_rh11_2010 = pd.DataFrame(
    janh11_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jan_rh12_2010 = pd.DataFrame(
    janh12_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jan_rh13_2010 = pd.DataFrame(
    janh13_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jan_rh14_2010 = pd.DataFrame(
    janh14_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jan_rh15_2010 = pd.DataFrame(
    janh15_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jan_rh16_2010 = pd.DataFrame(
    janh16_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jan_rh17_2010 = pd.DataFrame(
    janh17_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jan_rh18_2010 = pd.DataFrame(
    janh18_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jan_rh19_2010 = pd.DataFrame(
    janh19_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jan_rh20_2010 = pd.DataFrame(
    janh20_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jan_rh21_2010 = pd.DataFrame(
    janh21_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jan_rh22_2010 = pd.DataFrame(
    janh22_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jan_rh23_2010 = pd.DataFrame(
    janh23_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])

#################
#   Fevereiro   #
#################

fev_rh11_2010 = pd.DataFrame(
    fevh11_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
fev_rh12_2010 = pd.DataFrame(
    fevh12_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
fev_rh13_2010 = pd.DataFrame(
    fevh13_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
fev_rh14_2010 = pd.DataFrame(
    fevh14_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
fev_rh15_2010 = pd.DataFrame(
    fevh15_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
fev_rh16_2010 = pd.DataFrame(
    fevh16_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
fev_rh17_2010 = pd.DataFrame(
    fevh17_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
fev_rh18_2010 = pd.DataFrame(
    fevh18_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
fev_rh19_2010 = pd.DataFrame(
    fevh19_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
fev_rh20_2010 = pd.DataFrame(
    fevh20_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
fev_rh21_2010 = pd.DataFrame(
    fevh21_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
fev_rh22_2010 = pd.DataFrame(
    fevh22_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
fev_rh23_2010 = pd.DataFrame(
    fevh23_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])

###############
#   Março     #
###############

mar_rh11_2010 = pd.DataFrame(
    marh11_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
mar_rh12_2010 = pd.DataFrame(
    marh12_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
mar_rh13_2010 = pd.DataFrame(
    marh13_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
mar_rh14_2010 = pd.DataFrame(
    marh14_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
mar_rh15_2010 = pd.DataFrame(
    marh15_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
mar_rh16_2010 = pd.DataFrame(
    marh16_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
mar_rh17_2010 = pd.DataFrame(
    marh17_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
mar_rh18_2010 = pd.DataFrame(
    marh18_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
mar_rh19_2010 = pd.DataFrame(
    marh19_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
mar_rh20_2010 = pd.DataFrame(
    marh20_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
mar_rh21_2010 = pd.DataFrame(
    marh21_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
mar_rh22_2010 = pd.DataFrame(
    marh22_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
mar_rh23_2010 = pd.DataFrame(
    marh23_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])

#############
#   Abril   #
#############

abr_rh11_2010 = pd.DataFrame(
    abrh11_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
abr_rh12_2010 = pd.DataFrame(
    abrh12_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
abr_rh13_2010 = pd.DataFrame(
    abrh13_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
abr_rh14_2010 = pd.DataFrame(
    abrh14_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
abr_rh15_2010 = pd.DataFrame(
    abrh15_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
abr_rh16_2010 = pd.DataFrame(
    abrh16_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
abr_rh17_2010 = pd.DataFrame(
    abrh17_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
abr_rh18_2010 = pd.DataFrame(
    abrh18_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
abr_rh19_2010 = pd.DataFrame(
    abrh19_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
abr_rh20_2010 = pd.DataFrame(
    abrh20_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
abr_rh21_2010 = pd.DataFrame(
    abrh21_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
abr_rh22_2010 = pd.DataFrame(
    abrh22_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])

############
#   Maio   #
############

mai_rh11_2010 = pd.DataFrame(
    maih11_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
mai_rh12_2010 = pd.DataFrame(
    maih12_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
mai_rh13_2010 = pd.DataFrame(
    maih13_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
mai_rh14_2010 = pd.DataFrame(
    maih14_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
mai_rh15_2010 = pd.DataFrame(
    maih15_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
mai_rh16_2010 = pd.DataFrame(
    maih16_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
mai_rh17_2010 = pd.DataFrame(
    maih17_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
mai_rh18_2010 = pd.DataFrame(
    maih18_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
mai_rh19_2010 = pd.DataFrame(
    maih19_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
mai_rh20_2010 = pd.DataFrame(
    maih20_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
mai_rh21_2010 = pd.DataFrame(
    maih21_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
mai_rh22_2010 = pd.DataFrame(
    maih22_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])

#############
#   Junho   #
#############

jun_rh11_2010 = pd.DataFrame(
    junh11_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jun_rh12_2010 = pd.DataFrame(
    junh12_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jun_rh13_2010 = pd.DataFrame(
    junh13_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jun_rh14_2010 = pd.DataFrame(
    junh14_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jun_rh15_2010 = pd.DataFrame(
    junh15_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jun_rh16_2010 = pd.DataFrame(
    junh16_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jun_rh17_2010 = pd.DataFrame(
    junh17_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jun_rh18_2010 = pd.DataFrame(
    junh18_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jun_rh19_2010 = pd.DataFrame(
    junh19_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jun_rh20_2010 = pd.DataFrame(
    junh20_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jun_rh21_2010 = pd.DataFrame(
    junh21_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jun_rh22_2010 = pd.DataFrame(
    junh22_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])

#############
#   Julho   #
#############

jul_rh11_2010 = pd.DataFrame(
    julh11_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jul_rh12_2010 = pd.DataFrame(
    julh12_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jul_rh13_2010 = pd.DataFrame(
    julh13_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jul_rh14_2010 = pd.DataFrame(
    julh14_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jul_rh15_2010 = pd.DataFrame(
    julh15_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jul_rh16_2010 = pd.DataFrame(
    julh16_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jul_rh17_2010 = pd.DataFrame(
    julh17_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jul_rh18_2010 = pd.DataFrame(
    julh18_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jul_rh19_2010 = pd.DataFrame(
    julh19_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jul_rh20_2010 = pd.DataFrame(
    julh20_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jul_rh21_2010 = pd.DataFrame(
    julh21_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
jul_rh22_2010 = pd.DataFrame(
    julh22_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])

##############
#   Agosto   #
##############

ago_rh11_2010 = pd.DataFrame(
    agoh11_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
ago_rh12_2010 = pd.DataFrame(
    agoh12_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
ago_rh13_2010 = pd.DataFrame(
    agoh13_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
ago_rh14_2010 = pd.DataFrame(
    agoh14_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
ago_rh15_2010 = pd.DataFrame(
    agoh15_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
ago_rh16_2010 = pd.DataFrame(
    agoh16_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
ago_rh17_2010 = pd.DataFrame(
    agoh17_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
ago_rh18_2010 = pd.DataFrame(
    agoh18_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
ago_rh19_2010 = pd.DataFrame(
    agoh19_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
ago_rh20_2010 = pd.DataFrame(
    agoh20_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
ago_rh21_2010 = pd.DataFrame(
    agoh21_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
ago_rh22_2010 = pd.DataFrame(
    agoh22_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])

################
#   Setembro   #
################

set_rh11_2010 = pd.DataFrame(
    seth11_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
set_rh12_2010 = pd.DataFrame(
    seth12_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
set_rh13_2010 = pd.DataFrame(
    seth13_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
set_rh14_2010 = pd.DataFrame(
    seth14_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
set_rh15_2010 = pd.DataFrame(
    seth15_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
set_rh16_2010 = pd.DataFrame(
    seth16_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
set_rh17_2010 = pd.DataFrame(
    seth17_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
set_rh18_2010 = pd.DataFrame(
    seth18_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
set_rh19_2010 = pd.DataFrame(
    seth19_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
set_rh20_2010 = pd.DataFrame(
    seth20_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
set_rh21_2010 = pd.DataFrame(
    seth21_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
set_rh22_2010 = pd.DataFrame(
    seth22_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])

###############
#   Outubro   #
###############

out_rh11_2010 = pd.DataFrame(
    outh11_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
out_rh12_2010 = pd.DataFrame(
    outh12_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
out_rh13_2010 = pd.DataFrame(
    outh13_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
out_rh14_2010 = pd.DataFrame(
    outh14_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
out_rh15_2010 = pd.DataFrame(
    outh15_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
out_rh16_2010 = pd.DataFrame(
    outh16_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
out_rh17_2010 = pd.DataFrame(
    outh17_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
out_rh18_2010 = pd.DataFrame(
    outh18_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
out_rh19_2010 = pd.DataFrame(
    outh19_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
out_rh20_2010 = pd.DataFrame(
    outh20_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
out_rh21_2010 = pd.DataFrame(
    outh21_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
out_rh22_2010 = pd.DataFrame(
    outh22_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])

################
#   Novembro   #
################

nov_rh11_2010 = pd.DataFrame(
    novh11_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
nov_rh12_2010 = pd.DataFrame(
    novh12_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
nov_rh13_2010 = pd.DataFrame(
    novh13_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
nov_rh14_2010 = pd.DataFrame(
    novh14_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
nov_rh15_2010 = pd.DataFrame(
    novh15_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
nov_rh16_2010 = pd.DataFrame(
    novh16_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
nov_rh17_2010 = pd.DataFrame(
    novh17_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
nov_rh18_2010 = pd.DataFrame(
    novh18_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
nov_rh19_2010 = pd.DataFrame(
    novh19_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
nov_rh20_2010 = pd.DataFrame(
    novh20_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
nov_rh21_2010 = pd.DataFrame(
    novh21_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
nov_rh22_2010 = pd.DataFrame(
    novh22_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])

################
#   Dezembro   #
################

dez_rh11_2010 = pd.DataFrame(
    dezh11_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
dez_rh12_2010 = pd.DataFrame(
    dezh12_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
dez_rh13_2010 = pd.DataFrame(
    dezh13_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
dez_rh14_2010 = pd.DataFrame(
    dezh14_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
dez_rh15_2010 = pd.DataFrame(
    dezh15_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
dez_rh16_2010 = pd.DataFrame(
    dezh16_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
dez_rh17_2010 = pd.DataFrame(
    dezh17_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
dez_rh18_2010 = pd.DataFrame(
    dezh18_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
dez_rh19_2010 = pd.DataFrame(
    dezh19_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
dez_rh20_2010 = pd.DataFrame(
    dezh20_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
dez_rh21_2010 = pd.DataFrame(
    dezh21_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
dez_rh22_2010 = pd.DataFrame(
    dezh22_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])
dez_rh23_2010 = pd.DataFrame(
    dezh23_2010, columns=['dia', 'mes', 'ano', 'hora', 'rad'])

##################################
#      Calculo da média          #
##################################
###############
#   Janeiro   #
###############

jan_rh11_rad_2010 = jan_rh11_2010['rad']
jan_rh11media_2010 = sum(jan_rh11_rad_2010) / len(jan_rh11_rad_2010)
jan_rh12_rad_2010 = jan_rh12_2010['rad']
jan_rh12media_2010 = sum(jan_rh12_rad_2010) / len(jan_rh12_rad_2010)
jan_rh13_rad_2010 = jan_rh13_2010['rad']
jan_rh13media_2010 = sum(jan_rh13_rad_2010) / len(jan_rh13_rad_2010)
jan_rh14_rad_2010 = jan_rh14_2010['rad']
jan_rh14media_2010 = sum(jan_rh14_rad_2010) / len(jan_rh14_rad_2010)
jan_rh15_rad_2010 = jan_rh15_2010['rad']
jan_rh15media_2010 = sum(jan_rh15_rad_2010) / len(jan_rh15_rad_2010)
jan_rh16_rad_2010 = jan_rh16_2010['rad']
jan_rh16media_2010 = sum(jan_rh16_rad_2010) / len(jan_rh16_rad_2010)
jan_rh17_rad_2010 = jan_rh17_2010['rad']
jan_rh17media_2010 = sum(jan_rh17_rad_2010) / len(jan_rh17_rad_2010)
jan_rh18_rad_2010 = jan_rh18_2010['rad']
jan_rh18media_2010 = sum(jan_rh18_rad_2010) / len(jan_rh18_rad_2010)
jan_rh19_rad_2010 = jan_rh19_2010['rad']
jan_rh19media_2010 = sum(jan_rh19_rad_2010) / len(jan_rh19_rad_2010)
jan_rh20_rad_2010 = jan_rh20_2010['rad']
jan_rh20media_2010 = sum(jan_rh20_rad_2010) / len(jan_rh20_rad_2010)
jan_rh21_rad_2010 = jan_rh21_2010['rad']
jan_rh21media_2010 = sum(jan_rh21_rad_2010) / len(jan_rh21_rad_2010)
jan_rh22_rad_2010 = jan_rh22_2010['rad']
jan_rh22media_2010 = sum(jan_rh22_rad_2010) / len(jan_rh22_rad_2010)
jan_rh23_rad_2010 = jan_rh23_2010['rad']
jan_rh23media_2010 = sum(jan_rh23_rad_2010) / len(jan_rh23_rad_2010)

#################
#   Fevereiro   #
#################

fev_rh11_rad_2010 = fev_rh11_2010['rad']
fev_rh11media_2010 = sum(fev_rh11_rad_2010) / len(fev_rh11_rad_2010)
fev_rh12_rad_2010 = fev_rh12_2010['rad']
fev_rh12media_2010 = sum(fev_rh12_rad_2010) / len(fev_rh12_rad_2010)
fev_rh13_rad_2010 = fev_rh13_2010['rad']
fev_rh13media_2010 = sum(fev_rh13_rad_2010) / len(fev_rh13_rad_2010)
fev_rh14_rad_2010 = fev_rh14_2010['rad']
fev_rh14media_2010 = sum(fev_rh14_rad_2010) / len(fev_rh14_rad_2010)
fev_rh15_rad_2010 = fev_rh15_2010['rad']
fev_rh15media_2010 = sum(fev_rh15_rad_2010) / len(fev_rh15_rad_2010)
fev_rh16_rad_2010 = fev_rh16_2010['rad']
fev_rh16media_2010 = sum(fev_rh16_rad_2010) / len(fev_rh16_rad_2010)
fev_rh17_rad_2010 = fev_rh17_2010['rad']
fev_rh17media_2010 = sum(fev_rh17_rad_2010) / len(fev_rh17_rad_2010)
fev_rh18_rad_2010 = fev_rh18_2010['rad']
fev_rh18media_2010 = sum(fev_rh18_rad_2010) / len(fev_rh18_rad_2010)
fev_rh19_rad_2010 = fev_rh19_2010['rad']
fev_rh19media_2010 = sum(fev_rh19_rad_2010) / len(fev_rh19_rad_2010)
fev_rh20_rad_2010 = fev_rh20_2010['rad']
fev_rh20media_2010 = sum(fev_rh20_rad_2010) / len(fev_rh20_rad_2010)
fev_rh21_rad_2010 = fev_rh21_2010['rad']
fev_rh21media_2010 = sum(fev_rh21_rad_2010) / len(fev_rh21_rad_2010)
fev_rh22_rad_2010 = fev_rh22_2010['rad']
fev_rh22media_2010 = sum(fev_rh22_rad_2010) / len(fev_rh22_rad_2010)
fev_rh23_rad_2010 = fev_rh23_2010['rad']
fev_rh23media_2010 = sum(fev_rh23_rad_2010) / len(fev_rh23_rad_2010)

###############
#   Março     #
###############

mar_rh11_rad_2010 = mar_rh11_2010['rad']
mar_rh11media_2010 = sum(mar_rh11_rad_2010) / len(mar_rh11_rad_2010)
mar_rh12_rad_2010 = mar_rh12_2010['rad']
mar_rh12media_2010 = sum(mar_rh12_rad_2010) / len(mar_rh12_rad_2010)
mar_rh13_rad_2010 = mar_rh13_2010['rad']
mar_rh13media_2010 = sum(mar_rh13_rad_2010) / len(mar_rh13_rad_2010)
mar_rh14_rad_2010 = mar_rh14_2010['rad']
mar_rh14media_2010 = sum(mar_rh14_rad_2010) / len(mar_rh14_rad_2010)
mar_rh15_rad_2010 = mar_rh15_2010['rad']
mar_rh15media_2010 = sum(mar_rh15_rad_2010) / len(mar_rh15_rad_2010)
mar_rh16_rad_2010 = mar_rh16_2010['rad']
mar_rh16media_2010 = sum(mar_rh16_rad_2010) / len(mar_rh16_rad_2010)
mar_rh17_rad_2010 = mar_rh17_2010['rad']
mar_rh17media_2010 = sum(mar_rh17_rad_2010) / len(mar_rh17_rad_2010)
mar_rh18_rad_2010 = mar_rh18_2010['rad']
mar_rh18media_2010 = sum(mar_rh18_rad_2010) / len(mar_rh18_rad_2010)
mar_rh19_rad_2010 = mar_rh19_2010['rad']
mar_rh19media_2010 = sum(mar_rh19_rad_2010) / len(mar_rh19_rad_2010)
mar_rh20_rad_2010 = mar_rh20_2010['rad']
mar_rh20media_2010 = sum(mar_rh20_rad_2010) / len(mar_rh20_rad_2010)
mar_rh21_rad_2010 = mar_rh21_2010['rad']
mar_rh21media_2010 = sum(mar_rh21_rad_2010) / len(mar_rh21_rad_2010)
mar_rh22_rad_2010 = mar_rh22_2010['rad']
mar_rh22media_2010 = sum(mar_rh22_rad_2010) / len(mar_rh22_rad_2010)
mar_rh23_rad_2010 = mar_rh23_2010['rad']
mar_rh23media_2010 = sum(mar_rh23_rad_2010) / len(mar_rh23_rad_2010)

#############
#   Abril   #
#############

abr_rh11_rad_2010 = abr_rh11_2010['rad']
abr_rh11media_2010 = sum(abr_rh11_rad_2010) / len(abr_rh11_rad_2010)
abr_rh12_rad_2010 = abr_rh12_2010['rad']
abr_rh12media_2010 = sum(abr_rh12_rad_2010) / len(abr_rh12_rad_2010)
abr_rh13_rad_2010 = abr_rh13_2010['rad']
abr_rh13media_2010 = sum(abr_rh13_rad_2010) / len(abr_rh13_rad_2010)
abr_rh14_rad_2010 = abr_rh14_2010['rad']
abr_rh14media_2010 = sum(abr_rh14_rad_2010) / len(abr_rh14_rad_2010)
abr_rh15_rad_2010 = abr_rh15_2010['rad']
abr_rh15media_2010 = sum(abr_rh15_rad_2010) / len(abr_rh15_rad_2010)
abr_rh16_rad_2010 = abr_rh16_2010['rad']
abr_rh16media_2010 = sum(abr_rh16_rad_2010) / len(abr_rh16_rad_2010)
abr_rh17_rad_2010 = abr_rh17_2010['rad']
abr_rh17media_2010 = sum(abr_rh17_rad_2010) / len(abr_rh17_rad_2010)
abr_rh18_rad_2010 = abr_rh18_2010['rad']
abr_rh18media_2010 = sum(abr_rh18_rad_2010) / len(abr_rh18_rad_2010)
abr_rh19_rad_2010 = abr_rh19_2010['rad']
abr_rh19media_2010 = sum(abr_rh19_rad_2010) / len(abr_rh19_rad_2010)
abr_rh20_rad_2010 = abr_rh20_2010['rad']
abr_rh20media_2010 = sum(abr_rh20_rad_2010) / len(abr_rh20_rad_2010)
abr_rh21_rad_2010 = abr_rh21_2010['rad']
abr_rh21media_2010 = sum(abr_rh21_rad_2010) / len(abr_rh21_rad_2010)
abr_rh22_rad_2010 = abr_rh22_2010['rad']
abr_rh22media_2010 = sum(abr_rh22_rad_2010) / len(abr_rh22_rad_2010)

############
#   Maio   #
############

mai_rh11_rad_2010 = mai_rh11_2010['rad']
mai_rh11media_2010 = sum(mai_rh11_rad_2010) / len(mai_rh11_rad_2010)
mai_rh12_rad_2010 = mai_rh12_2010['rad']
mai_rh12media_2010 = sum(mai_rh12_rad_2010) / len(mai_rh12_rad_2010)
mai_rh13_rad_2010 = mai_rh13_2010['rad']
mai_rh13media_2010 = sum(mai_rh13_rad_2010) / len(mai_rh13_rad_2010)
mai_rh14_rad_2010 = mai_rh14_2010['rad']
mai_rh14media_2010 = sum(mai_rh14_rad_2010) / len(mai_rh14_rad_2010)
mai_rh15_rad_2010 = mai_rh15_2010['rad']
mai_rh15media_2010 = sum(mai_rh15_rad_2010) / len(mai_rh15_rad_2010)
mai_rh16_rad_2010 = mai_rh16_2010['rad']
mai_rh16media_2010 = sum(mai_rh16_rad_2010) / len(mai_rh16_rad_2010)
mai_rh17_rad_2010 = mai_rh17_2010['rad']
mai_rh17media_2010 = sum(mai_rh17_rad_2010) / len(mai_rh17_rad_2010)
mai_rh18_rad_2010 = mai_rh18_2010['rad']
mai_rh18media_2010 = sum(mai_rh18_rad_2010) / len(mai_rh18_rad_2010)
mai_rh19_rad_2010 = mai_rh19_2010['rad']
mai_rh19media_2010 = sum(mai_rh19_rad_2010) / len(mai_rh19_rad_2010)
mai_rh20_rad_2010 = mai_rh20_2010['rad']
mai_rh20media_2010 = sum(mai_rh20_rad_2010) / len(mai_rh20_rad_2010)
mai_rh21_rad_2010 = mai_rh21_2010['rad']
mai_rh21media_2010 = sum(mai_rh21_rad_2010) / len(mai_rh21_rad_2010)
mai_rh22_rad_2010 = mai_rh22_2010['rad']
mai_rh22media_2010 = sum(mai_rh22_rad_2010) / len(mai_rh22_rad_2010)

#############
#   Junho   #
#############

jun_rh11_rad_2010 = jun_rh11_2010['rad']
jun_rh11media_2010 = sum(jun_rh11_rad_2010) / len(jun_rh11_rad_2010)
jun_rh12_rad_2010 = jun_rh12_2010['rad']
jun_rh12media_2010 = sum(jun_rh12_rad_2010) / len(jun_rh12_rad_2010)
jun_rh13_rad_2010 = jun_rh13_2010['rad']
jun_rh13media_2010 = sum(jun_rh13_rad_2010) / len(jun_rh13_rad_2010)
jun_rh14_rad_2010 = jun_rh14_2010['rad']
jun_rh14media_2010 = sum(jun_rh14_rad_2010) / len(jun_rh14_rad_2010)
jun_rh15_rad_2010 = jun_rh15_2010['rad']
jun_rh15media_2010 = sum(jun_rh15_rad_2010) / len(jun_rh15_rad_2010)
jun_rh16_rad_2010 = jun_rh16_2010['rad']
jun_rh16media_2010 = sum(jun_rh16_rad_2010) / len(jun_rh16_rad_2010)
jun_rh17_rad_2010 = jun_rh17_2010['rad']
jun_rh17media_2010 = sum(jun_rh17_rad_2010) / len(jun_rh17_rad_2010)
jun_rh18_rad_2010 = jun_rh18_2010['rad']
jun_rh18media_2010 = sum(jun_rh18_rad_2010) / len(jun_rh18_rad_2010)
jun_rh19_rad_2010 = jun_rh19_2010['rad']
jun_rh19media_2010 = sum(jun_rh19_rad_2010) / len(jun_rh19_rad_2010)
jun_rh20_rad_2010 = jun_rh20_2010['rad']
jun_rh20media_2010 = sum(jun_rh20_rad_2010) / len(jun_rh20_rad_2010)
jun_rh21_rad_2010 = jun_rh21_2010['rad']
jun_rh21media_2010 = sum(jun_rh21_rad_2010) / len(jun_rh21_rad_2010)
jun_rh22_rad_2010 = jun_rh22_2010['rad']
jun_rh22media_2010 = sum(jun_rh22_rad_2010) / len(jun_rh22_rad_2010)

#############
#   Julho   #
#############

jul_rh11_rad_2010 = jul_rh11_2010['rad']
jul_rh11media_2010 = sum(jul_rh11_rad_2010) / len(jul_rh11_rad_2010)
jul_rh12_rad_2010 = jul_rh12_2010['rad']
jul_rh12media_2010 = sum(jul_rh12_rad_2010) / len(jul_rh12_rad_2010)
jul_rh13_rad_2010 = jul_rh13_2010['rad']
jul_rh13media_2010 = sum(jul_rh13_rad_2010) / len(jul_rh13_rad_2010)
jul_rh14_rad_2010 = jul_rh14_2010['rad']
jul_rh14media_2010 = sum(jul_rh14_rad_2010) / len(jul_rh14_rad_2010)
jul_rh15_rad_2010 = jul_rh15_2010['rad']
jul_rh15media_2010 = sum(jul_rh15_rad_2010) / len(jul_rh15_rad_2010)
jul_rh16_rad_2010 = jul_rh16_2010['rad']
jul_rh16media_2010 = sum(jul_rh16_rad_2010) / len(jul_rh16_rad_2010)
jul_rh17_rad_2010 = jul_rh17_2010['rad']
jul_rh17media_2010 = sum(jul_rh17_rad_2010) / len(jul_rh17_rad_2010)
jul_rh18_rad_2010 = jul_rh18_2010['rad']
jul_rh18media_2010 = sum(jul_rh18_rad_2010) / len(jul_rh18_rad_2010)
jul_rh19_rad_2010 = jul_rh19_2010['rad']
jul_rh19media_2010 = sum(jul_rh19_rad_2010) / len(jul_rh19_rad_2010)
jul_rh20_rad_2010 = jul_rh20_2010['rad']
jul_rh20media_2010 = sum(jul_rh20_rad_2010) / len(jul_rh20_rad_2010)
jul_rh21_rad_2010 = jul_rh21_2010['rad']
jul_rh21media_2010 = sum(jul_rh21_rad_2010) / len(jul_rh21_rad_2010)
jul_rh22_rad_2010 = jul_rh22_2010['rad']
jul_rh22media_2010 = sum(jul_rh22_rad_2010) / len(jul_rh22_rad_2010)

##############
#   Agosto   #
##############

ago_rh11_rad_2010 = ago_rh11_2010['rad']
ago_rh11media_2010 = sum(ago_rh11_rad_2010) / len(ago_rh11_rad_2010)
ago_rh12_rad_2010 = ago_rh12_2010['rad']
ago_rh12media_2010 = sum(ago_rh12_rad_2010) / len(ago_rh12_rad_2010)
ago_rh13_rad_2010 = ago_rh13_2010['rad']
ago_rh13media_2010 = sum(ago_rh13_rad_2010) / len(ago_rh13_rad_2010)
ago_rh14_rad_2010 = ago_rh14_2010['rad']
ago_rh14media_2010 = sum(ago_rh14_rad_2010) / len(ago_rh14_rad_2010)
ago_rh15_rad_2010 = ago_rh15_2010['rad']
ago_rh15media_2010 = sum(ago_rh15_rad_2010) / len(ago_rh15_rad_2010)
ago_rh16_rad_2010 = ago_rh16_2010['rad']
ago_rh16media_2010 = sum(ago_rh16_rad_2010) / len(ago_rh16_rad_2010)
ago_rh17_rad_2010 = ago_rh17_2010['rad']
ago_rh17media_2010 = sum(ago_rh17_rad_2010) / len(ago_rh17_rad_2010)
ago_rh18_rad_2010 = ago_rh18_2010['rad']
ago_rh18media_2010 = sum(ago_rh18_rad_2010) / len(ago_rh18_rad_2010)
ago_rh19_rad_2010 = ago_rh19_2010['rad']
ago_rh19media_2010 = sum(ago_rh19_rad_2010) / len(ago_rh19_rad_2010)
ago_rh20_rad_2010 = ago_rh20_2010['rad']
ago_rh20media_2010 = sum(ago_rh20_rad_2010) / len(ago_rh20_rad_2010)
ago_rh21_rad_2010 = ago_rh21_2010['rad']
ago_rh21media_2010 = sum(ago_rh21_rad_2010) / len(ago_rh21_rad_2010)
ago_rh22_rad_2010 = ago_rh22_2010['rad']
ago_rh22media_2010 = sum(ago_rh22_rad_2010) / len(ago_rh22_rad_2010)

################
#   Setembro   #
################

set_rh11_rad_2010 = set_rh11_2010['rad']
set_rh11media_2010 = sum(set_rh11_rad_2010) / len(set_rh11_rad_2010)
set_rh12_rad_2010 = set_rh12_2010['rad']
set_rh12media_2010 = sum(set_rh12_rad_2010) / len(set_rh12_rad_2010)
set_rh13_rad_2010 = set_rh13_2010['rad']
set_rh13media_2010 = sum(set_rh13_rad_2010) / len(set_rh13_rad_2010)
set_rh14_rad_2010 = set_rh14_2010['rad']
set_rh14media_2010 = sum(set_rh14_rad_2010) / len(set_rh14_rad_2010)
set_rh15_rad_2010 = set_rh15_2010['rad']
set_rh15media_2010 = sum(set_rh15_rad_2010) / len(set_rh15_rad_2010)
set_rh16_rad_2010 = set_rh16_2010['rad']
set_rh16media_2010 = sum(set_rh16_rad_2010) / len(set_rh16_rad_2010)
set_rh17_rad_2010 = set_rh17_2010['rad']
set_rh17media_2010 = sum(set_rh17_rad_2010) / len(set_rh17_rad_2010)
set_rh18_rad_2010 = set_rh18_2010['rad']
set_rh18media_2010 = sum(set_rh18_rad_2010) / len(set_rh18_rad_2010)
set_rh19_rad_2010 = set_rh19_2010['rad']
set_rh19media_2010 = sum(set_rh19_rad_2010) / len(set_rh19_rad_2010)
set_rh20_rad_2010 = set_rh20_2010['rad']
set_rh20media_2010 = sum(set_rh20_rad_2010) / len(set_rh20_rad_2010)
set_rh21_rad_2010 = set_rh21_2010['rad']
set_rh21media_2010 = sum(set_rh21_rad_2010) / len(set_rh21_rad_2010)
set_rh22_rad_2010 = set_rh22_2010['rad']
set_rh22media_2010 = sum(set_rh22_rad_2010) / len(set_rh22_rad_2010)

###############
#   Outubro   #
###############

out_rh11_rad_2010 = out_rh11_2010['rad']
out_rh11media_2010 = sum(out_rh11_rad_2010) / len(out_rh11_rad_2010)
out_rh12_rad_2010 = out_rh12_2010['rad']
out_rh12media_2010 = sum(out_rh12_rad_2010) / len(out_rh12_rad_2010)
out_rh13_rad_2010 = out_rh13_2010['rad']
out_rh13media_2010 = sum(out_rh13_rad_2010) / len(out_rh13_rad_2010)
out_rh14_rad_2010 = out_rh14_2010['rad']
out_rh14media_2010 = sum(out_rh14_rad_2010) / len(out_rh14_rad_2010)
out_rh15_rad_2010 = out_rh15_2010['rad']
out_rh15media_2010 = sum(out_rh15_rad_2010) / len(out_rh15_rad_2010)
out_rh16_rad_2010 = out_rh16_2010['rad']
out_rh16media_2010 = sum(out_rh16_rad_2010) / len(out_rh16_rad_2010)
out_rh17_rad_2010 = out_rh17_2010['rad']
out_rh17media_2010 = sum(out_rh17_rad_2010) / len(out_rh17_rad_2010)
out_rh18_rad_2010 = out_rh18_2010['rad']
out_rh18media_2010 = sum(out_rh18_rad_2010) / len(out_rh18_rad_2010)
out_rh19_rad_2010 = out_rh19_2010['rad']
out_rh19media_2010 = sum(out_rh19_rad_2010) / len(out_rh19_rad_2010)
out_rh20_rad_2010 = out_rh20_2010['rad']
out_rh20media_2010 = sum(out_rh20_rad_2010) / len(out_rh20_rad_2010)
out_rh21_rad_2010 = out_rh21_2010['rad']
out_rh21media_2010 = sum(out_rh21_rad_2010) / len(out_rh21_rad_2010)
out_rh22_rad_2010 = out_rh22_2010['rad']
out_rh22media_2010 = sum(out_rh22_rad_2010) / len(out_rh22_rad_2010)

################
#   Novembro   #
################

nov_rh11_rad_2010 = nov_rh11_2010['rad']
nov_rh11media_2010 = sum(nov_rh11_rad_2010) / len(nov_rh11_rad_2010)
nov_rh12_rad_2010 = nov_rh12_2010['rad']
nov_rh12media_2010 = sum(nov_rh12_rad_2010) / len(nov_rh12_rad_2010)
nov_rh13_rad_2010 = nov_rh13_2010['rad']
nov_rh13media_2010 = sum(nov_rh13_rad_2010) / len(nov_rh13_rad_2010)
nov_rh14_rad_2010 = nov_rh14_2010['rad']
nov_rh14media_2010 = sum(nov_rh14_rad_2010) / len(nov_rh14_rad_2010)
nov_rh15_rad_2010 = nov_rh15_2010['rad']
nov_rh15media_2010 = sum(nov_rh15_rad_2010) / len(nov_rh15_rad_2010)
nov_rh16_rad_2010 = nov_rh16_2010['rad']
nov_rh16media_2010 = sum(nov_rh16_rad_2010) / len(nov_rh16_rad_2010)
nov_rh17_rad_2010 = nov_rh17_2010['rad']
nov_rh17media_2010 = sum(nov_rh17_rad_2010) / len(nov_rh17_rad_2010)
nov_rh18_rad_2010 = nov_rh18_2010['rad']
nov_rh18media_2010 = sum(nov_rh18_rad_2010) / len(nov_rh18_rad_2010)
nov_rh19_rad_2010 = nov_rh19_2010['rad']
nov_rh19media_2010 = sum(nov_rh19_rad_2010) / len(nov_rh19_rad_2010)
nov_rh20_rad_2010 = nov_rh20_2010['rad']
nov_rh20media_2010 = sum(nov_rh20_rad_2010) / len(nov_rh20_rad_2010)
nov_rh21_rad_2010 = nov_rh21_2010['rad']
nov_rh21media_2010 = sum(nov_rh21_rad_2010) / len(nov_rh21_rad_2010)
nov_rh22_rad_2010 = nov_rh22_2010['rad']
nov_rh22media_2010 = sum(nov_rh22_rad_2010) / len(nov_rh22_rad_2010)

################
#   Dezembro   #
################

dez_rh11_rad_2010 = dez_rh11_2010['rad']
dez_rh11media_2010 = sum(dez_rh11_rad_2010) / len(dez_rh11_rad_2010)
dez_rh12_rad_2010 = dez_rh12_2010['rad']
dez_rh12media_2010 = sum(dez_rh12_rad_2010) / len(dez_rh12_rad_2010)
dez_rh13_rad_2010 = dez_rh13_2010['rad']
dez_rh13media_2010 = sum(dez_rh13_rad_2010) / len(dez_rh13_rad_2010)
dez_rh14_rad_2010 = dez_rh14_2010['rad']
dez_rh14media_2010 = sum(dez_rh14_rad_2010) / len(dez_rh14_rad_2010)
dez_rh15_rad_2010 = dez_rh15_2010['rad']
dez_rh15media_2010 = sum(dez_rh15_rad_2010) / len(dez_rh15_rad_2010)
dez_rh16_rad_2010 = dez_rh16_2010['rad']
dez_rh16media_2010 = sum(dez_rh16_rad_2010) / len(dez_rh16_rad_2010)
dez_rh17_rad_2010 = dez_rh17_2010['rad']
dez_rh17media_2010 = sum(dez_rh17_rad_2010) / len(dez_rh17_rad_2010)
dez_rh18_rad_2010 = dez_rh18_2010['rad']
dez_rh18media_2010 = sum(dez_rh18_rad_2010) / len(dez_rh18_rad_2010)
dez_rh19_rad_2010 = dez_rh19_2010['rad']
dez_rh19media_2010 = sum(dez_rh19_rad_2010) / len(dez_rh19_rad_2010)
dez_rh20_rad_2010 = dez_rh20_2010['rad']
dez_rh20media_2010 = sum(dez_rh20_rad_2010) / len(dez_rh20_rad_2010)
dez_rh21_rad_2010 = dez_rh21_2010['rad']
dez_rh21media_2010 = sum(dez_rh21_rad_2010) / len(dez_rh21_rad_2010)
dez_rh22_rad_2010 = dez_rh22_2010['rad']
dez_rh22media_2010 = sum(dez_rh22_rad_2010) / len(dez_rh22_rad_2010)
dez_rh23_rad_2010 = dez_rh23_2010['rad']
dez_rh23media_2010 = sum(dez_rh23_rad_2010) / len(dez_rh23_rad_2010)

#########################################################
#      Tranformação das matrizes em uma variavel        #
#########################################################
###############
#   Janeiro   #
###############

janrh11media_2010 = float(jan_rh11media_2010)
janrh12media_2010 = float(jan_rh12media_2010)
janrh13media_2010 = float(jan_rh13media_2010)
janrh14media_2010 = float(jan_rh14media_2010)
janrh15media_2010 = float(jan_rh15media_2010)
janrh16media_2010 = float(jan_rh16media_2010)
janrh17media_2010 = float(jan_rh17media_2010)
janrh18media_2010 = float(jan_rh18media_2010)
janrh19media_2010 = float(jan_rh19media_2010)
janrh20media_2010 = float(jan_rh20media_2010)
janrh21media_2010 = float(jan_rh21media_2010)
janrh22media_2010 = float(jan_rh22media_2010)
jan_2010 = [janrh11media_2010, janrh12media_2010, janrh13media_2010, janrh14media_2010, janrh15media_2010,
            janrh16media_2010, janrh17media_2010, janrh18media_2010, janrh19media_2010, janrh20media_2010,
            janrh21media_2010, janrh22media_2010]

#################
#   Fevereiro   #
#################

fevrh11media_2010 = float(fev_rh11media_2010)
fevrh12media_2010 = float(fev_rh12media_2010)
fevrh13media_2010 = float(fev_rh13media_2010)
fevrh14media_2010 = float(fev_rh14media_2010)
fevrh15media_2010 = float(fev_rh15media_2010)
fevrh16media_2010 = float(fev_rh16media_2010)
fevrh17media_2010 = float(fev_rh17media_2010)
fevrh18media_2010 = float(fev_rh18media_2010)
fevrh19media_2010 = float(fev_rh19media_2010)
fevrh20media_2010 = float(fev_rh20media_2010)
fevrh21media_2010 = float(fev_rh21media_2010)
fevrh22media_2010 = float(fev_rh22media_2010)
fev_2010 = [fevrh11media_2010, fevrh12media_2010, fevrh13media_2010, fevrh14media_2010, fevrh15media_2010,
            fevrh16media_2010, fevrh17media_2010, fevrh18media_2010, fevrh19media_2010, fevrh20media_2010,
            fevrh21media_2010, fevrh22media_2010]

###############
#   Março     #
###############

marrh11media_2010 = float(mar_rh11media_2010)
marrh12media_2010 = float(mar_rh12media_2010)
marrh13media_2010 = float(mar_rh13media_2010)
marrh14media_2010 = float(mar_rh14media_2010)
marrh15media_2010 = float(mar_rh15media_2010)
marrh16media_2010 = float(mar_rh16media_2010)
marrh17media_2010 = float(mar_rh17media_2010)
marrh18media_2010 = float(mar_rh18media_2010)
marrh19media_2010 = float(mar_rh19media_2010)
marrh20media_2010 = float(mar_rh20media_2010)
marrh21media_2010 = float(mar_rh21media_2010)
marrh22media_2010 = float(mar_rh22media_2010)
mar_2010 = [marrh11media_2010, marrh12media_2010, marrh13media_2010, marrh14media_2010, marrh15media_2010,
            marrh16media_2010, marrh17media_2010, marrh18media_2010, marrh19media_2010, marrh20media_2010,
            marrh21media_2010,
            marrh22media_2010]

#############
#   Abril   #
#############

abrrh11media_2010 = float(abr_rh11media_2010)
abrrh12media_2010 = float(abr_rh12media_2010)
abrrh13media_2010 = float(abr_rh13media_2010)
abrrh14media_2010 = float(abr_rh14media_2010)
abrrh15media_2010 = float(abr_rh15media_2010)
abrrh16media_2010 = float(abr_rh16media_2010)
abrrh17media_2010 = float(abr_rh17media_2010)
abrrh18media_2010 = float(abr_rh18media_2010)
abrrh19media_2010 = float(abr_rh19media_2010)
abrrh20media_2010 = float(abr_rh20media_2010)
abrrh21media_2010 = float(abr_rh21media_2010)
abrrh22media_2010 = float(abr_rh22media_2010)
abr_2010 = [abrrh11media_2010, abrrh12media_2010, abrrh13media_2010, abrrh14media_2010, abrrh15media_2010,
            abrrh16media_2010, abrrh17media_2010, abrrh18media_2010, abrrh19media_2010, abrrh20media_2010,
            abrrh21media_2010,
            abrrh22media_2010]

############
#   Maio   #
############

mairh11media_2010 = float(mai_rh11media_2010)
mairh12media_2010 = float(mai_rh12media_2010)
mairh13media_2010 = float(mai_rh13media_2010)
mairh14media_2010 = float(mai_rh14media_2010)
mairh15media_2010 = float(mai_rh15media_2010)
mairh16media_2010 = float(mai_rh16media_2010)
mairh17media_2010 = float(mai_rh17media_2010)
mairh18media_2010 = float(mai_rh18media_2010)
mairh19media_2010 = float(mai_rh19media_2010)
mairh20media_2010 = float(mai_rh20media_2010)
mairh21media_2010 = float(mai_rh21media_2010)
mairh22media_2010 = float(mai_rh22media_2010)
mai_2010 = [mairh11media_2010, mairh12media_2010, mairh13media_2010, mairh14media_2010, mairh15media_2010,
            mairh16media_2010, mairh17media_2010, mairh18media_2010, mairh19media_2010, mairh20media_2010,
            mairh21media_2010,
            mairh22media_2010]

#############
#   Junho   #
#############

junrh11media_2010 = float(jun_rh11media_2010)
junrh12media_2010 = float(jun_rh12media_2010)
junrh13media_2010 = float(jun_rh13media_2010)
junrh14media_2010 = float(jun_rh14media_2010)
junrh15media_2010 = float(jun_rh15media_2010)
junrh16media_2010 = float(jun_rh16media_2010)
junrh17media_2010 = float(jun_rh17media_2010)
junrh18media_2010 = float(jun_rh18media_2010)
junrh19media_2010 = float(jun_rh19media_2010)
junrh20media_2010 = float(jun_rh20media_2010)
junrh21media_2010 = float(jun_rh21media_2010)
junrh22media_2010 = float(jun_rh22media_2010)
jun_2010 = [junrh11media_2010, junrh12media_2010, junrh13media_2010, junrh14media_2010, junrh15media_2010,
            junrh16media_2010, junrh17media_2010, junrh18media_2010, junrh19media_2010, junrh20media_2010,
            junrh21media_2010,
            junrh22media_2010]

#############
#   Julho   #
#############

julrh11media_2010 = float(jul_rh11media_2010)
julrh12media_2010 = float(jul_rh12media_2010)
julrh13media_2010 = float(jul_rh13media_2010)
julrh14media_2010 = float(jul_rh14media_2010)
julrh15media_2010 = float(jul_rh15media_2010)
julrh16media_2010 = float(jul_rh16media_2010)
julrh17media_2010 = float(jul_rh17media_2010)
julrh18media_2010 = float(jul_rh18media_2010)
julrh19media_2010 = float(jul_rh19media_2010)
julrh20media_2010 = float(jul_rh20media_2010)
julrh21media_2010 = float(jul_rh21media_2010)
julrh22media_2010 = float(jul_rh22media_2010)

jul_2010 = [julrh11media_2010, julrh12media_2010, julrh13media_2010, julrh14media_2010, julrh15media_2010,
            julrh16media_2010, julrh17media_2010, julrh18media_2010, julrh19media_2010, julrh20media_2010,
            julrh21media_2010,
            julrh22media_2010]

##############
#   Agosto   #
##############

agorh11media_2010 = float(ago_rh11media_2010)
agorh12media_2010 = float(ago_rh12media_2010)
agorh13media_2010 = float(ago_rh13media_2010)
agorh14media_2010 = float(ago_rh14media_2010)
agorh15media_2010 = float(ago_rh15media_2010)
agorh16media_2010 = float(ago_rh16media_2010)
agorh17media_2010 = float(ago_rh17media_2010)
agorh18media_2010 = float(ago_rh18media_2010)
agorh19media_2010 = float(ago_rh19media_2010)
agorh20media_2010 = float(ago_rh20media_2010)
agorh21media_2010 = float(ago_rh21media_2010)
agorh22media_2010 = float(ago_rh22media_2010)
ago_2010 = [agorh11media_2010, agorh12media_2010, agorh13media_2010, agorh14media_2010, agorh15media_2010,
            agorh16media_2010, agorh17media_2010, agorh18media_2010, agorh19media_2010, agorh20media_2010,
            agorh21media_2010,
            agorh22media_2010]

################
#   Setembro   #
################

setrh11media_2010 = float(set_rh11media_2010)
setrh12media_2010 = float(set_rh12media_2010)
setrh13media_2010 = float(set_rh13media_2010)
setrh14media_2010 = float(set_rh14media_2010)
setrh15media_2010 = float(set_rh15media_2010)
setrh16media_2010 = float(set_rh16media_2010)
setrh17media_2010 = float(set_rh17media_2010)
setrh18media_2010 = float(set_rh18media_2010)
setrh19media_2010 = float(set_rh19media_2010)
setrh20media_2010 = float(set_rh20media_2010)
setrh21media_2010 = float(set_rh21media_2010)
setrh22media_2010 = float(set_rh22media_2010)
set_2010 = [setrh11media_2010, setrh12media_2010, setrh13media_2010, setrh14media_2010, setrh15media_2010,
            setrh16media_2010, setrh17media_2010, setrh18media_2010, setrh19media_2010, setrh20media_2010,
            setrh21media_2010,
            setrh22media_2010]

###############
#   Outubro   #
###############

outrh11media_2010 = float(out_rh11media_2010)
outrh12media_2010 = float(out_rh12media_2010)
outrh13media_2010 = float(out_rh13media_2010)
outrh14media_2010 = float(out_rh14media_2010)
outrh15media_2010 = float(out_rh15media_2010)
outrh16media_2010 = float(out_rh16media_2010)
outrh17media_2010 = float(out_rh17media_2010)
outrh18media_2010 = float(out_rh18media_2010)
outrh19media_2010 = float(out_rh19media_2010)
outrh20media_2010 = float(out_rh20media_2010)
outrh21media_2010 = float(out_rh21media_2010)
outrh22media_2010 = float(out_rh22media_2010)
out_2010 = [outrh11media_2010, outrh12media_2010, outrh13media_2010, outrh14media_2010, outrh15media_2010,
            outrh16media_2010, outrh17media_2010, outrh18media_2010, outrh19media_2010, outrh20media_2010,
            outrh21media_2010,
            outrh22media_2010]

################
#   Novembro   #
################

novrh11media_2010 = float(nov_rh11media_2010)
novrh12media_2010 = float(nov_rh12media_2010)
novrh13media_2010 = float(nov_rh13media_2010)
novrh14media_2010 = float(nov_rh14media_2010)
novrh15media_2010 = float(nov_rh15media_2010)
novrh16media_2010 = float(nov_rh16media_2010)
novrh17media_2010 = float(nov_rh17media_2010)
novrh18media_2010 = float(nov_rh18media_2010)
novrh19media_2010 = float(nov_rh19media_2010)
novrh20media_2010 = float(nov_rh20media_2010)
novrh21media_2010 = float(nov_rh21media_2010)
novrh22media_2010 = float(nov_rh22media_2010)

nov_2010 = [novrh11media_2010, novrh12media_2010, novrh13media_2010, novrh14media_2010, novrh15media_2010,
            novrh16media_2010, novrh17media_2010, novrh18media_2010, novrh19media_2010, novrh20media_2010,
            novrh21media_2010,
            novrh22media_2010]

################
#   Dezembro   #
################

dezrh11media_2010 = float(dez_rh11media_2010)
dezrh12media_2010 = float(dez_rh12media_2010)
dezrh13media_2010 = float(dez_rh13media_2010)
dezrh14media_2010 = float(dez_rh14media_2010)
dezrh15media_2010 = float(dez_rh15media_2010)
dezrh16media_2010 = float(dez_rh16media_2010)
dezrh17media_2010 = float(dez_rh17media_2010)
dezrh18media_2010 = float(dez_rh18media_2010)
dezrh19media_2010 = float(dez_rh19media_2010)
dezrh20media_2010 = float(dez_rh20media_2010)
dezrh21media_2010 = float(dez_rh21media_2010)
dezrh22media_2010 = float(dez_rh22media_2010)
dez_2010 = [dezrh11media_2010, dezrh12media_2010, dezrh13media_2010, dezrh14media_2010, dezrh15media_2010,
            dezrh16media_2010, dezrh17media_2010, dezrh18media_2010, dezrh19media_2010, dezrh20media_2010,
            dezrh21media_2010, dezrh22media_2010]

########################################
#      Calculo do Desvio Padrão        #
########################################
###############
#   Janeiro   #
###############

djan_h11_2010 = np.std(jan_rh11_rad_2010)
djan_h12_2010 = np.std(jan_rh12_rad_2010)
djan_h13_2010 = np.std(jan_rh13_rad_2010)
djan_h14_2010 = np.std(jan_rh14_rad_2010)
djan_h15_2010 = np.std(jan_rh15_rad_2010)
djan_h16_2010 = np.std(jan_rh16_rad_2010)
djan_h17_2010 = np.std(jan_rh17_rad_2010)
djan_h18_2010 = np.std(jan_rh18_rad_2010)
djan_h19_2010 = np.std(jan_rh19_rad_2010)
djan_h20_2010 = np.std(jan_rh20_rad_2010)
djan_h21_2010 = np.std(jan_rh21_rad_2010)
djan_h22_2010 = np.std(jan_rh22_rad_2010)

djan_2010 = [djan_h11_2010, djan_h12_2010, djan_h13_2010, djan_h14_2010, djan_h15_2010, djan_h16_2010, djan_h17_2010,
             djan_h18_2010, djan_h19_2010, djan_h20_2010, djan_h21_2010, djan_h22_2010]

#################
#   Fevereiro   #
#################

dfev_h11_2010 = np.std(fev_rh11_rad_2010)
dfev_h12_2010 = np.std(fev_rh12_rad_2010)
dfev_h13_2010 = np.std(fev_rh13_rad_2010)
dfev_h14_2010 = np.std(fev_rh14_rad_2010)
dfev_h15_2010 = np.std(fev_rh15_rad_2010)
dfev_h16_2010 = np.std(fev_rh16_rad_2010)
dfev_h17_2010 = np.std(fev_rh17_rad_2010)
dfev_h18_2010 = np.std(fev_rh18_rad_2010)
dfev_h19_2010 = np.std(fev_rh19_rad_2010)
dfev_h20_2010 = np.std(fev_rh20_rad_2010)
dfev_h21_2010 = np.std(fev_rh21_rad_2010)
dfev_h22_2010 = np.std(fev_rh22_rad_2010)

dfev_2010 = [dfev_h11_2010, dfev_h12_2010, dfev_h13_2010, dfev_h14_2010, dfev_h15_2010, dfev_h16_2010, dfev_h17_2010,
             dfev_h18_2010, dfev_h19_2010, dfev_h20_2010, dfev_h21_2010, dfev_h22_2010]

###############
#   Março     #
###############

dmar_h11_2010 = np.std(mar_rh11_rad_2010)
dmar_h12_2010 = np.std(mar_rh12_rad_2010)
dmar_h13_2010 = np.std(mar_rh13_rad_2010)
dmar_h14_2010 = np.std(mar_rh14_rad_2010)
dmar_h15_2010 = np.std(mar_rh15_rad_2010)
dmar_h16_2010 = np.std(mar_rh16_rad_2010)
dmar_h17_2010 = np.std(mar_rh17_rad_2010)
dmar_h18_2010 = np.std(mar_rh18_rad_2010)
dmar_h19_2010 = np.std(mar_rh19_rad_2010)
dmar_h20_2010 = np.std(mar_rh20_rad_2010)
dmar_h21_2010 = np.std(mar_rh21_rad_2010)
dmar_h22_2010 = np.std(mar_rh22_rad_2010)


dmar_2010 = [dmar_h11_2010, dmar_h12_2010, dmar_h13_2010, dmar_h14_2010, dmar_h15_2010, dmar_h16_2010, dmar_h17_2010,
             dmar_h18_2010, dmar_h19_2010, dmar_h20_2010, dmar_h21_2010, dmar_h22_2010]

#############
#   Abril   #
#############

dabr_h11_2010 = np.std(abr_rh11_rad_2010)
dabr_h12_2010 = np.std(abr_rh12_rad_2010)
dabr_h13_2010 = np.std(abr_rh13_rad_2010)
dabr_h14_2010 = np.std(abr_rh14_rad_2010)
dabr_h15_2010 = np.std(abr_rh15_rad_2010)
dabr_h16_2010 = np.std(abr_rh16_rad_2010)
dabr_h17_2010 = np.std(abr_rh17_rad_2010)
dabr_h18_2010 = np.std(abr_rh18_rad_2010)
dabr_h19_2010 = np.std(abr_rh19_rad_2010)
dabr_h20_2010 = np.std(abr_rh20_rad_2010)
dabr_h21_2010 = np.std(abr_rh21_rad_2010)
dabr_h22_2010 = np.std(abr_rh22_rad_2010)

dabr_2010 = [dabr_h11_2010, dabr_h12_2010, dabr_h13_2010, dabr_h14_2010, dabr_h15_2010, dabr_h16_2010, dabr_h17_2010,
             dabr_h18_2010, dabr_h19_2010, dabr_h20_2010, dabr_h21_2010, dabr_h22_2010]

############
#   Maio   #
############

dmai_h11_2010 = np.std(mai_rh11_rad_2010)
dmai_h12_2010 = np.std(mai_rh12_rad_2010)
dmai_h13_2010 = np.std(mai_rh13_rad_2010)
dmai_h14_2010 = np.std(mai_rh14_rad_2010)
dmai_h15_2010 = np.std(mai_rh15_rad_2010)
dmai_h16_2010 = np.std(mai_rh16_rad_2010)
dmai_h17_2010 = np.std(mai_rh17_rad_2010)
dmai_h18_2010 = np.std(mai_rh18_rad_2010)
dmai_h19_2010 = np.std(mai_rh19_rad_2010)
dmai_h20_2010 = np.std(mai_rh20_rad_2010)
dmai_h21_2010 = np.std(mai_rh21_rad_2010)
dmai_h22_2010 = np.std(mai_rh22_rad_2010)

dmai_2010 = [dmai_h11_2010, dmai_h12_2010, dmai_h13_2010, dmai_h14_2010, dmai_h15_2010, dmai_h16_2010, dmai_h17_2010,
             dmai_h18_2010, dmai_h19_2010, dmai_h20_2010, dmai_h21_2010, dmai_h22_2010]

#############
#   Junho   #
#############

djun_h11_2010 = np.std(jun_rh11_rad_2010)
djun_h12_2010 = np.std(jun_rh12_rad_2010)
djun_h13_2010 = np.std(jun_rh13_rad_2010)
djun_h14_2010 = np.std(jun_rh14_rad_2010)
djun_h15_2010 = np.std(jun_rh15_rad_2010)
djun_h16_2010 = np.std(jun_rh16_rad_2010)
djun_h17_2010 = np.std(jun_rh17_rad_2010)
djun_h18_2010 = np.std(jun_rh18_rad_2010)
djun_h19_2010 = np.std(jun_rh19_rad_2010)
djun_h20_2010 = np.std(jun_rh20_rad_2010)
djun_h21_2010 = np.std(jun_rh21_rad_2010)
djun_h22_2010 = np.std(jun_rh22_rad_2010)

djun_2010 = [djun_h11_2010, djun_h12_2010, djun_h13_2010, djun_h14_2010, djun_h15_2010, djun_h16_2010, djun_h17_2010,
             djun_h18_2010, djun_h19_2010, djun_h20_2010, djun_h21_2010, djun_h22_2010]

#############
#   Julho   #
#############

djul_h11_2010 = np.std(jul_rh11_rad_2010)
djul_h12_2010 = np.std(jul_rh12_rad_2010)
djul_h13_2010 = np.std(jul_rh13_rad_2010)
djul_h14_2010 = np.std(jul_rh14_rad_2010)
djul_h15_2010 = np.std(jul_rh15_rad_2010)
djul_h16_2010 = np.std(jul_rh16_rad_2010)
djul_h17_2010 = np.std(jul_rh17_rad_2010)
djul_h18_2010 = np.std(jul_rh18_rad_2010)
djul_h19_2010 = np.std(jul_rh19_rad_2010)
djul_h20_2010 = np.std(jul_rh20_rad_2010)
djul_h21_2010 = np.std(jul_rh21_rad_2010)
djul_h22_2010 = np.std(jul_rh22_rad_2010)

djul_2010 = [djul_h11_2010, djul_h12_2010, djul_h13_2010, djul_h14_2010, djul_h15_2010, djul_h16_2010, djul_h17_2010,
             djul_h18_2010, djul_h19_2010, djul_h20_2010, djul_h21_2010, djul_h22_2010]

##############
#   Agosto   #
##############

dago_h11_2010 = np.std(ago_rh11_rad_2010)
dago_h12_2010 = np.std(ago_rh12_rad_2010)
dago_h13_2010 = np.std(ago_rh13_rad_2010)
dago_h14_2010 = np.std(ago_rh14_rad_2010)
dago_h15_2010 = np.std(ago_rh15_rad_2010)
dago_h16_2010 = np.std(ago_rh16_rad_2010)
dago_h17_2010 = np.std(ago_rh17_rad_2010)
dago_h18_2010 = np.std(ago_rh18_rad_2010)
dago_h19_2010 = np.std(ago_rh19_rad_2010)
dago_h20_2010 = np.std(ago_rh20_rad_2010)
dago_h21_2010 = np.std(ago_rh21_rad_2010)
dago_h22_2010 = np.std(ago_rh22_rad_2010)

dago_2010 = [dago_h11_2010, dago_h12_2010, dago_h13_2010, dago_h14_2010, dago_h15_2010, dago_h16_2010, dago_h17_2010,
             dago_h18_2010, dago_h19_2010, dago_h20_2010, dago_h21_2010, dago_h22_2010]

################
#   Setembro   #
################

dset_h11_2010 = np.std(set_rh11_rad_2010)
dset_h12_2010 = np.std(set_rh12_rad_2010)
dset_h13_2010 = np.std(set_rh13_rad_2010)
dset_h14_2010 = np.std(set_rh14_rad_2010)
dset_h15_2010 = np.std(set_rh15_rad_2010)
dset_h16_2010 = np.std(set_rh16_rad_2010)
dset_h17_2010 = np.std(set_rh17_rad_2010)
dset_h18_2010 = np.std(set_rh18_rad_2010)
dset_h19_2010 = np.std(set_rh19_rad_2010)
dset_h20_2010 = np.std(set_rh20_rad_2010)
dset_h21_2010 = np.std(set_rh21_rad_2010)
dset_h22_2010 = np.std(set_rh22_rad_2010)

dset_2010 = [dset_h11_2010, dset_h12_2010, dset_h13_2010, dset_h14_2010, dset_h15_2010, dset_h16_2010, dset_h17_2010,
             dset_h18_2010, dset_h19_2010, dset_h20_2010, dset_h21_2010, dset_h22_2010]

###############
#   Outubro   #
###############

dout_h11_2010 = np.std(out_rh11_rad_2010)
dout_h12_2010 = np.std(out_rh12_rad_2010)
dout_h13_2010 = np.std(out_rh13_rad_2010)
dout_h14_2010 = np.std(out_rh14_rad_2010)
dout_h15_2010 = np.std(out_rh15_rad_2010)
dout_h16_2010 = np.std(out_rh16_rad_2010)
dout_h17_2010 = np.std(out_rh17_rad_2010)
dout_h18_2010 = np.std(out_rh18_rad_2010)
dout_h19_2010 = np.std(out_rh19_rad_2010)
dout_h20_2010 = np.std(out_rh20_rad_2010)
dout_h21_2010 = np.std(out_rh21_rad_2010)
dout_h22_2010 = np.std(out_rh22_rad_2010)


dout_2010 = [dout_h11_2010, dout_h12_2010, dout_h13_2010, dout_h14_2010, dout_h15_2010, dout_h16_2010, dout_h17_2010,
             dout_h18_2010, dout_h19_2010, dout_h20_2010, dout_h21_2010, dout_h22_2010]

################
#   Novembro   #
################

dnov_h11_2010 = np.std(nov_rh11_rad_2010)
dnov_h12_2010 = np.std(nov_rh12_rad_2010)
dnov_h13_2010 = np.std(nov_rh13_rad_2010)
dnov_h14_2010 = np.std(nov_rh14_rad_2010)
dnov_h15_2010 = np.std(nov_rh15_rad_2010)
dnov_h16_2010 = np.std(nov_rh16_rad_2010)
dnov_h17_2010 = np.std(nov_rh17_rad_2010)
dnov_h18_2010 = np.std(nov_rh18_rad_2010)
dnov_h19_2010 = np.std(nov_rh19_rad_2010)
dnov_h20_2010 = np.std(nov_rh20_rad_2010)
dnov_h21_2010 = np.std(nov_rh21_rad_2010)
dnov_h22_2010 = np.std(nov_rh22_rad_2010)

dnov_2010 = [dnov_h11_2010, dnov_h12_2010, dnov_h13_2010, dnov_h14_2010, dnov_h15_2010, dnov_h16_2010, dnov_h17_2010,
             dnov_h18_2010, dnov_h19_2010, dnov_h20_2010, dnov_h21_2010, dnov_h22_2010]

################
#   Dezembro   #
################

ddez_h11_2010 = np.std(dez_rh11_rad_2010)
ddez_h12_2010 = np.std(dez_rh12_rad_2010)
ddez_h13_2010 = np.std(dez_rh13_rad_2010)
ddez_h14_2010 = np.std(dez_rh14_rad_2010)
ddez_h15_2010 = np.std(dez_rh15_rad_2010)
ddez_h16_2010 = np.std(dez_rh16_rad_2010)
ddez_h17_2010 = np.std(dez_rh17_rad_2010)
ddez_h18_2010 = np.std(dez_rh18_rad_2010)
ddez_h19_2010 = np.std(dez_rh19_rad_2010)
ddez_h20_2010 = np.std(dez_rh20_rad_2010)
ddez_h21_2010 = np.std(dez_rh21_rad_2010)
ddez_h22_2010 = np.std(dez_rh22_rad_2010)

ddez_2010 = [ddez_h11_2010, ddez_h12_2010, ddez_h13_2010, ddez_h14_2010, ddez_h15_2010, ddez_h16_2010, ddez_h17_2010,
             ddez_h18_2010, ddez_h19_2010, ddez_h20_2010, ddez_h21_2010, ddez_h22_2010]

########################################
#             Média Anual              #
########################################
mrh11_2010 = [jan_rh11media_2010, fev_rh11media_2010, mar_rh11media_2010, abr_rh11media_2010, mai_rh11media_2010, jun_rh11media_2010,
              jul_rh11media_2010, ago_rh11media_2010, set_rh11media_2010, out_rh11media_2010, nov_rh11media_2010, dez_rh11media_2010]
mmrh11_2020 = sum(mrh11_2010) / len(mrh11_2010)

mrh12_2010 = [jan_rh12media_2010, fev_rh12media_2010, mar_rh12media_2010, abr_rh12media_2010, mai_rh12media_2010, jun_rh12media_2010,
              jul_rh12media_2010, ago_rh12media_2010, set_rh12media_2010, out_rh12media_2010, nov_rh12media_2010, dez_rh12media_2010]
mmrh12_2020 = sum(mrh12_2010) / len(mrh12_2010)

mrh13_2010 = [jan_rh13media_2010, fev_rh13media_2010, mar_rh13media_2010, abr_rh13media_2010, mai_rh13media_2010, jun_rh13media_2010,
              jul_rh13media_2010, ago_rh13media_2010, set_rh13media_2010, out_rh13media_2010, nov_rh13media_2010, dez_rh13media_2010]
mmrh13_2020 = sum(mrh13_2010) / len(mrh13_2010)

mrh14_2010 = [jan_rh14media_2010, fev_rh14media_2010, mar_rh14media_2010, abr_rh14media_2010, mai_rh14media_2010, jun_rh14media_2010,
              jul_rh14media_2010, ago_rh14media_2010, set_rh14media_2010, out_rh14media_2010, nov_rh14media_2010, dez_rh14media_2010]
mmrh14_2010 = sum(mrh14_2010) / len(mrh14_2010)

mrh15_2010 = [jan_rh15media_2010, fev_rh15media_2010, mar_rh15media_2010, abr_rh15media_2010, mai_rh15media_2010, jun_rh15media_2010,
              jul_rh15media_2010, ago_rh15media_2010, set_rh15media_2010, out_rh15media_2010, nov_rh15media_2010, dez_rh15media_2010]
mmrh15_2010 = sum(mrh15_2010) / len(mrh15_2010)

mrh16_2010 = [jan_rh16media_2010, fev_rh16media_2010, mar_rh16media_2010, abr_rh16media_2010, mai_rh16media_2010, jun_rh16media_2010,
              jul_rh16media_2010, ago_rh16media_2010, set_rh16media_2010, out_rh16media_2010, nov_rh16media_2010, dez_rh16media_2010]
mmrh16_2010 = sum(mrh16_2010) / len(mrh16_2010)

mrh17_2010 = [jan_rh17media_2010, fev_rh17media_2010, mar_rh17media_2010, abr_rh17media_2010, mai_rh17media_2010, jun_rh17media_2010,
              jul_rh17media_2010, ago_rh17media_2010, set_rh17media_2010, out_rh17media_2010, nov_rh17media_2010, dez_rh17media_2010]
mmrh17_2010 = sum(mrh17_2010) / len(mrh17_2010)

mrh18_2010 = [jan_rh18media_2010, fev_rh18media_2010, mar_rh18media_2010, abr_rh18media_2010, mai_rh18media_2010, jun_rh18media_2010,
              jul_rh18media_2010, ago_rh18media_2010, set_rh18media_2010, out_rh18media_2010, nov_rh18media_2010, dez_rh18media_2010]
mmrh18_2010 = sum(mrh18_2010) / len(mrh18_2010)

mrh19_2010 = [jan_rh19media_2010, fev_rh19media_2010, mar_rh19media_2010, abr_rh19media_2010, mai_rh19media_2010, jun_rh19media_2010,
              jul_rh19media_2010, ago_rh19media_2010, set_rh19media_2010, out_rh19media_2010, nov_rh19media_2010, dez_rh19media_2010]
mmrh19_2010 = sum(mrh19_2010) / len(mrh19_2010)

mrh20_2010 = [jan_rh20media_2010, fev_rh20media_2010, mar_rh20media_2010, abr_rh20media_2010, mai_rh20media_2010, jun_rh20media_2010,
              jul_rh20media_2010, ago_rh20media_2010, set_rh20media_2010, out_rh20media_2010, nov_rh20media_2010, dez_rh20media_2010]
mmrh20_2010 = sum(mrh20_2010) / len(mrh20_2010)

mrh21_2010 = [jan_rh21media_2010, fev_rh21media_2010, mar_rh21media_2010, abr_rh21media_2010, mai_rh21media_2010, jun_rh21media_2010,
              jul_rh21media_2010, ago_rh21media_2010, set_rh21media_2010, out_rh21media_2010, nov_rh21media_2010, dez_rh21media_2010]
mmrh21_2010 = sum(mrh21_2010) / len(mrh21_2010)

mrh22_2010 = [jan_rh22media_2010, fev_rh22media_2010, mar_rh22media_2010, abr_rh22media_2010, mai_rh22media_2010, jun_rh22media_2010,
              jul_rh22media_2010, ago_rh22media_2010, set_rh22media_2010, out_rh22media_2010, nov_rh22media_2010, dez_rh22media_2010]
mmrh22_2010 = sum(mrh22_2010) / len(mrh22_2010)

########################################
#            Desvio anual              #
########################################
dmrh11_2010 = [djan_h11_2010, dfev_h11_2010, dmar_h11_2010, dabr_h11_2010, dmai_h11_2010, djun_h11_2010, djul_h11_2010, dago_h11_2010, dset_h11_2010,
               dout_h11_2010, dnov_h11_2010, ddez_h11_2010]
ddmrh11_2020 = sum(dmrh11_2010) / len(dmrh11_2010)

dmrh12_2010 = [djan_h12_2010, dfev_h12_2010, dmar_h12_2010, dabr_h12_2010, dmai_h12_2010, djun_h12_2010, djul_h12_2010, dago_h12_2010, dset_h12_2010,
               dout_h12_2010, dnov_h12_2010, ddez_h12_2010]
ddmrh12_2020 = sum(dmrh12_2010) / len(dmrh12_2010)

dmrh13_2010 = [djan_h13_2010, dfev_h13_2010, dmar_h13_2010, dabr_h13_2010, dmai_h13_2010, djun_h13_2010, djul_h13_2010, dago_h13_2010, dset_h13_2010,
               dout_h13_2010, dnov_h13_2010, ddez_h13_2010]
ddmrh13_2020 = sum(dmrh13_2010) / len(dmrh13_2010)

dmrh14_2010 = [djan_h14_2010, dfev_h14_2010, dmar_h14_2010, dabr_h14_2010, dmai_h14_2010, djun_h14_2010, djul_h14_2010, dago_h14_2010, dset_h14_2010,
               dout_h14_2010, dnov_h14_2010, ddez_h14_2010]
ddmrh14_2020 = sum(dmrh14_2010) / len(dmrh14_2010)

dmrh15_2010 = [djan_h15_2010, dfev_h15_2010, dmar_h15_2010, dabr_h15_2010, dmai_h15_2010, djun_h15_2010, djul_h15_2010, dago_h15_2010, dset_h15_2010,
               dout_h15_2010, dnov_h15_2010, ddez_h15_2010]
ddmrh15_2020 = sum(dmrh15_2010) / len(dmrh15_2010)

dmrh16_2010 = [djan_h16_2010, dfev_h16_2010, dmar_h16_2010, dabr_h16_2010, dmai_h16_2010, djun_h16_2010, djul_h16_2010, dago_h16_2010, dset_h16_2010,
               dout_h16_2010, dnov_h16_2010, ddez_h16_2010]
ddmrh16_2020 = sum(dmrh16_2010) / len(dmrh16_2010)

dmrh17_2010 = [djan_h17_2010, dfev_h17_2010, dmar_h17_2010, dabr_h17_2010, dmai_h17_2010, djun_h17_2010, djul_h17_2010, dago_h17_2010, dset_h17_2010,
               dout_h17_2010, dnov_h17_2010, ddez_h17_2010]
ddmrh17_2020 = sum(dmrh17_2010) / len(dmrh17_2010)

dmrh18_2010 = [djan_h18_2010, dfev_h18_2010, dmar_h18_2010, dabr_h18_2010, dmai_h18_2010, djun_h18_2010, djul_h18_2010, dago_h18_2010, dset_h18_2010,
               dout_h18_2010, dnov_h18_2010, ddez_h18_2010]
ddmrh18_2020 = sum(dmrh18_2010) / len(dmrh18_2010)

dmrh19_2010 = [djan_h19_2010, dfev_h19_2010, dmar_h19_2010, dabr_h19_2010, dmai_h19_2010, djun_h19_2010, djul_h19_2010, dago_h19_2010, dset_h19_2010,
               dout_h19_2010, dnov_h19_2010, ddez_h19_2010]
ddmrh19_2020 = sum(dmrh19_2010) / len(dmrh19_2010)

dmrh20_2010 = [djan_h20_2010, dfev_h20_2010, dmar_h20_2010, dabr_h20_2010, dmai_h20_2010, djun_h20_2010, djul_h20_2010, dago_h20_2010, dset_h20_2010,
               dout_h20_2010, dnov_h20_2010, ddez_h20_2010]
ddmrh20_2020 = sum(dmrh20_2010) / len(dmrh20_2010)

dmrh21_2010 = [djan_h21_2010, dfev_h21_2010, dmar_h21_2010, dabr_h21_2010, dmai_h21_2010, djun_h21_2010, djul_h21_2010, dago_h21_2010, dset_h21_2010,
               dout_h21_2010, dnov_h21_2010, ddez_h21_2010]
ddmrh21_2020 = sum(dmrh21_2010) / len(dmrh21_2010)

dmrh22_2010 = [djan_h22_2010, dfev_h22_2010, dmar_h22_2010, dabr_h22_2010, dmai_h22_2010, djun_h22_2010, djul_h22_2010, dago_h22_2010, dset_h22_2010,
               dout_h22_2010, dnov_h22_2010, ddez_h22_2010]
ddmrh22_2020 = sum(dmrh22_2010) / len(dmrh22_2010)

mediatotal_2010 = [mmrh11_2020, mmrh12_2020, mmrh13_2020, mmrh14_2010, mmrh15_2010, mmrh16_2010, mmrh17_2010, mmrh18_2010, mmrh19_2010, mmrh20_2010,
                   mmrh21_2010, mmrh22_2010]
desviototal_2010 = [ddmrh11_2020, ddmrh12_2020, ddmrh13_2020, ddmrh14_2020, ddmrh15_2020, ddmrh16_2020, ddmrh17_2020, ddmrh18_2020, ddmrh19_2020,
                    ddmrh20_2020, ddmrh21_2020, ddmrh22_2020]

########################################
#         Plotagem de Gráfico          #
########################################

###############
#   Janeiro   #
###############

horas = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
fig = plt.figure(figsize=(12, 8))
plt.bar(horas, jan_2010, yerr=djan_2010, capsize=5)
plt.xlabel('Horas(UTC)')
plt.ylabel('Radiação (J/m^2)')
plt.title(
    'Radiação média e desvio padrão da região do Bolsão no mês de janeiro de 2010')
plt.savefig(r'C:\Users\igorb\OneDrive\Desktop\Projetos\ESTAÇÃO_METEOROLÓGICA\Rad_MS_2010_2020\Regiões\Bolsão\2010\\Jan_2010.png')
plt.close()

#################
#   Fevereiro   #
#################

horas = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
fig = plt.figure(figsize=(12, 8))
plt.bar(horas, fev_2010, yerr=dfev_2010, capsize=5)
plt.xlabel('Horas(UTC)')
plt.ylabel('Radiação (J/m^2)')
plt.title(
    'Radiação média e desvio padrão da região do Bolsão no mês de fevereiro de 2010')
plt.savefig(r'C:\Users\igorb\OneDrive\Desktop\Projetos\ESTAÇÃO_METEOROLÓGICA\Rad_MS_2010_2020\Regiões\Bolsão\2010\\fev_2010.png')
plt.close()

###############
#   Março     #
###############

horas = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
fig = plt.figure(figsize=(12, 8))
plt.bar(horas, mar_2010, yerr=dmar_2010, capsize=5)
plt.xlabel('Horas(UTC)')
plt.ylabel('Radiação (J/m^2)')
plt.title(
    'Radiação média e desvio padrão da região do Bolsão no mês de março de 2010')
plt.savefig(r'C:\Users\igorb\OneDrive\Desktop\Projetos\ESTAÇÃO_METEOROLÓGICA\Rad_MS_2010_2020\Regiões\Bolsão\2010\\mar_2010.png')
plt.close()


#############
#   Abril   #
#############

horas = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
fig = plt.figure(figsize=(12, 8))
plt.bar(horas, abr_2010, yerr=dabr_2010, capsize=5)
plt.xlabel('Horas(UTC)')
plt.ylabel('Radiação (J/m^2)')
plt.title(
    'Radiação média e desvio padrão da região do Bolsão no mês de abril de 2010')
plt.savefig(r'C:\Users\igorb\OneDrive\Desktop\Projetos\ESTAÇÃO_METEOROLÓGICA\Rad_MS_2010_2020\Regiões\Bolsão\2010\\abr_2010.png')
plt.close()

############
#   Maio   #
############

horas = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
fig = plt.figure(figsize=(12, 8))
plt.bar(horas, mai_2010, yerr=dmai_2010, capsize=5)
plt.xlabel('Horas(UTC)')
plt.ylabel('Radiação (J/m^2)')
plt.title('Radiação média e desvio padrão da região do Bolsão no mês de maio de 2010')
plt.savefig(r'C:\Users\igorb\OneDrive\Desktop\Projetos\ESTAÇÃO_METEOROLÓGICA\Rad_MS_2010_2020\Regiões\Bolsão\2010\\mai_2010.png')
plt.close()

#############
#   Junho   #
#############

horas = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
fig = plt.figure(figsize=(12, 8))
plt.bar(horas, jun_2010, yerr=djun_2010, capsize=5)
plt.xlabel('Horas(UTC)')
plt.ylabel('Radiação (J/m^2)')
plt.title(
    'Radiação média e desvio padrão da região do Bolsão no mês de junho de 2010')
plt.savefig(r'C:\Users\igorb\OneDrive\Desktop\Projetos\ESTAÇÃO_METEOROLÓGICA\Rad_MS_2010_2020\Regiões\Bolsão\2010\\jun_2010.png')
plt.close()


#############
#   Julho   #
#############

horas = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
fig = plt.figure(figsize=(12, 8))
plt.bar(horas, jul_2010, yerr=djul_2010, capsize=5)
plt.xlabel('Horas(UTC)')
plt.ylabel('Radiação (J/m^2)')
plt.title(
    'Radiação média e desvio padrão da região do Bolsão no mês de julho de 2010')
plt.savefig(r'C:\Users\igorb\OneDrive\Desktop\Projetos\ESTAÇÃO_METEOROLÓGICA\Rad_MS_2010_2020\Regiões\Bolsão\2010\\jul_2010.png')
plt.close()


##############
#   Agosto   #
##############

horas = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
fig = plt.figure(figsize=(12, 8))
plt.bar(horas, ago_2010, yerr=dago_2010, capsize=5)
plt.xlabel('Horas(UTC)')
plt.ylabel('Radiação (J/m^2)')
plt.title(
    'Radiação média e desvio padrão da região do Bolsão no mês de agosto de 2010')
plt.savefig(r'C:\Users\igorb\OneDrive\Desktop\Projetos\ESTAÇÃO_METEOROLÓGICA\Rad_MS_2010_2020\Regiões\Bolsão\2010\\ago_2010.png')
plt.close()


################
#   Setembro   #
################

horas = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
fig = plt.figure(figsize=(12, 8))
plt.bar(horas, set_2010, yerr=dset_2010, capsize=5)
plt.xlabel('Horas(UTC)')
plt.ylabel('Radiação (J/m^2)')
plt.title(
    'Radiação média e desvio padrão da região do Bolsão no mês de setembro de 2010')
plt.savefig(r'C:\Users\igorb\OneDrive\Desktop\Projetos\ESTAÇÃO_METEOROLÓGICA\Rad_MS_2010_2020\Regiões\Bolsão\2010\\set_2010.png')
plt.close()

###############
#   Outubro   #
###############

horas = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
fig = plt.figure(figsize=(12, 8))
plt.bar(horas, out_2010, yerr=dout_2010, capsize=5)
plt.xlabel('Horas(UTC)')
plt.ylabel('Radiação (J/m^2)')
plt.title(
    'Radiação média e desvio padrão da região do Bolsão no mês de outubro de 2010')
plt.savefig(r'C:\Users\igorb\OneDrive\Desktop\Projetos\ESTAÇÃO_METEOROLÓGICA\Rad_MS_2010_2020\Regiões\Bolsão\2010\\out_2010.png')
plt.close()

################
#   Novembro   #
################

horas = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
fig = plt.figure(figsize=(12, 8))
plt.bar(horas, nov_2010, yerr=dnov_2010, capsize=5)
plt.xlabel('Horas(UTC)')
plt.ylabel('Radiação (J/m^2)')
plt.title(
    'Radiação média e desvio padrão da região do Bolsão no mês de novembro de 2010')
plt.savefig(r'C:\Users\igorb\OneDrive\Desktop\Projetos\ESTAÇÃO_METEOROLÓGICA\Rad_MS_2010_2020\Regiões\Bolsão\2010\\nov_2010.png')
plt.close()

################
#   Dezembro   #
################

horas = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
fig = plt.figure(figsize=(12, 8))
plt.bar(horas, dez_2010, yerr=ddez_2010, capsize=5)
plt.xlabel('Horas(UTC)')
plt.ylabel('Radiação (J/m^2)')
plt.title(
    'Radiação média e desvio padrão da região do Bolsão no mês de dezembro de 2010')
plt.savefig(r'C:\Users\igorb\OneDrive\Desktop\Projetos\ESTAÇÃO_METEOROLÓGICA\Rad_MS_2010_2020\Regiões\Bolsão\2010\\dez_2010.png')
plt.close()


################
#     2010     #
################

horas = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
fig = plt.figure(figsize=(12, 8))
plt.bar(horas, mediatotal_2010, yerr=desviototal_2010, capsize=5, color='red')
plt.xlabel('Horas(UTC)')
plt.ylabel('Radiação (J/m^2)')
plt.title('Radiação média e desvio padrão da região do Bolsão no ano de 2010')
plt.savefig(r'C:\Users\igorb\OneDrive\Desktop\Projetos\ESTAÇÃO_METEOROLÓGICA\Rad_MS_2010_2020\Regiões\Bolsão\2010\\2010.png')
plt.close()
