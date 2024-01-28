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
with open('2Y_duracao_seg_300pkt', 'r') as datafile:
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
Y0agg_200pkt_tempo_10x = [59, 58, 59, 53, 54, 59, 55, 60, 57, 55]
plt.boxplot((Y0agg_200pkt_tempo_10x), positions=[0])

Y2agg_200pkt_tempo_10x = [42, 38, 38, 36, 35, 37, 35, 37, 36, 36]
plt.boxplot((Y2agg_200pkt_tempo_10x), positions=[2])

Y4agg_200pkt_tempo_10x = [15, 14, 12, 20, 17, 18, 19, 19, 17, 19]
plt.boxplot((Y4agg_200pkt_tempo_10x), positions=[4])

Y6agg_200pkt_tempo_10x = [12, 9, 8, 8, 8, 9, 9, 9, 9, 8]
plt.boxplot((Y6agg_200pkt_tempo_10x), positions=[6])

Y8agg_200pkt_tempo_10x = [9, 6, 6, 7, 7, 6, 6, 6, 7, 6]
plt.boxplot((Y8agg_200pkt_tempo_10x), positions=[8])

Y10agg_200pkt_tempo_10x = [5, 6, 5, 5, 5, 4, 4, 4, 5, 4]
plt.boxplot((Y10agg_200pkt_tempo_10x), positions=[10])

Y12agg_200pkt_tempo_10x = [3, 3, 5, 3, 5, 5, 3, 3, 4, 5]
plt.boxplot((Y12agg_200pkt_tempo_10x), positions=[12])

# Boxplot's 300pkt
Y0agg_300pkt_tempo_10x = [63, 63, 63, 61, 70, 69, 73, 68, 71, 70]
plt.boxplot((Y0agg_300pkt_tempo_10x), positions=[0])

Y2agg_300pkt_tempo_10x = [52, 52, 48, 53, 53, 55, 58, 50, 39, 39]
plt.boxplot((Y2agg_300pkt_tempo_10x), positions=[2])

Y4agg_300pkt_tempo_10x = [31, 29, 27, 27, 28, 28, 27, 31, 26, 29]
plt.boxplot((Y4agg_300pkt_tempo_10x), positions=[4])

Y6agg_300pkt_tempo_10x = [13, 17, 17, 17, 15, 17, 14, 19, 16, 17]
plt.boxplot((Y6agg_300pkt_tempo_10x), positions=[6])

Y8agg_300pkt_tempo_10x = [9, 10, 9, 10, 11, 11, 11, 11, 11, 9]
plt.boxplot((Y8agg_300pkt_tempo_10x), positions=[8])

Y10agg_300pkt_tempo_10x = [6, 7, 7, 8, 12, 5, 10, 10, 10, 11]
plt.boxplot((Y10agg_300pkt_tempo_10x), positions=[10])

Y12agg_300pkt_tempo_10x = [7, 6, 6, 6, 7, 8, 6, 7, 9, 7]
plt.boxplot((Y12agg_300pkt_tempo_10x), positions=[12])

# Boxplot's 400pkt
Y0agg_400pkt_tempo_10x = [98, 83, 84, 92, 103, 104, 98, 99, 83]
plt.boxplot((Y0agg_400pkt_tempo_10x), positions=[0])

Y2agg_400pkt_tempo_10x = [56, 74, 72, 71, 58, 60, 59, 75, 75, 85]
plt.boxplot((Y2agg_400pkt_tempo_10x), positions=[2])

Y4agg_400pkt_tempo_10x = [42, 34, 35, 35, 36, 41, 38, 38, 44, 43]
plt.boxplot((Y4agg_400pkt_tempo_10x), positions=[4])

Y6agg_400pkt_tempo_10x = [24, 31, 20, 20, 21, 22, 18, 20, 19, 18]
plt.boxplot((Y6agg_400pkt_tempo_10x), positions=[6])

Y8agg_400pkt_tempo_10x = [14, 16, 16, 14, 16, 15, 13, 18, 14, 13]
plt.boxplot((Y8agg_400pkt_tempo_10x), positions=[8])

Y10agg_400pkt_tempo_10x = [10, 8, 9, 10, 10, 11, 10, 12, 12, 10]
plt.boxplot((Y10agg_400pkt_tempo_10x), positions=[10])

Y12agg_400pkt_tempo_10x = [7, 9, 9, 8, 8, 10, 7, 7, 7, 7]
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