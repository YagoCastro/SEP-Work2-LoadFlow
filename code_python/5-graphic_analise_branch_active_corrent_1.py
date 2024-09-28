import matplotlib.pyplot as plt
import numpy as np

# Dados 
labels = ['Line 4-6', 'Line 5-4', 'Line 9-8', 'Line 7-8', 'Line 7-5', 
          'Line 6-9', 'Transformer 1', 'Transformer 2', 'Transformer 3']
methods = ['NR', 'GS', 'DR', 'AC', 'DC']
values = np.array([
    [0.30, 0.30, -0.28, 0.22, -0.42],
    [-0.30, -0.30, 0.50, -0.95, 9],
    [0.25, 0.25, -0.21, -1.36, 0.24],
    [0.78, 0.78, -0.13, 0.70, -9],
    [0.87, 0.87, -0.12, 1.63, 0],
    [-0.61, -0.61, 0.09, 0.99, -9],
    [-0.70, -0.70, 0.78, -0.69, -0.67],
    [-0.86, -0.86, 0.31, 1.53, 0.66],
    [1.65, 1.65, -0.25, 1.67, 2.63]
])

# Função para definir as cores
def get_color(value, is_reference):
    if is_reference:  
        return 'blue'
    elif abs(value) > 5:  
        return 'red'
    else:
        return 'green'

# gráficos
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(15, 15))
axes = axes.ravel()

for i, ax in enumerate(axes):
    colors = [get_color(values[i, j], j == 0) for j in range(len(methods))]
    bars = ax.bar(methods, values[i], color=colors)
    
    # Adiciona valores em cima de cada barra
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), 
                ha='center', va='bottom', fontsize=10)

    reference = values[i, 0]
    ax.axhline(y=reference, color='blue', linestyle='--', label='Referência (NR)')
    ax.set_title(labels[i])
    ax.set_ylim(min(values[i]) - 1, max(values[i]) + 1)  
    ax.legend()


plt.tight_layout()
plt.show()
