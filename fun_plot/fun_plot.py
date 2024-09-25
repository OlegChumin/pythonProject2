import numpy as np
import matplotlib.pyplot as plt


# Создаем массив значений x от -2π до 2π
x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
# Вычисляем значения y для косинуса и синуса
y_cos = np.cos(x)
y_sin = np.sin(x)
y_tan = np.tan(x)
y_ctg = np.cos(x) / np.sin(x)

# Создаем график
plt.figure(figsize=(10, 6))

# График косинуса (красный)
plt.plot(x, y_cos, color='red', label='cos(x)')
# График синуса (синий)
plt.plot(x, y_sin, color='blue', label='sin(x)')
# График тангенса (коричневый)
plt.plot(x, y_tan, color='brown', label='tan(x)')
# График котангенса (желтый)
plt.plot(x, y_ctg, color='yellow', label='ctg(x)')

# Добавляем координатную сетку
plt.grid(True)

# Добавляем заголовок и метки осей
plt.title('Графики функций cos(x), sin(x), tan(x), ctg(x) ')
plt.xlabel('x')
plt.ylabel('y')

# Добавляем легенду
plt.legend()

# Отображаем график
plt.axhline(0, color='black',linewidth=0.5, ls='--')  # Горизонтальная ось
plt.axvline(0, color='black',linewidth=0.5, ls='--')  # Вертикальная ось
plt.xlim(-2 * np.pi, 2 * np.pi)  # Установка пределов по оси x
plt.ylim(-1.5, 1.5)  # Установка пределов по оси y

plt.show()
