from math import factorial
print("               Calculadora")
while True:

    operadores = int(input("""    1 - Operacoes aritmeticas
    2 - Fatorial
    3 - Equacao Quadratica"""))


    if operadores == 1:
        conta = str(input("Operar: "))
        print(conta) 


    if operadores == 2:
        fat = int(input("Numero: "))
        print(f"\033[0;32m{factorial(fat)}\033[m")


    if operadores == 3:
        import Equacao_Quadratica_V2

    per = str(input("Quer continuar ?")).strip().lower()[0]

    if per not in "sn":
        per = str(input("Sim ou Nao")).strip().lower()[0]
    if per == "n":
        break
