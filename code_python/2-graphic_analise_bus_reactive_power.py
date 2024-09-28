import matplotlib.pyplot as plt
import numpy as np

# Dados 
buses_new = ["Bus 1", "Bus 2", "Bus 3", "Bus 4", "Bus 5", "Bus 6", "Bus 7", "Bus 8", "Bus 9"]
reactive_power_NR_new = [81.18, 53.47, 38.64, 0.00, -50.00, -30.00, 0.00, -35.00, -0.00]
reactive_power_GS_new = [81.18, 53.47, 38.64, 0.00, -50.00, -30.00, 0.00, -35.00, -0.00]
reactive_power_DR_new = [81.18, 53.47, 38.64, 0.00, -50.00, -30.00, -0.00, -35.00, -0.00]
reactive_power_AC_new = [14.23, 19.36, 1794.14, 1196.34, 0.00, 655.28, 585.23, 1090.60, 0.00]
reactive_power_DC_new = [73.57, 1682.08, 0.00, 2143.38, 0.00, 0.00, 0.00, 1372.87, 2262.80]

x = np.arange(len(buses_new)) 

# Configuração dos gráficos 
plt.figure(figsize=(10, 10))

# Gráfico 1: Comparação GS e NR
plt.subplot(2, 2, 1)
plt.bar(x - 0.2, reactive_power_NR_new, width=0.4, label='Reactive Power NR', color='blue')
plt.bar(x + 0.2, reactive_power_GS_new, width=0.4, label='Reactive Power GS', color='green')
plt.xticks(x, buses_new)
plt.ylabel('Reactive Power (MVAR)')
plt.title('Comparação de Potência Reativa: GS vs NR')
plt.legend()

# Gráfico 2: Comparação DR e NR
plt.subplot(2, 2, 2)
plt.bar(x - 0.2, reactive_power_NR_new, width=0.4, label='Reactive Power NR', color='blue')
plt.bar(x + 0.2, reactive_power_DR_new, width=0.4, label='Reactive Power DR', color='green')
plt.xticks(x, buses_new)
plt.ylabel('Reactive Power (MVAR)')
plt.title('Comparação de Potência Reativa: DR vs NR')
plt.legend()

# Gráfico 3: Comparação AC e NR
plt.subplot(2, 2, 3)
plt.bar(x - 0.2, reactive_power_NR_new, width=0.4, label='Reactive Power NR', color='blue')
plt.bar(x + 0.2, reactive_power_AC_new, width=0.4, label='Reactive Power AC', color='red')
plt.xticks(x, buses_new)
plt.ylabel('Reactive Power (MVAR)')
plt.title('Comparação de Potência Reativa: AC vs NR')
plt.legend()

# Gráfico 4: Comparação DC e NR
plt.subplot(2, 2, 4)
plt.bar(x - 0.2, reactive_power_NR_new, width=0.4, label='Reactive Power NR', color='blue')
plt.bar(x + 0.2, reactive_power_DC_new, width=0.4, label='Reactive Power DC', color='red')
plt.xticks(x, buses_new)
plt.ylabel('Reactive Power (MVAR)')
plt.title('Comparação de Potência Reativa: DC vs NR')
plt.legend()

plt.tight_layout()
plt.show()
