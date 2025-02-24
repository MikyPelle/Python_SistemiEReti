import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import csv

mesi_n = []
temp = []
giacca = []
gio_gioco = []
scuola = []

data_file = open("edCiv1.csv")
data_reader = csv.reader(data_file, delimiter=',')
next(data_reader)
for row in data_reader: 
    mesi_n.append(int(row[1]))
    temp.append(float(row[2]))
    giacca.append(int(row[3]))
    gio_gioco.append(int(row[4]))
    scuola.append(int(row[5]))
data_file.close()
    
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1)
fig.suptitle('Correlazione e causalità')

ax1.plot(mesi_n, temp, 'red')
ax1.set_xlabel('Mese')
ax1.set_ylabel('Temperatura\nmedia °C')
ax1.grid()
ax1.set_ylim(0, 40)

ax2.plot(mesi_n, giacca, 'green')
ax2.set_xlabel('Mese')
ax2.set_ylabel('Giorni con\nla giacca')
ax2.grid()
ax2.set_ylim(0, 40)

ax3.plot(mesi_n, gio_gioco, 'blue')
ax3.set_xlabel('Mese')
ax3.set_ylabel('Giorni di gioco')
ax3.grid()
ax3.set_ylim(0, 40)

ax4.plot(mesi_n, scuola, 'yellow')
ax4.set_xlabel('Mese')
ax4.set_ylabel('Giorni di scuola')
ax4.grid()
ax4.set_ylim(0, 40)

plt.show()