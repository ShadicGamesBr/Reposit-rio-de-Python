import numpy as np
import math
try:
    matriz = np.array([])
    X = str(input("Quantidade de elementos em X: ")).strip().replace(" ", "")
    while not int(X.isnumeric()):
        X = str(input("Por favor, digite apenas a quantidade de elementos em X: ")).strip().replace(" ", "")
    Y = str(input("Quantidade de elementos em Y: ")).strip().replace(" ", "")
    while not int(Y.isnumeric()):
        Y = str(input("Por favor, digite apenas a quantidade de elementos em Y: ")).strip().replace(" ","")
    print("")
    for i in range(1, (int(X)*int(Y))+1):
        ele = str(input(f"Insira o elemento nº{i}: ")).strip().replace(" ", "")
        while not int(ele.isnumeric()):
            ele = str(input(f"Por favor, insira apenas número inteiros para o número {i}: ")).strip().replace(" ", "")
        matriz = np.append(matriz, int(ele))
    print(f"\nMatriz {X} x {Y}")
    print(f"Valor de X: {X}\nValor de Y: {Y}")
    print(matriz.reshape(int(X), int(Y)))
except:
    print("Ocorreu um erro desconhecido no programa, por favor, tente reiniciar o programa.")
