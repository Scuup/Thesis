import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import img2pdf
import os

# This is where the data gets its meaning
dataNames=['Time1','Time2','Time3','byte','ID','D1','D2','D3','D4','D5','D6','D7','D8','end']
# Make a table out of the saved file
canTable = pd.read_csv('log.csv', delimiter = ',',names=dataNames)
# Drop nan values
canTable=canTable.dropna()
# Drop the byte and end values, comes from the serial communication
canTable = canTable.drop(columns=['byte','end'])



canTable['time'] = canTable.Time1.map(str) + canTable.Time2.map(str) + canTable.Time3.map(str)


#canTable['time'] = canTable['Time1'].str.cat(canTable[['Time2', 'Time3']], sep=' - ')
print(canTable)
print(canTable.info())
#plt.plot(canTable.time,canTable.D1, label='Loaded from file!')
#plt.show()
testing=canTable.loc[canTable['ID'] == 130]
print(testing)
plt.plot(testing.time,testing.D1)
plt.plot(testing.time,testing.D2)
plt.plot(testing.time,testing.D3)
plt.plot(testing.time,testing.D4)
plt.plot(testing.time,testing.D5)
plt.plot(testing.time,testing.D6)
plt.plot(testing.time,testing.D7)
plt.plot(testing.time,testing.D8)
plt.xticks(rotation=45)
#plt.locator_params(numticks=12)
plt.grid()
plt.show()
