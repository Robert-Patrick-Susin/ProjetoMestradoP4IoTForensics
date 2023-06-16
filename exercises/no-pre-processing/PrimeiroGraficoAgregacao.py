import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv

X = []
Y = []

# Linha com agregação
with open('nopre_dispositivos_iot.txt', 'r') as datafile:
    plotting = csv.reader(datafile)

    for ROWS in plotting:
        X.append(int(ROWS[0]))

with open('nopre_total_pkt.txt', 'r') as datafile:
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