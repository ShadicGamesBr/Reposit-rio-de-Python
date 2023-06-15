try:
    pala = str(input("Digite uma palavra: "))
    print(f"a palavra \033[36m{pala}\033[m ao contrário fica: ")
    for i in range(len(pala)-1, -1, -1):
        print(f"\033[36m{pala[i]}\033[m", end="")
except:
    print("Digite apenas palavras ou números")
