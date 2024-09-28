import matplotlib.pyplot as plt
import numpy as np

# Dados
labels = ['Line 4-6', 'Line 5-4', 'Line 9-8', 'Line 7-8', 'Line 7-5', 'Line 6-9', 
          'Transformer 1', 'Transformer 2', 'Transformer 3']
methods = ['NR', 'GS', 'DR', 'AC', 'DC']
values = np.array([
    [40.78, 40.78, 40.78, 37.47, 41.95],
    [60.76, 60.76, 60.76, 0.00, 45.40],
    [32.93, 32.93, 32.93, 0.00, 23.97],
    [78.54, 78.54, 78.54, 81.19, 19.93],
    [88.39, 88.39, 88.39, 632.33, 0.00],
    [59.49, 59.49, 59.49, 639.98, 22.65],
    [104.11, 104.11, 104.11, 72.84, 67.00],
    [91.47, 91.47, 91.47, 0.00, 65.72],
    [171.54, 171.54, 171.54, 171.07, 273.55]
])

# Função para definir as cores com base nos intervalos
def get_color(value):
    if value <= 60.99:
        return 'green'
    elif 61 <= value <= 79.99:
        return 'yellow'
    elif 80 <= value <= 95:
        return 'orange'
    else:
        return 'red'

# gráficos
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(15, 15))
axes = axes.ravel()

for i, ax in enumerate(axes):
    colors = [get_color(v) for v in values[i]]
    ax.bar(methods, values[i], color=colors)
    ax.axhline(y=100, color='blue', linestyle='--', label='Reference (100)')
    ax.set_title(labels[i])
    ax.set_ylim(0, max(values[i]) + 50)
    ax.legend()


plt.tight_layout()
plt.show()
