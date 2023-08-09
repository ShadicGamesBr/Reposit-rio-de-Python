#Movimento oblíquio

from matplotlib import pyplot as plt
import seaborn as sb
from math import radians,cos,sin

#Vo = float(input("Velocidade do objeto (m/s): ")) #velocidade em M/S
#Ang = float(input("Ângulo do objeto °: ")) #angulo
Vo = 50
Ang = 45
Vox = (Vo*(cos(radians(Ang)))) #Calcula a velocidade horizontal
Voy = (Vo*(sin(radians(Ang)))) #Calcula a velocidade vertical

Tempo_subida = (Voy / 9.8) # Calcula o termpo de subida que o é mesmo que o tempo de descida

Alc = (Vox*Tempo_subida*2)
Alt = (Voy ** 2) / (2 * 9.8)

x = []
y = []

for t in range(0, 21):
    x.append(t)
    y.append(Voy*t - (0.5 * 9.8 *t**2)) #coloca cada valor de y no gráfico

plt.plot(x, y)
plt.title("Movimento oblíquo")
plt.xlabel("Tempo (s)")
plt.ylabel("Altura ()")
plt.show()
