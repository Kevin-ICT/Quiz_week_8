import matplotlib.pyplot as plt
import sqlite3

years = []
co2 = []
temp = []

connection = sqlite3.connect("climate.db")
cursor = connection.cursor()


cursor.execute("SELECT Temperature FROM ClimateData")
result = cursor.fetchall()
for i in result:
    temp.append(i)

cursor.execute("SELECT Co2 FROM ClimateData")
result = cursor.fetchall()
for i in result:
    co2.append(i)

cursor.execute("SELECT Year FROM ClimateData")
result = cursor.fetchall()
for i in result:
    years.append(i)

def printRes(r):
    for l in r:
        print(l)
    print()


sql_cmd = """
SELECT * FROM ClimateData WHERE Temperature > '17';
"""

cursor.execute(sql_cmd)
res = cursor.fetchall()
printRes(res)

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
