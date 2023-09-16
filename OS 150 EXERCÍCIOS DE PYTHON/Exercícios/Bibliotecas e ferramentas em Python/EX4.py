#Movimento oblíquio

from matplotlib import pyplot as plt

from math import radians,cos,sin

from matplotlib.animation import FuncAnimation

from functools import partial

import numpy as np

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
    y.append(Voy*t - (0.5 * 9.8 * t**2)) #coloca cada valor de y no gráfico

fig, ax = plt.subplots()
line1, = ax.plot([], [], "ro")
def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return line1,

def update(frame, ln, x, y):
    x.append(frame)
    y.append(np.sin(frame))
    ln.set_data(x, y)
    return ln,

ani = FuncAnimation(
    fig, partial(update, ln=line1, x=[], y=[]),
    frames = np.linspace(0, 2*np.pi, 128),
    init_func=init, blit=True
)

plt.show()