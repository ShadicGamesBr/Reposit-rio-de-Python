# Pandas e Matplotlib
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

# Carregar os dados do arquivo
notas = pd.read_excel(r"C:\Users\ShadicGamesBr\Documents\ESTUDOS\PYTHON\OS 150 EXERCÍCIOS DE PYTHON\Exercícios\Documentos\Tabela 1.xlsx")

#Soma da coluna

boletim = {"Matérias":[], "Notas":([])}

for coluna in range(0, 8):
    boletim["Matérias"].append(notas.iloc[coluna, 0])

    
print(boletim)
