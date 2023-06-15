try:
    num1 = float(input("Digite um número real: "))
    num2 = float(input("Digite o segundo número: "))

    
    if num1 > num2:
        print(f"O maior número é \033[34m{num1}\033[m")
    else:
        print(f"O maior número é \033[37m{num2}\033[m")
    
except:
    print("Digite apenas números reais!")