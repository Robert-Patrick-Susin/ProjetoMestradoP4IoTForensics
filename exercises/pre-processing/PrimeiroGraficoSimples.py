import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv

X = []
Y = []
X2 = []
Y2 = []

# Linha com agregação
with open('pkt_por_seg.txt', 'r') as datafile:
    plotting = csv.reader(datafile)

    for ROWS in plotting:
        X.append(int(ROWS[0]))

with open('med_tx_receb_pkt.txt', 'r') as datafile:
    plotting = csv.reader(datafile)
     
    for ROWS in plotting:
        Y.append(float(ROWS[0]))

# Linha sem agreação
with open('pkt_por_seg.txt', 'r') as datafile:
    plotting = csv.reader(datafile)

    for ROWS in plotting:
        X2.append(int(ROWS[0]))

with open('no_med_tx_receb_pkt.txt', 'r') as datafile:
    plotting = csv.reader(datafile)
     
    for ROWS in plotting:
        Y2.append(float(ROWS[0]))    

plt.plot(X, Y)
plt.plot(X2, Y2)
plt.title('Envio de 10/100/1000 pacotes sensíveis (10 banco)')
plt.xlabel('Pacotes enviados por segundo (s)')
plt.ylabel('Média taxa de recebimento (m/s)')
plt.show()