#!bin/usr/python

import csv
import sys

selIndex = 0
def getLastColumn(temp):
    return temp

if (len(sys.argv) != 2):
    print("Usage: q1.py <csv-file-name>" )
    exit()
else:
    inputFile = sys.argv[1]
    extracted = []
    with open(inputFile , mode='r') as file:
        data = csv.reader(file)
        for lines in data:
            if(lines[0] == "Sno"):
                for i in range (0,len(lines)):
                    if(lines[i]== "Sel"):
                        selIndex = i
            if (lines[0].isnumeric()):
                extracted.append(lines)
                
    Seleted = map(getLastColumn,extracted)
    finalSeleted = []
    for lst in Seleted:
        finalSeleted.append(int(lst[selIndex]))

    print((finalSeleted))
    print(sum(finalSeleted))


# 3)
# Modify the previous program to make a list of only the final selected candidates. 
#Extract "Sel" column in a list. This list contains 0's and 1's as integers. 
#Use map on the list of lists to achieve this. 
#Print this list and then print the total number of selected candidates using the "sum" function on this list in the next line.
# What you are expected to learn: using map on a list.
      