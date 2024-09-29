import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 5, 50)

y = x ** 3

plt.plot(x, y)
plt.show()

#Matplotlib отображает ваши данные на Figure-х (например, Windows, виджеты Jupyter и т.д.).
#Каждый из них может содержать один или несколько Axes, область, где точки могут быть указаны в терминах координат x-y.
#Самый простой способ создания фигуры с осями - это использование pyplot.subplots.
