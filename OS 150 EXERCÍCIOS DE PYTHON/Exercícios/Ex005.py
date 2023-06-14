try:
    num1 = str(input("Digite o primeiro número: ")).replace(",", ".").strip()
    num2 = str(input("Digite o segundo número: ")).replace(",", ".").strip()
    print(f"A soma dos números são {float(num1)+float(num2)}, a diferença entre eles é de {(((float(num1) - float(num2))**2)**0.5)} e o quocente deles são {float(num1) / float(num2):.2f}")
except:
    print("Não consegui calcular nada, por favor, coloque apenas números reais")