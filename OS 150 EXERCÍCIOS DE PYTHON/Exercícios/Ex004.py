try:
    res = 1
    fat = int(input("Fatorial de : "))
    for i in range(fat, 1, -1):
        res *= i
    print(f"O fatorial de \033[36m{fat}\033[m é \033[34m{res}\033[m")
except:
    print("Não consegui calcular o fatorial, considere usar apenas números inteiros.")