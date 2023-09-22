#q1
import sqlite3
import matplotlib.pyplot as plt

connection = sqlite3.connect('climate.db')
cursor = connection.cursor()
cursor.execute("SELECT year, co2, temp FROM climate_data")
climate_data = cursor.fetchall()

years = [row[0] for row in climate_data]
co2_levels = [row[1] for row in climate_data]
temperature = [row[2] for row in climate_data]
connection.close()

plt.subplot(2, 1, 1)
plt.plot(years, co2_levels, 'b--')
plt.title("Climate Data")
plt.ylabel("CO2 Levels")
plt.xlabel("Year (Decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temperature, 'r*-')
plt.ylabel("Temperature (°C)")
plt.xlabel("Year (Decade)")

plt.show()
plt.savefig("climate_data_plot.png")
