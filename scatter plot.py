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
data = pandas.read_csv('kelas f.csv',names=colnames, header=None)

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
labels = ['Modul 1', 'Modul 2', 'Modul 3', 'Modul 4', 'Modul 5', 'Modul 6']
sizes = [rmodul1, rmodul2, rmodul3, rmodul4, rmodul5, rmodul6]

import seaborn as sns
sns.set_style("whitegrid")
blue, = sns.color_palette("muted", 1)
from matplotlib import pyplot as plt
fig, ax = plt.subplots()
ax.scatter(labels, sizes)
for i, txt in enumerate(sizes):
    txt = round(txt,2)
    ax.annotate(txt, (labels[i], sizes[i]))
plt.plot(labels, sizes, marker='o', color='mediumvioletred')
plt.suptitle('persentase rata rata nilai modul praktikum \nkelas F menggunakan line plot')
plt.savefig('lineplot/kelas f.png', dpi = 300)
