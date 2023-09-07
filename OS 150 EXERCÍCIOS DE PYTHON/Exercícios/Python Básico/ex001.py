try:
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        print("\033[36mEste número é par !\033[m")
    else:
        print("\033[33mEste número é ímpar!\033[m")

except ImportError:
    print(
        "\033[31mNão consegui calcular, verifique se você digitou apenas números !\033[m")
