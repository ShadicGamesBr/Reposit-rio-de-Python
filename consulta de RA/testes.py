#disciplinas = {"Artes" , "Biologia", "Educação física", "Filosofia", "Física", "Geografia", "História", #"Inglês", "Português", "Matemática", "Química", "Sociologia"}

import matplotlib.pyplot as plt
import numpy as np

# Dados do boletim
disciplinas = ['Artes', 'Matemática', 'Ciências', 'História']
bimestres = ['Bimestre 1', 'Bimestre 2', 'Bimestre 3', 'Bimestre 4']
notas = np.random.randint(0, 10, (len(disciplinas), len(bimestres)))  # Notas aleatórias

# Criar o gráfico de barras
fig, ax = plt.subplots()

# Posições das barras
posicoes = np.arange(len(bimestres))

# Largura das barras
largura = 0.15

# Plotar as barras para cada disciplina
for i, disciplina in enumerate(disciplinas):
    deslocamento = (i - len(disciplinas)//2) * largura
    ax.bar(posicoes + deslocamento, notas[i], largura, label=disciplina)

# Personalizar os eixos
ax.set_ylabel('Notas')
ax.set_xlabel('Bimestres')
ax.set_title('Boletim Escolar')
ax.set_xticks(posicoes)
ax.set_xticklabels(bimestres)
ax.legend()

# Exibir o gráfico
plt.show()
