import numpy as np
import matplotlib.pyplot as plt

# Dados
buses = ["Bus 1", "Bus 2", "Bus 3", "Bus 4", "Bus 5", "Bus 6", "Bus 7", "Bus 8", "Bus 9"]
active_power_NR = [72.336976, 162.999077, 84.999789, 0, -124.999200, -89.999694, 0, -99.999415, 0]
active_power_GS = [72.336976, 162.999077, 84.999789, 0, -124.999200, -89.999694, 0, -99.999415, 0]
active_power_DR = [72.336049, 162.998546, 84.999572, 0.002133, -124.997924, -90.000198, -0.003062, -99.998589, 0.000892]
active_power_AC = [71.953826, 169.978137, -0.0, 95.760577, 0, 121.257873, 27.466364, 50.680731, 0]
active_power_DC = [69.662705, 0, 0, 261.075191, 0, 0, 0, 138.110308, 151.870269]

# Configuração dos gráficos
x = np.arange(len(buses))  # índice dos barramentos

plt.figure(figsize=(10, 10))

# Gráfico 1: Comparação GS e NR
plt.subplot(2, 2, 1)
plt.bar(x - 0.2, active_power_NR, width=0.4, label='Active Power NR', color='blue')
plt.bar(x + 0.2, active_power_GS, width=0.4, label='Active Power GS', color='orange')
plt.xticks(x, buses)
plt.ylabel('Active Power (MW)')
plt.title('Comparação de Potência Ativa: GS vs NR')
plt.legend()

# Gráfico 2: Comparação DR e NR
plt.subplot(2, 2, 2)
plt.bar(x - 0.2, active_power_NR, width=0.4, label='Active Power NR', color='blue')
plt.bar(x + 0.2, active_power_DR, width=0.4, label='Active Power DR', color='green')
plt.xticks(x, buses)
plt.ylabel('Active Power (MW)')
plt.title('Comparação de Potência Ativa: DR vs NR')
plt.legend()

# Gráfico 3: Comparação AC e NR
plt.subplot(2, 2, 3)
plt.bar(x - 0.2, active_power_NR, width=0.4, label='Active Power NR', color='blue')
plt.bar(x + 0.2, active_power_AC, width=0.4, label='Active Power AC', color='orange')
plt.xticks(x, buses)
plt.ylabel('Active Power (MW)')
plt.title('Comparação de Potência Ativa: AC vs NR')
plt.legend()

# Gráfico 4: Comparação DC e NR
plt.subplot(2, 2, 4)
plt.bar(x - 0.2, active_power_NR, width=0.4, label='Active Power NR', color='blue')
plt.bar(x + 0.2, active_power_DC, width=0.4, label='Active Power DC', color='green')
plt.xticks(x, buses)
plt.ylabel('Active Power (MW)')
plt.title('Comparação de Potência Ativa: DC vs NR')
plt.legend()

plt.tight_layout()
plt.show()
