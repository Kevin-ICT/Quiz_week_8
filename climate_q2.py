import matplotlib.pyplot as plt
import pandas as pd

years = []
co2 = []
temp = []

df = pd.read_csv(r"climate.csv")
for i in df['Temperature']:
    temp.append(i)

for i in df['CO2']:
    co2.append(i)

for i in df['Year']:
    years.append(i)

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")
plt.show()
plt.savefig("co2_temp_2.png")
