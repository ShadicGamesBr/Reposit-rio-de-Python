try:
    total = 0

    num = int(input("Digite um número inteiro para ver se é primo ou não: "))

    for i in range(1, num+1):
        if num %i ==0:
            total += 1
    
    if total == 2:
        print(f"O número \033[33m{num}\033[m é um número primo")
    else:
        print(f"O número {num} \033[31mnão\033[m é um número primo")
except:
    print("Por favor digite apenas números inteiros :)")
    