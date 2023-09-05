try:
    num = float(input("Escreva um número: "))
    if num > 0:
        print(f"Número \033[35mpositivo\033[m")
    elif num == 0:
        print(f"Número igual a \033[37mzero\033[m")
    else:
        print("Número \033[31mnegativo\033[m")
except:
    print("Por favor, digite apenas números :)")