import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 400)

y_cos = np.cos(x) #прилежащий катет к гипотенузе
y_sin = np.sin(x) #противолежащий катет к гипотенузе

plt.figure(figsize=(10, 6))

plt.plot(x, y_cos, color="red", label='cos(x)')
plt.plot(x, y_sin, color="blue", label='sin(x)')

plt.grid(True)

plt.title('Графики функций cos(x) и sin(x)')
plt.xlabel('x')
plt.xlabel('y')

plt.legend

plt.axhline(0, color="black", linewidth=0.5, ls="--") #Горизонтальная ось
plt.axvline(0, color="black", linewidth=0.5, ls="--") #Вертикальная ось
plt.xlim(-2 * np.pi, 2 * np.pi)
plt.ylim(-1.5, 1.5)

plt.show()