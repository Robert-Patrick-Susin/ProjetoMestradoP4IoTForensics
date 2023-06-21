import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv

# Linhas de Baseline
Xb = []
Yb = []
X2b = []
Y2b = []
X3b = []
Y3b = []

# Linhas de Filtragem
Xa = []
Ya = []
X2a = []
Y2a = []
X3a = []
Y3a = []


# 1 Linha - Baseline (1 pacotes por segundo)
# X nr de dispositivos
with open('dispositivos_iot.txt', 'r') as datafile:
    plotting = csv.reader(datafile)

    for ROWS in plotting:
        Xb.append(int(ROWS[0]))
# Y nr total pkt        
with open('1-nopre_total_pkt.txt', 'r') as datafile:
    plotting = csv.reader(datafile)
     
    for ROWS in plotting:
        Yb.append(int(ROWS[0]))



# 2 Linha - Baseline (2 pacotes por segundo)
# X nr de dispositivos        
with open('dispositivos_iot.txt', 'r') as datafile:
    plotting = csv.reader(datafile)

    for ROWS in plotting:
        X2b.append(int(ROWS[0]))
# Y nr total pkt        
with open('2-nopre_total_pkt.txt', 'r') as datafile:
    plotting = csv.reader(datafile)
     
    for ROWS in plotting:
        Y2b.append(int(ROWS[0]))



# 3 Linha - Baseline (3 pacotes por segundo)
# X nr de dispositivos        
with open('dispositivos_iot.txt', 'r') as datafile:
    plotting = csv.reader(datafile)

    for ROWS in plotting:
        X3b.append(int(ROWS[0]))
# Y nr total pkt 
with open('3-nopre_total_pkt.txt', 'r') as datafile:
    plotting = csv.reader(datafile)
     
    for ROWS in plotting:
        Y3b.append(int(ROWS[0]))

# 4 Linha - Filtragem 4 registradores (1 pacotes por segundo)
# X nr de dispositivos        
with open('dispositivos_iot.txt', 'r') as datafile:
    plotting = csv.reader(datafile)

    for ROWS in plotting:
        Xa.append(int(ROWS[0]))
# Y nr total pkt
with open('../pre-processing/1-pre_filt_total_pkt.txt', 'r') as datafile:
    plotting = csv.reader(datafile)
    for ROWS in plotting:
        Ya.append(int(ROWS[0]))

# 5 Linha - Filtragem 4 registradores (2 pacotes por segundo)
# X nr de dispositivos
with open('dispositivos_iot.txt', 'r') as datafile:
    plotting = csv.reader(datafile)

    for ROWS in plotting:
        X2a.append(int(ROWS[0]))
# Y nr total pkt 
with open('../pre-processing/2-pre_filt_total_pkt.txt', 'r') as datafile:
    plotting = csv.reader(datafile)
     
    for ROWS in plotting:
        Y2a.append(int(ROWS[0]))

# 6 Linha - Filtragem 4 registradores (3 pacotes por segundo)
# X nr de dispositivos        
with open('dispositivos_iot.txt', 'r') as datafile:
    plotting = csv.reader(datafile)

    for ROWS in plotting:
        X3a.append(int(ROWS[0]))
# Y nr total pkt 
with open('../pre-processing/3-pre_filt_total_pkt.txt', 'r') as datafile:
    plotting = csv.reader(datafile)
     
    for ROWS in plotting:
        Y3a.append(int(ROWS[0]))

        

# Marcar linhas Baseline
plt.plot(Xb, Yb, 'o-', label='Baseline (workload a)')
plt.plot(X2b, Y2b, 'o-', label='Baseline (workload b)')
plt.plot(X3b, Y3b, 'o-', label='Baseline (workload c)')

# Marcar linhas com Filtragem
plt.plot(Xa, Ya, 'o-', label='Filtragem (workload a)')
plt.plot(X2a, Y2a, 'o-', label='Filtragem (workload b)')
plt.plot(X3a, Y3a, 'o-', label='Filtragem (workload c)')

plt.legend()
plt.grid(True)
plt.xlabel('Número de dispositivos IoT')
plt.ylabel('Total pkt receb. Plano de Controle (20 segundos)')
plt.show()