#!bin/usr/python

import csv
import sys

inputFile = sys.argv[1]

if (len(sys.argv) != 2):
    print("Usage: q1.py <csv-file-name>")
    exit()
else:
    result = []
    with open(inputFile , mode='r') as file:
        data = csv.reader(file)
        indexlist = []
        for line in data:
            if(line[0]=="Sno"):
                for i in range (0,len(line)):
                    if(line[i]== "Math" or line[i]== "CS" or line[i]== "GK" or line[i]== "Prog" or line[i]== "Comm" ):
                        indexlist.append(i)
            if(line[0].isnumeric()):
                sum = 0
                for i in indexlist:
                    if(line[i] != "NA"):
                        sum = sum + float(line[i])
                line.append((sum))
                result.append(line)
    result.reverse()
    result.sort(key=lambda row: row[7])
    result.reverse()
    with open("output.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(result)
    #print(result)
    


#6)
# Modify the previous program to store an extra column in each row, which is the total marks obtained by the candidate (count "NA" as 0 marks). 
# Then sort the list-of-lists by the total marks obtained by each candidate. Print this sorted list onto a new file in csv format named as "output.csv".
# What you are expected to learn: sorting a list using the "sort" command, and using a lambda function to specify the key, using csv writer
      