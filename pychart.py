import matplotlib.pyplot as plt
import pandas

def rerataModul(modul):
    modul = modul[1:]
    kosong = 0
    rmodul = 0
    for nilai in modul:
        nilai = int(nilai)
        if (nilai != 0):
            rmodul = rmodul + nilai
        else:
            kosong += 1
    rmodul = rmodul / (len(modul) - kosong)
    return rmodul

colnames = ['Modul1','Modul2','Modul3','Modul4','Modul5','Modul6']
data = pandas.read_csv('kelas g.csv',names=colnames, header=None)
modul1 = data.Modul1.tolist()
rmodul1 = rerataModul(modul1)

modul2 = data.Modul2.tolist()
rmodul2 = rerataModul(modul2)

modul3 = data.Modul3.tolist()
rmodul3 = rerataModul(modul3)

modul4 = data.Modul4.tolist()
rmodul4 = rerataModul(modul4)

modul5 = data.Modul5.tolist()
rmodul5 = rerataModul(modul5)

modul6 = data.Modul6.tolist()
rmodul6 = rerataModul(modul6)

#Data to plot
labels = 'Modul 1', 'Modul 2', 'Modul 3', 'Modul 4', 'Modul 5', 'Modul 6'
sizes = [rmodul1, rmodul2, rmodul3, rmodul4, rmodul5, rmodul6]
colors = ['orchid', 'orange', 'green', 'olive', 'cyan', 'sandybrown']

# Plot
plt.pie(sizes, labels=labels, colors=colors,autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.suptitle('persentase rata rata nilai modul praktikum \nkelas G tanpa nilai yang belum demo')
plt.savefig('kelas g.png', dpi = 300)