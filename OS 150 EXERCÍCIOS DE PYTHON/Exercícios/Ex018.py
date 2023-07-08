from matplotlib import pyplot as plt
from random import randint

X = []

Y = []
a = int(input("Valor de a: "))
b = int(input("Valor de b: "))
c = int(input("Valor de c: "))
for x in range(-20, 21):
    X.append([x])   
    Y.append([(a*x**2) + (b*x) + (c)])

plt.plot(X, Y)
plt.show()