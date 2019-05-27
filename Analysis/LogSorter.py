
#This works and sorts the datasets
#In addtition lets eplore directory creations with : folderfordata.py
#putting them together to one file multipleJPGinto PDF
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import img2pdf
import os

# This is where the data gets its meaning
dataNames=['Time1','Time2','Time3','Time4','ID','D1','D2','D3','D4','D5','D6','D7','D8','end']
# Make a table out of the saved file
canTable = pd.read_csv('log.csv', delimiter = ',',names=dataNames)

print(canTable)
#canTable.ID = canTable.ID.astype(float)
canTable_Test=canTable.dropna()
#print(canTable)
# Change this to true and you get a dataset in a txt file for each ID
iterate = True

## By changing this "sortedByID" you can make a table that has only one
    ## ID and its dataset
#sortParameter = 1034
#sortedByID = canTable_Test[canTable_Test.ID == sortParameter]

## uniqueID has all the unique ID's that the dataset has
uniqueID = canTable_Test.ID.unique()
uniqueID = uniqueID[~pd.isnull(uniqueID)]
sortedUniqueID=np.sort(uniqueID)
#print(sortedUniqueID)
#print(type(sortedUniqueID))
canTable['D1'] = canTable['D1'].astype(float)
print(canTable.info())
## This for loop iterates through the dataset and makes a txt.file for each
    ## ID and its dataset, for further things...
if iterate == True:
    for item in sortedUniqueID:
        print("This is list for ID:")
        print(item)
        sorting = canTable_Test[canTable_Test.ID == item]
        #print(sorting)
        #print(len(sorting))
        #print(type(sorting))
        print("--------------------")


        ##!!!!!! UNCOMMENT THIS TO MAKE TXT FOR EACH FILE!!!!!!!!!#######
        np.savetxt(r'np{}.txt'.format(item), sorting.values, fmt='%s')
        sorting = sorting.drop(columns=["Time1","Time2","Time3","Time4","ID"])

        #This is test for dropping the ID from the plot!!!
        #sorting = sorting.drop(columns=["Time"])
        #print(sorting)
        #sorting = sorting.drop(columns="Time")
        #print(sorting)
        #!!!

        sorting.plot(title="Sorted ID plot:{}".format(item))
        plt.savefig("{}.jpg".format(item))



# Print a plot of the dataset, from the ID that is defined in sortedByID
#sortedByID.plot(title="Sorted ID plot:{}".format(sortParameter))
#plt.savefig("{}.png".format(sortParameter))
#plt.show()

path="E:\Aalto\Lopputyö\Python_Projects\Logit"
os.chdir(path)
testVar="lol"
with open("OneFileToRuleThemAll.pdf", "wb") as f:
    listPhotos = [i for i in os.listdir(os.getcwd()) if i.endswith(".jpg")]
    sortedListPhotos = sorted(listPhotos,key=lambda x: int(os.path.splitext(x)[0]))
    #os.path.splitext on '10.jpg' returns ['10','.jpg'] so taking the int()
        #of element zero will give you want you want as long as the filenames without the
        #extention only contain strings that can be converted to integers with int().
    f.write(img2pdf.convert(sortedListPhotos))
