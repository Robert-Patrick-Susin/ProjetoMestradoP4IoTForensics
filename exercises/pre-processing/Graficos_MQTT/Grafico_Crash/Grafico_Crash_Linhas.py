import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv
from matplotlib.patches import Polygon
plt.rcParams['font.size'] = 28

# Linhas de Baseline
X1 = []
Y1 = []

# Linhas de Agregação
X2 = []
Y2 = []
X3 = []
Y3 = []
X4 = []
Y4 = []

# 1 Linha - Baseline
with open('1X_med_tempo_passado.txt', 'r') as datafile:
    plotting = csv.reader(datafile)

    for ROWS in plotting:
        X1.append(int(ROWS[0]))
# Y nr total pkt        
with open('1Y_blocos_criados_baseline', 'r') as datafile:
    plotting = csv.reader(datafile)
     
    for ROWS in plotting:
        Y1.append(int(ROWS[0]))



# 2 Linha - Agregação (4)      
with open('2X_med_tempo_passado.txt', 'r') as datafile:
    plotting = csv.reader(datafile)

    for ROWS in plotting:
        X2.append(int(ROWS[0]))
# Y nr total pkt        
with open('2Y_blocos_criados_4agg', 'r') as datafile:
    plotting = csv.reader(datafile)
     
    for ROWS in plotting:
        Y2.append(int(ROWS[0]))



# 3 Linha - Agregação (8)     
with open('3X_med_tempo_passado.txt', 'r') as datafile:
    plotting = csv.reader(datafile)

    for ROWS in plotting:
        X3.append(int(ROWS[0]))
# Y nr total pkt 
with open('3Y_blocos_criados_8agg', 'r') as datafile:
    plotting = csv.reader(datafile)
     
    for ROWS in plotting:
        Y3.append(int(ROWS[0]))

# 4 Linha - Agregação (12)     
with open('4X_med_tempo_passado.txt', 'r') as datafile:
    plotting = csv.reader(datafile)

    for ROWS in plotting:
        X4.append(int(ROWS[0]))
# Y nr total pkt
with open('4Y_blocos_criados_12agg', 'r') as datafile:
    plotting = csv.reader(datafile)
    for ROWS in plotting:
        Y4.append(int(ROWS[0]))
     
# Marcar linhas Baseline
plt.plot(X1, Y1, label='Baseline')

# Marcar linhas com Agregação
plt.plot(X2, Y2, label='Agregação (4)')
plt.plot(X3, Y3, label='Agregação (8)')
plt.plot(X4, Y4, label='Agregação (12)')

plt.legend()
plt.grid(True)
plt.xlabel('Tempo (seg)')
plt.ylabel('Total de blocos criados na blockchain')
plt.show()
