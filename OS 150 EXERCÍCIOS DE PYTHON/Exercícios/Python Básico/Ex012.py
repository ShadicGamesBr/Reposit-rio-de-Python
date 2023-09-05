try:
    numeros = float(input("Digite o primeiro número: ")), float(input("digite o segundo número: ")), float(input("digite o terceiro número: "))

    print(f"A média entre eles é {(numeros[0] + numeros[1]+ numeros[2])/3}")
except:
    print("Ocorreu um erro no programa, por favor, tente novamente")
