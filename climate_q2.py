import matplotlib.pyplot as plt
import pandas as pd
import csv

years = []
co2 = []
temp = []

with open('climate.csv', 'r') as file:
  reader = csv.reader(file)
  next(reader)
  for row in reader:
    years.append(int(row[0]))
    co2.append(float(row[1]))
    temp.append(float(row[2]))

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 

