import numpy as np
print("Calculadora de matrizes lineares")
metodos = ["inv", "eig", "det", "qr", "svd", ]
nomes = ["matriz inversa", "Autovalores", "Determinante", "Decomposição QR", "Decomposição singular"]
matriz = np.array([])
X = str(input("Quantidade de elementos em X: ")).strip()
np.set_printoptions(precision=3, suppress=True)
while not float(X.isnumeric()):
    X = str(input("Por favor, digite apenas a quantidade de elementos em X: ")).strip()

Y = str(input("Quantidade de elementos em Y: ")).strip()
while not float(Y.isnumeric()):
    Y = str(input("Por favor, digite apenas a quantidade de elementos em Y: ")).strip()
print("")
for i in range(1, (int(X)*int(Y))+1):
    ele = str(input(f"Insira o elemento nº{i}: ")).strip()
    matriz = np.append(matriz, float(ele)) 

print()
while True:
    for met in range(0, len(metodos)):
        print(f"{met+1} {nomes[met]}: ({metodos[met]})")
    meto = str(input("\nSelecione um método acima ↑ ")).strip()

    while not meto.isnumeric() or  0 == int(meto) or int(meto) > len(metodos):
        meto = str(input(f"Por favor, digite no intervalo de 1 até {len(metodos)}: ")).strip().replace(" ", "").lower()

    metodo_escolhido = metodos[int(meto)-1]
    metodo = getattr(np.linalg, metodo_escolhido)
    print(f"\n\nMatriz {X} x {Y}\n\n")
    print(f"Método:  {nomes[int(meto)-1]}\n\033[32m{metodo(matriz.reshape(int(X),int(Y)))}\033[m")
    per1 = str(input("Quer outro método ?")).strip().lower().replace(" ", "")
    while per1.isnumeric() or per1 not in "sn":
        per1 = str(input("Por favor, digite s/n")).strip().replace(" ", "").lower()
    if per1 in "n":
        break 
 