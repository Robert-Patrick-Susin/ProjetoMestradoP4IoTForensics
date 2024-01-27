import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv
from matplotlib.patches import Polygon

# Linhas
X1 = []
Y1 = []
X2 = []
Y2 = []
X3 = []
Y3 = []

# 1 Linha - Baseline
with open('X_agg', 'r') as datafile:
    plotting = csv.reader(datafile)

    for ROWS in plotting:
        X1.append(int(ROWS[0]))
# Y nr total pkt        
with open('1Y_duracao_seg_200pkt', 'r') as datafile:
    plotting = csv.reader(datafile)
     
    for ROWS in plotting:
        Y1.append(int(ROWS[0]))

# 2 Linha - 300 pkt
with open('X_agg', 'r') as datafile:
    plotting = csv.reader(datafile)

    for ROWS in plotting:
        X2.append(int(ROWS[0]))
# Y nr total pkt        
with open('2Y_duracao_seg_400pkt', 'r') as datafile:
    plotting = csv.reader(datafile)
     
    for ROWS in plotting:
        Y2.append(int(ROWS[0]))


# 3 Linha - 400 pkt
with open('X_agg', 'r') as datafile:
    plotting = csv.reader(datafile)

    for ROWS in plotting:
        X3.append(int(ROWS[0]))
# Y nr total pkt 
with open('3Y_duracao_seg_400pkt', 'r') as datafile:
    plotting = csv.reader(datafile)
     
    for ROWS in plotting:
        Y3.append(int(ROWS[0]))


# Boxplot's 200pkt
Y0agg_200pkt_tempo_10x = [, , , , , , , , ,]
plt.boxplot((Y0agg_200pkt_tempo_10x), positions=[0])

Y2agg_200pkt_tempo_10x = [, , , , , , , , ,]
plt.boxplot((Y2agg_200pkt_tempo_10x), positions=[2])

Y4agg_200pkt_tempo_10x = [, , , , , , , , ,]
plt.boxplot((Y4agg_200pkt_tempo_10x), positions=[4])

Y6agg_200pkt_tempo_10x = [, , , , , , , , ,]
plt.boxplot((Y6agg_200pkt_tempo_10x), positions=[6])

Y8agg_200pkt_tempo_10x = [, , , , , , , , ,]
plt.boxplot((Y8agg_200pkt_tempo_10x), positions=[8])

Y10agg_200pkt_tempo_10x = [, , , , , , , , ,]
plt.boxplot((Y10agg_200pkt_tempo_10x), positions=[10])

Y12agg_200pkt_tempo_10x = [, , , , , , , , ,]
plt.boxplot((Y12agg_200pkt_tempo_10x), positions=[12])

# Boxplot's 300pkt
Y0agg_300pkt_tempo_10x = [, , , , , , , , ,]
plt.boxplot((Y0agg_300pkt_tempo_10x), positions=[0])

Y2agg_300pkt_tempo_10x = [, , , , , , , , ,]
plt.boxplot((Y2agg_300pkt_tempo_10x), positions=[2])

Y4agg_300pkt_tempo_10x = [, , , , , , , , ,]
plt.boxplot((Y4agg_300pkt_tempo_10x), positions=[4])

Y6agg_300pkt_tempo_10x = [, , , , , , , , ,]
plt.boxplot((Y6agg_300pkt_tempo_10x), positions=[6])

Y8agg_300pkt_tempo_10x = [, , , , , , , , ,]
plt.boxplot((Y8agg_300pkt_tempo_10x), positions=[8])

Y10agg_300pkt_tempo_10x = [, , , , , , , , ,]
plt.boxplot((Y10agg_300pkt_tempo_10x), positions=[10])

Y12agg_300pkt_tempo_10x = [, , , , , , , , ,]
plt.boxplot((Y12agg_300pkt_tempo_10x), positions=[12])

# Boxplot's 400pkt
Y0agg_400pkt_tempo_10x = [, , , , , , , , ,]
plt.boxplot((Y0agg_400pkt_tempo_10x), positions=[0])

Y2agg_400pkt_tempo_10x = [, , , , , , , , ,]
plt.boxplot((Y2agg_400pkt_tempo_10x), positions=[2])

Y4agg_400pkt_tempo_10x = [, , , , , , , , ,]
plt.boxplot((Y4agg_400pkt_tempo_10x), positions=[4])

Y6agg_400pkt_tempo_10x = [, , , , , , , , ,]
plt.boxplot((Y6agg_400pkt_tempo_10x), positions=[6])

Y8agg_400pkt_tempo_10x = [, , , , , , , , ,]
plt.boxplot((Y8agg_400pkt_tempo_10x), positions=[8])

Y10agg_400pkt_tempo_10x = [, , , , , , , , ,]
plt.boxplot((Y10agg_400pkt_tempo_10x), positions=[10])

Y12agg_400pkt_tempo_10x = [, , , , , , , , ,]
plt.boxplot((Y12agg_400pkt_tempo_10x), positions=[12])

# Linhas plots
plt.plot(X1, Y1, label='200 pkt enviados')
plt.plot(X2, Y2, label='300 pkt enviados')
plt.plot(X3, Y3, label='400 pkt enviados')

plt.legend()
plt.grid(True)
plt.xlabel('Agregações (por pkt)')
plt.ylabel('Duração de armazenamento (seg)')
plt.show()