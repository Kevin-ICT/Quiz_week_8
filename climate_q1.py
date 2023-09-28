import sqlite3
# Connect to the SQLite database
conn = sqlite3.connect('climate.db')
cursor = conn.cursor()

# Fetch data from the "ClimateData" table and populate lists
cursor.execute("SELECT Year, CO2, Temperature FROM ClimateData")
data = cursor.fetchall()

years = [row[0] for row in data]
co2 = [row[1] for row in data]
temp = [row[2] for row in data]

conn.close()


import matplotlib.pyplot as plt

# years = []
# co2 = []
# temp = []

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
plt.savefig("co2_temp_1.png") 
