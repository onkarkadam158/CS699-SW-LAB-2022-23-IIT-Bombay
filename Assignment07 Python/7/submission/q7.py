#!bin/usr/python

import csv
import sys
import math

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
    OverallM=result

    Num_of_top20Rows=math.ceil(len(OverallM)*0.2)
    top20pM=OverallM[0:Num_of_top20Rows]

    with open("top20.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(top20pM)

    Num_of_bot40Rows=math.ceil(len(OverallM)*0.6)
    bot40pM=OverallM[Num_of_bot40Rows:]

    with open("bot40.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(bot40pM)


    #print(result)
 
# 7)
# Add to the previous program to create two separate 2D matrices: one with the top 20% of candidates (by total marks), 
# and another with the bottom 40% of candidates (by total marks). Use ceil() to determine number of rows in each case. 
# You can create these as sub-lists of the above sorted matrix. For convenience, call the 3 matrices as OverallM, top20pM, and bot40pM respectively. 
# Print these sorted list onto separate files in csv format.
# (Output filenames: top20pM : "top20.csv", bot40pM : "bot40.csv")
# What you are expected to learn: quick ways to make sub-lists from lists, using csv writer
      
    