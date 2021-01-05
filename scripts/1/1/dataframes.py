import os
import pandas as pd
import numpy as np

paths = "C:\\Users\\Host02\\Documents\\analise2\\archives\\ms"

df = []

arr = os.scandir(paths)

for file in arr:
    df2 = pd.read_csv(file.path, skiprows=range(0, 9), sep=";")
    df.append(df2)

df = pd.concat(df)


print(df)
"""
# for i, file in enumerate(arr):
#     load_df = pd.read_csv(file.path, skiprows=range(0, 9), sep=";")
#     if i == 0:
#         df = load_df
#     if i > 0:
#         df = pd.concat([df, load_df])
"""
