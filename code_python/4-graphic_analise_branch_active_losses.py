import matplotlib.pyplot as plt
import numpy as np

# Dados 
labels = ['Line 4-6', 'Line 5-4', 'Line 9-8', 'Line 7-8', 'Line 7-5', 'Line 6-9', 
          'Transformer 1', 'Transformer 2', 'Transformer 3']
methods = ['NR', 'GS', 'DR', 'AC', 'DC']
values = np.array([
    [0.92, 0.92, 0.92, 1.01, 0],
    [1.00, 1.00, 1.00, 999, 0],
    [0.53, 0.53, 0.53, 999, 0],
    [0.69, 0.69, 0.69, 0.73, 0],
    [2.90, 2.90, 2.90, 100, 0],
    [2.49, 2.49, 2.49, 100, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 999, 0],
    [0, 0, 0, 0, 0]
])

# Função para definir as cores com base na comparação com NR
def get_color(value, reference):
    if value > reference * 10:  
        return 'red'
    else:
        return 'green'

# gráficos
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(15, 15))
axes = axes.ravel()

for i, ax in enumerate(axes):
   
    reference = values[i, 0]
    colors = [get_color(v, reference) for v in values[i]]
    ax.bar(methods, values[i], color=colors)
    ax.axhline(y=reference, color='blue', linestyle='--', label='Referência (NR)')
    ax.set_title(labels[i])
    ax.set_ylim(0, max(values[i]) + 50)
    ax.legend()


plt.tight_layout()
plt.show()
