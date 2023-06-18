import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv

X = []
Y = []

# 1 Linha - Baseline (Workload (a) 1 pacotes por segundo)
# X nr de dispositivos
with open('dispositivos_iot.txt', 'r') as datafile:
    plotting = csv.reader(datafile)

    for ROWS in plotting:
        X.append(int(ROWS[0]))
# Y nr total pkt        
with open('1-nopre_total_pkt.txt', 'r') as datafile:
    plotting = csv.reader(datafile)
     
    for ROWS in plotting:
        Y.append(int(ROWS[0]))



# 2 Linha - Baseline (Workload (b) 2 pacotes por segundo)
# X nr de dispositivos        
with open('dispositivos_iot.txt', 'r') as datafile:
    plotting = csv.reader(datafile)

    for ROWS in plotting:
        X.append(int(ROWS[0]))
# Y nr total pkt        
with open('2-nopre_total_pkt.txt', 'r') as datafile:
    plotting = csv.reader(datafile)
     
    for ROWS in plotting:
        Y.append(int(ROWS[0]))



# 3 Linha - Baseline (Workload (b) 3 pacotes por segundo)
# X nr de dispositivos        
with open('dispositivos_iot.txt', 'r') as datafile:
    plotting = csv.reader(datafile)

    for ROWS in plotting:
        X.append(int(ROWS[0]))
# Y nr total pkt        
with open('3-nopre_total_pkt.txt', 'r') as datafile:
    plotting = csv.reader(datafile)
     
    for ROWS in plotting:
        Y.append(int(ROWS[0]))

        

plt.plot(X, Y, label='Sem agregação')
plt.scatter(X, Y)
plt.legend()
plt.grid(True)
plt.xlabel('Número de dispositivos IoT')
plt.ylabel('Total pkt receb. Plano de Controle')
plt.show()