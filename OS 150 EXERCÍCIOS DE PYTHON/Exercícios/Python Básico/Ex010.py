from time import sleep
try:
    frase = str(input("Digite uma frase: "))
    print("")
    for letra, pos in enumerate(frase):
        print(f"Letra \033[34m'{frase[letra]}'\033[m na posição {letra+1}")
        sleep(0.1)
except:
    print("Ocorreu um erro no programa, por gentileza tente novamente :)")
    