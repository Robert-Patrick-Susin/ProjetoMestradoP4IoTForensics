import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv

# Linhas de Agregação Registradores
Xar = []
Yar = []
X2ar = []
Y2ar = []
X3ar = []
Y3ar = []


# 1 Linha - Agregação e Registradores(40 pacotes por segundo)
# X nr de dispositivos
with open('../metricas/registradores_iot.txt', 'r') as datafile:
    plotting = csv.reader(datafile)

    for ROWS in plotting:
        Xar.append(int(ROWS[0]))
# Y nr total pkt        
with open('../../pre-processing/metricas/1-pre_med_rec_pkt.txt', 'r') as datafile:
    plotting = csv.reader(datafile)
     
    for ROWS in plotting:
        Yar.append(float(ROWS[0]))



# 2 Linha - Agregação e Registradores(70 pacotes por segundo)
# X nr de dispositivos        
with open('../metricas/registradores_iot.txt', 'r') as datafile:
    plotting = csv.reader(datafile)

    for ROWS in plotting:
        X2ar.append(int(ROWS[0]))
# Y nr total pkt        
with open('../../pre-processing/metricas/2-pre_med_rec_pkt.txt', 'r') as datafile:
    plotting = csv.reader(datafile)
     
    for ROWS in plotting:
        Y2ar.append(float(ROWS[0]))



# 3 Linha - Agregação e Registradores(110 pacotes por segundo)
# X nr de dispositivos        
with open('../metricas/registradores_iot.txt', 'r') as datafile:
    plotting = csv.reader(datafile)

    for ROWS in plotting:
        X3ar.append(int(ROWS[0]))
# Y nr total pkt 
with open('../../pre-processing/metricas/3-pre_med_rec_pkt.txt', 'r') as datafile:
    plotting = csv.reader(datafile)
     
    for ROWS in plotting:
        Y3ar.append(float(ROWS[0]))


      
# Marcar linhas com Agregação e Registradores
plt.plot(Xar, Yar, 'o-', label='Agregação (workload d)')
plt.plot(X2ar, Y2ar, 'o-', label='Agregação (workload e)')
plt.plot(X3ar, Y3ar, 'o-', label='Agregação (workload f)')

plt.legend()
plt.grid(True)
plt.xlabel('Tamanho do vetor registrador banco')
plt.ylabel('Tempo de chegada pkt receb. Plano de Controle (seg)')
plt.show()