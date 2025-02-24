import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import csv

annoT = []
temp = []
annoG = []
gas = []
annoI = []
infl = []

data_file = open("dataTemp.csv")
data_reader = csv.reader(data_file, delimiter=',')
next(data_reader)
for row in data_reader: 
    annoT.append(int(row[0]))
    temp.append(float(row[1]))
data_file.close()

data_file = open("dataMetano.csv")
data_reader = csv.reader(data_file, delimiter=',')
next(data_reader)
for row in data_reader: 
    annoG.append(int(row[0]))
    gas.append(float(row[1]))
data_file.close()

data_file = open("dataInfl.csv")
data_reader = csv.reader(data_file, delimiter=',')
next(data_reader)
for row in data_reader: 
    annoI.append(int(row[0]))
    infl.append(float(row[1]))
data_file.close()
    
fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
fig.suptitle('Correlazione e causalità')

ax1.plot(annoT, temp, "r")
ax1.set_xlabel('anno')
ax1.set_ylabel('Variazione\ntemperatura °C')
ax1.grid()
ax1.set_ylim(-0.5, 1.5)

ax3.plot(annoG, gas, 'green')
ax3.set_xlabel('anno')
ax3.set_ylabel('Incremento\ngas metano')
ax3.grid()
ax3.set_ylim(1600, 2000)

ax2.plot(annoI, infl, 'blue')
ax2.set_xlabel('anno')
ax2.set_ylabel('Inflazione\nargentina')
ax2.grid()

plt.show()