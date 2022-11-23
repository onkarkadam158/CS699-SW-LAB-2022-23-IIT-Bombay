#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import csv, sys, re, random, os, time

datfile="impl-loss-stats.txt"
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

nodeid_col = map(lambda r: r[I['NodeId']], M)
overflow_col = map(lambda r: 0.1*float(r[I['OverFlow']]), M)
retrylimit_col = map(lambda r: 0.1*float(r[I['RetryLimit']]), M)
temp = zip(overflow_col, retrylimit_col)
total_col = map(lambda tup: sum(tup), temp)

ind = np.arange(len(nodeid_col))
width = 0.20

r1 = plt.bar(ind, total_col, width, color='r')
r2 = plt.bar(ind+width, overflow_col, width, color='w', hatch='/')
r3 = plt.bar(ind+2*width, retrylimit_col, width, color='gray', hatch='\\')

plt.axis(xmin=-0.5)
plt.xlabel('Node Id')
plt.ylabel('Packet Drop (%)')
plt.grid(b='on')
plt.xticks(ind+1.5*width, nodeid_col)
plt.legend((r1[0], r2[0], r3[0]), ('Total','OverFlow', 'RetryLimit'), loc=0)
plt.savefig("impl-loss-stats.pdf", bbox_inches='tight')
#plt.show()
