import matplotlib.pyplot as plt
import sqlite3 as sql
        
years = []
co2 = []
temps = []

sqlConn = sql.connect('climate.db')
cursor = sqlConn.cursor()

queryYear = 'Select Year FROM ClimateData'
queryco2 = 'Select co2 from ClimateData'
querytemp = 'Select temp from ClimateData'

cursor.execute(queryYear)
year = cursor.fetchall()
years = [i[0] for i in year]

cursor.execute(queryco2)
co = cursor.fetchall()
co2 = years = [i[0] for i in co]

cursor.execute(queryco2)
temp = cursor.fetchall()
temps = [i[0] for i in temp]

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
