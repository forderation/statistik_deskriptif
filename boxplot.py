# library & dataset
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.ticker
sns.set_style(style="darkgrid")
df = pd.read_csv('kelas g.csv')
sns.pairplot(data=df)
ax = plt.gca()
ax.set_xlim([0,100])
ax.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(10))
ax.set_xlabel('nilai sesuai modul masing masing')
plt.suptitle('nilai keseluruhan praktikum pemrograman dasar kelas G')
plt.savefig('kelas g.png', dpi = 300)