try:
    # 1, 2, 3, 5, 8, 13, 21, 34...
    # 5, 8, 13, N, 34, 55, 89
    sequencia = [1]
    num = str(input("Quantos números você quer que eu gero ?")).strip()

    while not num.isnumeric:
        num = str(input("Por favor, digite apenas números inteiros para funcionar :)")).strip()

    for i in range(1, int(num)+1):
        sequencia.append(sequencia[len(sequencia)-2]+ sequencia[len(sequencia)-1])


    print("Posição1: \033[34m1\033[m")
    for i,u in enumerate(sequencia):
        print(f"Posição{i+2}: \033[34m{sequencia[i]}\033[m")
except:
    print("Tente reiniciar o programa para poder gerar os números")