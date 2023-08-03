from matplotlib import pyplot as plt
#from scrollable_plots import scrollable

lista = [[10, 10, 10, 8], [8, 8, 9, 10], [10, 8, 8, 5], [10, 7, 9, 8], [7, 6, 6, 7], [8, 6, 8, 8], [9, 9, 8, 10], [10, 10, 9, 10], [9, 8, 9, 9], [7, 6, 5, 8], [10, 9, 8, 10], [10, 8, 9, 8]]

disciplinas = ("Artes", "Biologia", "Educação física", "Filosofia", "Física", "Geografia", "História", "Inglês", "Língua portuguesa", "Matemática", "Química", "Sociologia")

numDisciplinas = len(disciplinas)

fig, axs = plt.subplots(nrows=numDisciplinas)

for i in range(0, len(disciplinas)-1):
    ax = axs[i]
    plt.bar(range(1, 5), lista[i], color="black")
    plt.grid(axis="y", color="gray", linestyle="--", linewidth="0.5")
    plt.ylabel("Nota")
    plt.xlabel("Bimestre")
    plt.title(f"Notas por bimestre\n {disciplinas[i]}")

    #Ajusta o espaçamento entre os gráficos
    plt.tight_layout()

    #Mostra o gráfico composto
    plt.show()