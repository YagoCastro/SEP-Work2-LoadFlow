import matplotlib.pyplot as plt
import numpy as np

# Dados 
active_current = np.array([
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

# Labels para as linhas
labels = ['Line 4-6', 'Line 5-4', 'Line 9-8', 'Line 7-8', 'Line 7-5', 
          'Line 6-9', 'Transformer 1', 'Transformer 2', 'Transformer 3']

# Configuração do gráfico
fig, ax = plt.subplots(figsize=(12, 8))

# Criação do gráfico de barras para cada método
bar_width = 0.15  
x = np.arange(len(labels))  

# Adicionando barras para cada método
for i in range(active_current.shape[1]):
    bars = ax.bar(x + i * bar_width, active_current[:, i], width=bar_width, label=f'Active Current ({["NR", "GS", "DR", "AC", "DC"][i]})')
    
    # Adicionando os valores em cima das barras
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom', fontsize=9)

# Adiciona títulos e rótulos
ax.set_xlabel('Trechos')
ax.set_ylabel('Corrente Ativa (A)')
ax.set_title('Análise da Corrente Ativa em Cada Trecho')
ax.set_xticks(x + bar_width * 2) 
ax.set_xticklabels(labels)


ax.legend()


plt.tight_layout()
plt.show()
