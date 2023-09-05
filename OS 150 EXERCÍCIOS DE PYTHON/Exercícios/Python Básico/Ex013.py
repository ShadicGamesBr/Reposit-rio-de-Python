try:
    print("Consulta de quadrados perfeitos")
    num = str(input("Digite um número inteiro: ")).strip().replace(",", ".")

    while float(num) %1 !=0:
        num = str(input("Por favor, digite números inteiros")).strip().replace(",", ".")

    while num.isalpha():
        num = str(input("Por favor, não coloque letras ou símbolos: ")).strip().replace(",", ".")

    if (int(num) **0.5) %1 ==0:
        print(f"O {num} é um quadrado perfeito!")
        print(f"√{num} = {int(num)**0.5}")
    else:
        print(f"O \033[33m{num}\033[m \033[31mNão é um quadrado perfeito...\033[m")
except:
    print("Ocorreu um erro, tente reiniciar o programa")