import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv

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

# Linhas de Agregação
# X5 = []
# Y5 = []
# X6 = []
# Y6 = []
# X7 = []
# Y7 = []


# 1 Linha - Baseline
with open('1X_tempo_passado_seg', 'r') as datafile:
    plotting = csv.reader(datafile)

    for ROWS in plotting:
        X1.append(int(ROWS[0]))
# Y nr total pkt        
with open('1Y_med_blocos_criados_baseline', 'r') as datafile:
    plotting = csv.reader(datafile)
     
    for ROWS in plotting:
        Y1.append(int(ROWS[0]))



# 2 Linha - Agregação (4)      
with open('2X_tempo_passado_seg', 'r') as datafile:
    plotting = csv.reader(datafile)

    for ROWS in plotting:
        X2.append(int(ROWS[0]))
# Y nr total pkt        
with open('2Y_med_blocos_criados_4agg', 'r') as datafile:
    plotting = csv.reader(datafile)
     
    for ROWS in plotting:
        Y2.append(int(ROWS[0]))



# 3 Linha - Agregação (8)     
with open('3X_tempo_passado_seg', 'r') as datafile:
    plotting = csv.reader(datafile)

    for ROWS in plotting:
        X3.append(int(ROWS[0]))
# Y nr total pkt 
with open('3Y_med_blocos_criados_8agg', 'r') as datafile:
    plotting = csv.reader(datafile)
     
    for ROWS in plotting:
        Y3.append(int(ROWS[0]))

# 4 Linha - Agregação (12)     
with open('4X_tempo_passado_seg', 'r') as datafile:
    plotting = csv.reader(datafile)

    for ROWS in plotting:
        X4.append(int(ROWS[0]))
# Y nr total pkt
with open('4Y_med_blocos_criados_12agg', 'r') as datafile:
    plotting = csv.reader(datafile)
    for ROWS in plotting:
        Y4.append(int(ROWS[0]))

# # 5 Linha - Agregação (4) + Filtragem (75% dispositivos)
# # X nr de dispositivos
# with open('pacotes', 'r') as datafile:
#     plotting = csv.reader(datafile)

#     for ROWS in plotting:
#         X5.append(int(ROWS[0]))
# # Y nr total pkt 
# with open('5_blocos_agg_4agg_filt75', 'r') as datafile:
#     plotting = csv.reader(datafile)
     
#     for ROWS in plotting:
#         Y5.append(int(ROWS[0]))

# # 6 Linha - Agregação (8) + Filtragem (50% dispositivos)
# # X nr de dispositivos        
# with open('pacotes', 'r') as datafile:
#     plotting = csv.reader(datafile)

#     for ROWS in plotting:
#         X6.append(int(ROWS[0]))
# # Y nr total pkt 
# with open('6_blocos_agg_8agg_filt50', 'r') as datafile:
#     plotting = csv.reader(datafile)
     
#     for ROWS in plotting:
#         Y6.append(int(ROWS[0]))

# # 7 Linha - Agregação (12) + Filtragem (25% dispositivos)
# # X nr de dispositivos        
# with open('pacotes', 'r') as datafile:
#     plotting = csv.reader(datafile)

#     for ROWS in plotting:
#         X7.append(int(ROWS[0]))
# # Y nr total pkt 
# with open('7_blocos_agg_12agg_filt25', 'r') as datafile:
#     plotting = csv.reader(datafile)
     
#     for ROWS in plotting:
#         Y7.append(int(ROWS[0]))

        

# Marcar linhas Baseline
plt.plot(X1, Y1, label='Baseline')

# Marcar linhas com Agregação
plt.plot(X2, Y2, label='Agregação (4)')
plt.plot(X3, Y3, label='Agregação (8)')
plt.plot(X4, Y4, label='Agregação (12)')

# Marcar linhas com Filtragem + Agregação
# plt.plot(X5, Y5, 'o-', label='Agregação (4) + Filtragem (75% dispositivos) (workload h)')
# plt.plot(X6, Y6, 'o-', label='Agregação (8) + Filtragem (50% dispositivos) (workload i)')
# plt.plot(X7, Y7, 'o-', label='Agregação (12) + Filtragem (25% dispositivos) (workload j)')


plt.legend()
plt.grid(True)
plt.xlabel('Tempo (seg)')
plt.ylabel('Total de blocos criados na blockchain')
plt.show()
