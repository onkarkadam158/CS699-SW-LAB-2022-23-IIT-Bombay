#!bin/usr/python

import csv
import sys

inputFile = sys.argv[1]

if (len(sys.argv) > 2):
    print("Usage: q1.py " + inputFile)
else:
    listOfList = [] 
    with open(inputFile , mode='r') as file:
        data = csv.reader(file)
        for lines in data:
            #print(lines)
            if(lines[0].isnumeric()):
                listOfList.append(lines)
    print(listOfList)
    print(len(listOfList))
 
#        2)
#Modify the previous program to store the main data (i.e. excluding the header rows) as a list of lists (2D array). Print this list of lists and then print the number of candidates appeared by using "len" function in the next line.
#What you are expected to learn: lists, list-of-lists, the len function
      
