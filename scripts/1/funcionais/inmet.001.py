#!/usr/bin/python
#coding: utf-8

# _autor_: Hallan Souza

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics
import csv
import pathlib
import os

from decimal import Decimal

# ===========================================================
# ===========================================================


def qualmes(mes):
    if mes == 1:
        dias = int(0)
    if mes == 2:
        dias = int(31)
    if mes == 3:
        dias = int(59)
    if mes == 4:
        dias = int(90)
    if mes == 5:
        dias = int(120)
    if mes == 6:
        dias = int(150)
    if mes == 7:
        dias = int(181)
    if mes == 8:
        dias = int(212)
    if mes == 9:
        dias = int(243)
    if mes == 10:
        dias = int(273)
    if mes == 11:
        dias = int(304)
    if mes == 12:
        dias = int(334)

    return dias


direct_csv = '/home/hallan/research/research.data/data.extracted/data.extracted.inmet/inmet.2019/data.inmet.001/'

arr = os.listdir(direct_csv)
# print(arr)

for file in arr:
    arquivos = '/home/hallan/research/research.data/data.extracted/data.extracted.inmet/inmet.2019/data.inmet.001/'+file+''
    # print(arquivos)

    data = []

    inmet = pd.read_csv(arquivos, skiprows=range(0, 10))

    df = pd.DataFrame(inmet)

    for i, j in df.iterrows():

        codgo = str(file[6:10])

        tempo = j[0]

        2010-01-01
        00: 00

        ano = int(tempo[0:4])
        mes = int(tempo[5:7])
        ddd = int(tempo[8:10])

        #print(ano, "*******", mes, "*******", ddd, "*******", codgo)

        tempo09 = j[0]
        tempo10 = j[0]
        tempo11 = j[0]
        tempo12 = j[0]
        tempo13 = j[0]
        tempo14 = j[0]
        tempo15 = j[0]
        tempo16 = j[0]
        tempo17 = j[0]
        tempo18 = j[0]
        tempo19 = j[0]
        tempo20 = j[0]
        tempo21 = j[0]
        tempo22 = j[0]

        ano09 = int(tempo09[0:4])
        ano10 = int(tempo10[0:4])
        ano11 = int(tempo11[0:4])
        ano12 = int(tempo12[0:4])
        ano13 = int(tempo13[0:4])
        ano14 = int(tempo14[0:4])
        ano15 = int(tempo15[0:4])
        ano16 = int(tempo16[0:4])
        ano17 = int(tempo17[0:4])
        ano18 = int(tempo18[0:4])
        ano19 = int(tempo19[0:4])
        ano20 = int(tempo20[0:4])
        ano21 = int(tempo21[0:4])
        ano22 = int(tempo22[0:4])

        mes09 = int(tempo09[5:7])
        mes10 = int(tempo10[5:7])
        mes11 = int(tempo11[5:7])
        mes12 = int(tempo12[5:7])
        mes13 = int(tempo13[5:7])
        mes14 = int(tempo14[5:7])
        mes15 = int(tempo15[5:7])
        mes16 = int(tempo16[5:7])
        mes17 = int(tempo17[5:7])
        mes18 = int(tempo18[5:7])
        mes19 = int(tempo19[5:7])
        mes20 = int(tempo20[5:7])
        mes21 = int(tempo21[5:7])
        mes22 = int(tempo22[5:7])

        ddd09 = int(tempo09[8:10])
        ddd10 = int(tempo10[8:10])
        ddd11 = int(tempo11[8:10])
        ddd12 = int(tempo12[8:10])
        ddd13 = int(tempo13[8:10])
        ddd14 = int(tempo14[8:10])
        ddd15 = int(tempo15[8:10])
        ddd16 = int(tempo16[8:10])
        ddd17 = int(tempo17[8:10])
        ddd18 = int(tempo18[8:10])
        ddd19 = int(tempo19[8:10])
        ddd20 = int(tempo20[8:10])
        ddd21 = int(tempo21[8:10])
        ddd22 = int(tempo22[8:10])

        # =============================

        rad10 = j[2:3]
        rad11 = j[3:4]
        rad12 = j[4:5]
        rad13 = j[5:6]
        rad14 = j[6:7]
        rad15 = j[7:8]
        rad16 = j[8:9]
        rad17 = j[9:10]
        rad18 = j[10:11]
        rad19 = j[11:12]
        rad20 = j[12:13]
        rad21 = j[13:14]
        rad22 = j[14:15]

        # =============================

        rad09 = pd.to_numeric(j[1:2], errors='coerce')
        rad09 = float(rad09)
        wm2_09 = rad09 * (1000/3600)

        thora09 = 9 * 60
        frac09 = thora09 / 1440

        d09 = qualmes(mes09)

        tt09 = d09 + frac09 + ddd09
        dj09 = float(tt09)

        h09 = 9.0

        num09 = [codgo, ano09, mes09, ddd09, h09, dj09, wm2_09]
        data.append(num09)
        # print(data.values)
        # print(num09)

        # ++++++++++++++++++

        rad10 = pd.to_numeric(j[2:3], errors='coerce')
        rad10 = float(rad10)
        wm2_10 = rad10 * (1000/3600)

        thora10 = 10 * 60
        frac10 = thora10 / 1040

        d10 = qualmes(mes10)

        tt10 = d10 + frac10 + ddd10
        dj10 = float(tt10)

        h10 = 10.0

        num10 = [codgo, ano10, mes10, ddd10, h10, dj10, wm2_09]
        data.append(num10)

        # ++++++++++++++++++

        rad11 = pd.to_numeric(j[3:4], errors='coerce')
        rad11 = float(rad11)
        wm2_11 = rad11 * (1000/3600)

        thora11 = 11 * 60
        frac11 = thora11 / 1140

        d11 = qualmes(mes11)

        tt11 = d11 + frac11 + ddd11
        dj11 = float(tt11)

        h11 = 11.0

        num11 = [codgo, ano11, mes11, ddd11, h11, dj11, wm2_11]
        data.append(num11)

        # ++++++++++++++++++

        rad12 = pd.to_numeric(j[4:5], errors='coerce')
        rad12 = float(rad12)
        wm2_12 = rad12 * (1000/3600)

        thora12 = 12 * 60
        frac12 = thora12 / 1240

        d12 = qualmes(mes12)

        tt12 = d12 + frac12 + ddd12
        dj12 = float(tt12)

        h12 = 12.0

        num12 = [codgo, ano12, mes12, ddd12, h12, dj12, wm2_12]
        data.append(num12)

        # ++++++++++++++++++

        rad13 = pd.to_numeric(j[5:6], errors='coerce')
        rad13 = float(rad13)
        wm2_13 = rad13 * (1000/3600)

        thora13 = 13 * 60
        frac13 = thora13 / 1340

        d13 = qualmes(mes13)

        tt13 = d13 + frac13 + ddd13
        dj13 = float(tt13)

        h13 = 13.0

        num13 = [codgo, ano13, mes13, ddd13, h13, dj13, wm2_13]
        data.append(num13)

        # ++++++++++++++++++

        rad14 = pd.to_numeric(j[6:7], errors='coerce')
        rad14 = float(rad14)
        wm2_14 = rad14 * (1000/3600)

        thora14 = 14 * 60
        frac14 = thora14 / 1440

        d14 = qualmes(mes14)

        tt14 = d14 + frac14 + ddd14
        dj14 = float(tt14)

        h14 = 14.0

        num14 = [codgo, ano14, mes14, ddd14, h14, dj14, wm2_14]
        data.append(num14)

        # ++++++++++++++++++

        rad15 = pd.to_numeric(j[7:8], errors='coerce')
        rad15 = float(rad15)
        wm2_15 = rad15 * (1000/3600)

        thora15 = 15 * 60
        frac15 = thora15 / 1440

        d15 = qualmes(mes15)

        tt15 = d15 + frac15 + ddd15
        dj15 = float(tt15)

        h15 = 15.0

        num15 = [codgo, ano15, mes15, ddd15, h15, dj15, wm2_15]
        data.append(num15)

        # ++++++++++++++++++

        rad16 = pd.to_numeric(j[8:9], errors='coerce')
        rad16 = float(rad16)
        wm2_16 = rad16 * (1000/3600)

        thora16 = 16 * 60
        frac16 = thora16 / 1440

        d16 = qualmes(mes16)

        tt16 = d16 + frac16 + ddd16
        dj16 = float(tt16)

        h16 = 16.0

        num16 = [codgo, ano16, mes16, ddd16, h16, dj16, wm2_16]
        data.append(num16)

        # ++++++++++++++++++

        rad17 = pd.to_numeric(j[9:10], errors='coerce')
        rad17 = float(rad17)
        wm2_17 = rad17 * (1000/3600)

        thora17 = 17 * 60
        frac17 = thora17 / 1440

        d17 = qualmes(mes17)

        tt17 = d17 + frac17 + ddd17
        dj17 = float(tt17)

        h17 = 17.0

        num17 = [codgo, ano17, mes17, ddd17, h17, dj17, wm2_17]
        data.append(num17)

        # ++++++++++++++++++

        rad18 = pd.to_numeric(j[10:11], errors='coerce')
        rad18 = float(rad18)
        wm2_18 = rad18 * (1000/3600)

        thora18 = 18 * 60
        frac18 = thora18 / 1440

        d18 = qualmes(mes18)

        tt18 = d18 + frac18 + ddd18
        dj18 = float(tt18)

        h18 = 18.0

        num18 = [codgo, ano18, mes18, ddd18, h18, dj18, wm2_18]
        data.append(num18)

        # ++++++++++++++++++

        rad19 = pd.to_numeric(j[11:12], errors='coerce')
        rad19 = float(rad19)

        wm2_19 = rad19 * (1000/3600)

        thora19 = 19 * 60
        frac19 = thora19 / 1440

        d19 = qualmes(mes19)

        tt19 = d19 + frac19 + ddd19
        dj19 = float(tt19)

        h19 = 19.0

        num19 = [codgo, ano19, mes19, ddd19, h19, dj19, wm2_19]
        data.append(num19)

        # ++++++++++++++++++

        rad20 = pd.to_numeric(j[12:13], errors='coerce')
        rad20 = float(rad20)
        wm2_20 = rad20 * (1000/3600)

        thora20 = 20 * 60
        frac20 = thora20 / 1440

        d20 = qualmes(mes20)

        tt20 = d20 + frac20 + ddd20
        dj20 = float(tt20)

        h20 = 20.0

        num20 = [codgo, ano20, mes20, ddd20, h20, dj20, wm2_20]
        data.append(num20)

        # ++++++++++++++++++

        rad21 = pd.to_numeric(j[13:14], errors='coerce')

        rad21 = float(rad21)

        wm2_21 = rad21 * (1000/3600)

        thora21 = 21 * 60
        frac21 = thora21 / 1440

        d21 = qualmes(mes21)

        tt21 = d21 + frac21 + ddd21
        dj21 = float(tt21)

        h21 = 21.0

        num21 = [codgo, ano21, mes21, ddd21, h21, dj21, wm2_21]
        data.append(num21)

        # ++++++++++++++++++

        rad22 = pd.to_numeric(j[14:15], errors='coerce')

        rad22 = float(rad22)

        wm2_22 = rad22 * (1000/3600)

        thora22 = 22 * 60
        frac22 = thora22 / 1440

        d22 = qualmes(mes22)

        tt22 = d09 + frac22 + ddd22
        dj22 = float(tt22)

        h22 = 22.0

        num22 = [codgo, ano22, mes22, ddd22, h22, dj22, wm2_22]
        data.append(num22)

        # ++++++++++++++++++

    print(data)
    info_data = pd.DataFrame(data,
                             columns=['inmet', 'ano', 'mes', 'dia', 'utc', 'diaJuliano', 'radiacao_wm2'])
    info_data.to_csv(
        '/home/hallan/research/research.data/data.extracted/data.extracted.inmet/inmet.2017/data.inmet.002/org' + file + '')
