import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("18esc_elsalado.csv", sep=";")
df['fecha_'] = pd.to_datetime(df[' fecha      '] + ' ' + df[' hora     '])
print(df)
print(df.columns)

# Datos en listas
fechas = pd.to_datetime(df['fecha_'].tolist())
fechas = df[' hora     '].tolist()
p1 = (df[' p1/1000 ']/1000).values
p2 = (df[' p2/1000 ']/1000).values

figura = plt.figure(figsize=[15, 10])
plt.plot(fechas, p1, linewidth=3, label='Pluviometro 1')
plt.hold(True)
plt.plot(fechas, p2, linewidth=3, label='Pluviometro 2')
plt.xlabel("Hora", fontsize=24)
plt.ylabel("Acumulados (mm/min)", fontsize=24)
plt.title("18. Escuela El Salado", fontsize=30)
plt.grid(True)
plt.legend()
plt.yticks(size='large')
plt.xticks(size='large')
plt.gcf().autofmt_xdate()
plt.savefig("/home/luis/elsalado.png", dpi=200)
plt.show()
