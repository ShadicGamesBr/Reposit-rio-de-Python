import matplotlib.pyplot as plt

while True:
    y = []
    x = []
    for i in range(-20, 21):
        x.append(i)

    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))
    calc = []
    for res in range(0, len(x)):
        y.append(a*x[res]**2+b*x[res]+c)

    delta = b**2 - (4*a*c)




    if delta > 0:
        x1 = (-b+(delta**0.5))/(2*a)
        x2 = (-b-(delta**0.5))/(2*a)
        print(f"dois valores: {x1}, {x2}")
        plt.scatter(x1, a*x1**2+b*x1+c, color='red')
        plt.annotate(f"X1: {x1:.1f}", xy=(x1, a*x1**2 + b*x1 + c), xytext=(x1-4, a*x1**2+b*x1+c+400))
        plt.scatter(x2, a*x2**2+b*x2+c, color = "green")
        plt.annotate(f"X2: {x2:.1f}", xy=(x2, a*x2**2+b*x2+c), xytext=(x2-4, a*x2**2+b*x2+c+250))

    elif delta == 0:
        x1 = (-b+(delta**0.5))/(2*a)
        plt.title(f"Um valor: {x1}")
        plt.scatter(x1, a*x1**2+b*x1+c, color='red')
        plt.annotate(f"X1: {x1:2f}", xy=(x1, a*x1**2 + b*x1 + c), xytext=(x1-3, a*x1**2+b*x1+c+90))
    else:
        plt.title("Não possui valores reais")
    plt.title(f"{a:.0f}x² + {b:.0f}x + {c:.0f}")
    plt.ylabel("eixo Y")
    plt.axhline(0, color="black", linewidth=1)
    plt.axvline(0, color="black", linewidth=1)
    plt.xlim(-20, 20)
    plt.ylim(-1000, 1000)
    plt.grid()
    plt.xlabel("eixo X")
    plt.plot(x, y)
    plt.show()
    per = str(input("Quer continuar ? ")).strip().replace(" ", "")
    if per in "n":
        break
print(f"\033[m31Fim do programa\033[m")