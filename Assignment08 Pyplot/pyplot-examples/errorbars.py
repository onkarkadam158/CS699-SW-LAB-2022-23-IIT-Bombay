#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import csv, sys, re, random, os, time

datfile="errorbars.txt"
Mcsv = csv.reader(open(datfile, 'rb'), delimiter=',', quotechar='"')

# Mapping from column name to column index
I = {}

# Matrix of all the rows
M = []

rowNum = 0
for row in Mcsv:
    rowNum += 1
    if (rowNum == 1):
        for i in range(len(row)):
            I[row[i]] = i
        continue
    else:
        M.append(row)

SupNum_col = map(lambda r: int(r[I['SupNum']]), M)
Wt_col = map(lambda r: float(r[I['Wt']]), M)
err_col = map(lambda r: float(r[I['Err']]), M)

#plt.plot(SupNum_col, Wt_col, label='Average over 10 sacks', ls='-', color='r', marker='^', markersize=9, mew=2, linewidth=2)
plt.errorbar(SupNum_col, Wt_col, yerr=err_col, label='Average over 10 sacks', ls='-', color='r', marker='^', markersize=9, mew=2, linewidth=2)

plt.xlabel('Supplier number')
plt.ylabel('Average weight of potato sack (kg)')
plt.grid(b='on')
plt.legend(loc=0)
plt.savefig("errorbars.pdf", bbox_inches='tight')
#plt.show()
