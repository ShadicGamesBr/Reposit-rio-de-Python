# Pandas e Matplotlib
from matplotlib import pyplot as plt
import pandas as pd

# Carregar os dados do arquivo
lista = pd.read_excel(r"C:\Users\ShadicGamesBr\Documents\ESTUDOS\PYTHON\OS 150 EXERCÍCIOS DE PYTHON\Exercícios\Documentos\Tabela 1.xlsx")

provisorio = {"Notas":([])}

#Pega cada célula da tabela pela quantidade de linhas e colunas
boletim = {"Matérias":[], "Notas":[], "bimestre":[]}
for coluna in range(0, lista.shape[0]):
    for linha in range(0, len(lista.columns)):
        provisorio["Notas"].append(lista.iloc[coluna, linha])

notas = []

#Separa notas e matérias
for i in range(0, lista.shape[0]*5, 1):
    if i%5 ==0:
        boletim["Matérias"].append(provisorio["Notas"][i])
    else:
        notas.append(provisorio["Notas"][i])

#Divide as notas de 4 em 4
for bim in range(1, 5):
    boletim["bimestre"].append(f"{bim}º bimestre")

#Coloca as notas divididas no dicionário boletim
for nota in range(0, (lista.shape[0]*4), 4):
    boletim["Notas"].append(notas[nota:nota+4])



#Verifica as características da tabela
print(lista.shape[0]*5)
print(len(notas))
print(len(lista.columns))
print(boletim)

#Cria o gráfico do boletim
plt.plot(boletim["Matérias"], boletim["Notas"])
plt.title("Aproveitamento")
plt.show()

