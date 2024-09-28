import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Dados
labels = ['Line 4-6', 'Line 5-4', 'Line 9-8', 'Line 7-8', 'Line 7-5', 
          'Line 6-9', 'Transformer 1', 'Transformer 2', 'Transformer 3']
methods = ['NR', 'GS', 'DR', 'AC', 'DC']
values = np.array([
    [26.46, 26.46, 26.46, -30.29, 0],
    [-44.94, -44.94, -44.94, 0, 0],
    [22.27, 22.27, 22.27, 0, 0],
    [18.28, 18.28, 18.28, -33.01, 0],
    [17.70, 17.70, 17.70, 620.20, 0],
    [-5.07, -5.07, -5.07, 623.79, 0],
    [-74.88, -74.88, -74.88, -11.36, 0],
    [-33.78, -33.78, -33.78, 0, 0],
    [53.47, 53.47, 53.47, 19.36, 0]
])

# Função para definir as cores 
def get_color(value, is_reference, is_nr_column):
    if is_nr_column:  
        return 'blue'
    elif abs(abs(is_reference) - abs(value)) > 5:  
        return 'red'
    else:
        return 'green'

# Criar gráficos para cada linha
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(15, 15))
axes = axes.ravel()

for i, ax in enumerate(axes):

    reference = values[i, 0]  
    colors = [get_color(values[i, j], reference, j == 0) for j in range(len(methods))]
    
    bars = ax.bar(methods, values[i], color=colors)
    

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
plt.title('Heatmap de Potência Reativa (Qf: RP)')
plt.show()
