#!bin/usr/python

import csv
import sys


if (len(sys.argv) != 2):
    print("Usage: q1.py <csv-file-name>" )
    exit()
else:
    inputFile = sys.argv[1]
    result = {}
    with open(inputFile , mode='r') as file:
        data = csv.reader(file)
        for line in data:
            if(line[0] == "Sno" ):
                for i in range(0,7):
                    result[line[i]]=i
    for item in result:
        print( item , result[item])


#         5)
# Now add to the previous program to make a "dictionary" or a "hashtable" which maps the column name to the column index. 
#To construct this index, you have to use the header row, which you can identify in the program as having "SNo" as the first column value. 
#The program should then loop through the dictionary to print each column name and corresponding index. Index starts at zero.
# What you are expected to learn: constructing and looping through dictionary or hashtable structures in python

# Example:
# Sno 0
# Math 1
# CS 2
# ..
# .
      