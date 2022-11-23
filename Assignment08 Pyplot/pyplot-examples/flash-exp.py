#!/usr/bin/python

import matplotlib.pyplot as plt
import csv, sys, re, random, os, time

########## Data reading section

datfile="flash-exp.txt"
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

########## Plot configuration section

colors = { 'ReadTime':'red', 'WriteTime':'blue', 'SyncTime':'black' }
markers = { 'ReadTime':'x', 'WriteTime':'+', 'SyncTime':'o' }
lss = { 'ReadTime':'-', 'WriteTime':'--', 'SyncTime':'-.' }

########## Plotting section

bytes_col = map(lambda r: r[I['NumBytes']], M)

for col in ['ReadTime','WriteTime', 'SyncTime']:
    latency_col = map(lambda r: r[I[col]], M)
    plt.plot(bytes_col, latency_col, label=col, ls=lss[col], color=colors[col], marker=markers[col], markersize=9, mew=2, linewidth=2)

plt.xlabel('Number of Bytes')
plt.ylabel('Latency (ticks)')
plt.grid(b='on')
plt.legend(loc=0)
#plt.show()
plt.savefig("flash-exp.pdf", bbox_inches='tight')
