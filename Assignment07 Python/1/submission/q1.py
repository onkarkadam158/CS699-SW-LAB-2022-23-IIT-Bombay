#!bin/usr/python

import csv
import sys



if (len(sys.argv) != 2):
    print("Usage: q1.py <csv-file-name>")
    exit()
else:
    inputFile = sys.argv[1]
    count = 0 
    with open(inputFile , mode='r') as file:
        data = csv.reader(file)
        for lines in data:
            if(lines[0].isnumeric()):
                count = count+1
    print(count)






#         Python Exercises

# Python is excellent for text processing and functional programming, as we'll find out in the course of these exercises. Many exercises will use the following (imagined) context.

# The Job Interview

# Anaconda Systems was one of the companies which came for placement to IITB. Their selection process included five written tests followed by an interview. The written tests had up to 5 marks each. Students could decide not to attempt a written test, since if they get the written test totally wrong, they may get negative marks.

# The file marks.ods gives the spreadsheet of marks obtained by each of the candidates who appeared for selection. There are some heading rows in the spreadsheet. The first row before the actual data in the spreadsheet gives the column names which stand for the various written tests. In the cells, a "NA" means that the candidate did not attempt that particular written test (for fear of getting negative marks). The column named "Sel" tells whether the candidate was finally selected after the interview: this is a binary value (1=selected, 0=not selected).

# 1)

# Write a python script to read the csv file and print the total number of candidates who appeared for placement. Hint: You must look for a number (integer) as the first entry in a row, and count such rows to arrive at the answer. Your program should take exactly one command-line argument, the input csv file. If the wrong number of arguments are given, the program should exit after printing "Usage: q1.py <csv-file-name>" to specify correct usage of the program to the user.

# What you are expected to learn: command-line arguments, functions, if-then-else, loops, the csv module, regular expression matching