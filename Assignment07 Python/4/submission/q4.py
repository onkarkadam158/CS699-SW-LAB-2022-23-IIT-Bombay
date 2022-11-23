#!bin/usr/python

import csv
import sys

selIndex = 0
inputFile = sys.argv[1]

def getLastColumn(temp):
    if(temp[selIndex] == '1'):
        return True
    else:
        return False

if (len(sys.argv) != 2):
    print("Usage: q1.py <csv-file-name>" )
    exit()
else:
    extractSelected = []
    with open(inputFile , mode='r') as file:
        data = csv.reader(file)
        for lines in data:
            if(lines[0] == "Sno"):
                for i in range (0,len(lines)):
                    if(lines[i]== "Sel"):
                        selIndex = i
            if (lines[0].isnumeric()):
                extractSelected.append(lines)
    Seleted = filter(getLastColumn,extractSelected)
    finalSeleted = []
    for lst in Seleted:
        if(lst != None ):
            finalSeleted.append(lst)
    print(finalSeleted)
    print(len(finalSeleted))


#        4)

#Modify the previous program to make another 2D matrix. This should consist of the rows corresponding to only the selected candidates. Use the filter function to achieve this. Print this list of lists and then print the total number of selected candidates by using "len" on this 2D matrix.
#What you are expected to learn: using filter on a list
      
