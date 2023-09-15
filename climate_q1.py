import sqlite3
import matplotlib.pyplot as plt
# connecting to the database
conn = sqlite3.connect('climate.db')
cursor = conn.cursor()

#SQL query to select data from climate data base
cursor.execute('SELECT * FROM ClimateData')
data = cursor.fetchall()

# close it
conn.close()

years = []
co2 = []
temp = []

for row in data:
    years.append(row[0])
    co2.append(row[1])
    temp.append(row[2])

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)")

plt.tight_layout()
plt.show()

plt.savefig("co2_temp_1.png")
