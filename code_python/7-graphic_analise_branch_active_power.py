import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Dados 
labels = ['Line 4-6', 'Line 5-4', 'Line 9-8', 'Line 7-8', 'Line 7-5', 
          'Line 6-9', 'Transformer 1', 'Transformer 2', 'Transformer 3']
methods = ['NR', 'GS', 'DR', 'AC', 'DC']
values = np.array([
    [31.02, 31.02, 31.02, 22.07, -41.94],
    [-40.90, -40.90, -40.90, 0, 45.40],
    [24.26, 24.26, 24.26, 0, 23.97],
    [76.39, 76.39, 76.39, 74.17, -19.94],
    [86.60, 86.60, 86.60, 123.27, 0],
    [-59.26, -59.26, -59.26, 143.10, -22.65],
    [-72.34, -72.34, -72.34, -71.95, -67.00],
    [-85.00, -85.00, -85.00, 0, 65.72],
    [163.00, 163.00, 163.00, 169.98, 273.56]
])

# Função para definir as cores
def get_color(value, is_reference, is_nr_column):
    if is_nr_column:  
        return 'blue'
    elif abs(abs(is_reference) - abs(value)) > 5:  
        return 'red'
    else:
        return 'green'

# Cria gráficos para cada linha
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(15, 15))
axes = axes.ravel()

for i, ax in enumerate(axes):

    reference = values[i, 0] 
    colors = [get_color(values[i, j], reference, j == 0) for j in range(len(methods))]
    
    bars = ax.bar(methods, values[i], color=colors)
    
    # Adiciona valores em cima de cada barra
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), 
                ha='center', va='bottom', fontsize=10)


    ax.axhline(y=reference, color='blue', linestyle='--', label='Referência (NR)')
    ax.set_title(labels[i])
    ax.set_ylim(min(values[i]) - 50, max(values[i]) + 50)  
    ax.legend()



plt.tight_layout()
plt.show()

# Criar o heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(values, annot=True, cmap="coolwarm", xticklabels=methods, yticklabels=labels)
plt.title('Heatmap de Potência Ativa')
plt.show()
