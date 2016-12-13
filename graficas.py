import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
from matplotlib.dates import DateFormatter

df = pd.read_csv("2esc_laverde.csv", sep=";")
df['fecha_'] = pd.to_datetime(df[' fecha      '] + ' ' + (df[' hora     ']))
print(df)
print(df.columns)

# Datos en listas
fechas = pd.to_datetime(df['fecha_'].values)

p1 = (df[' p1/1000 ']*0.01).values
p2 = (df[' p2/1000 ']*0.01).values

fig = plt.figure(figsize=[15, 10])
ax = fig.add_subplot(111)
ax.plot(fechas, p1, linewidth=3, label='Pluviometro 1')
# ax.hold(True)
ax.plot(fechas, p2, linewidth=3, label='Pluviometro 2')
ax.set_xlabel("Hora", fontsize=24)
ax.yaxis.set_major_formatter(ScalarFormatter(useOffset=False))
ax.xaxis.set_major_formatter(DateFormatter('%H:%m'))
ax.set_ylabel("Acumulados (mm/min)", fontsize=24)
ax.set_title("2. Escuela Rural La Verde", fontsize=30)
ax.grid(True)
ax.legend()
ax.tick_params(direction='out', labelsize='large')

# plt.savefig("/home/luis/laverde.png", dpi=300)
plt.show()
