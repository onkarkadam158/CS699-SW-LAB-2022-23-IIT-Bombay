#!/usr/bin/python

import matplotlib.pyplot as plt
import csv, sys, re, random, os, time

datfile="roofnet-noise1.txt"
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

colors = { '5%-ile':'red', '95%-ile':'blue', 'Median (50%-ile)':'black' }
markers = { '5%-ile':'x', '95%-ile':'+', 'Median (50%-ile)':'o' }
lss = { '5%-ile':'-', '95%-ile':'--', 'Median (50%-ile)':'-.' }

plt.figure(figsize=(8,4))

for col in ['5%-ile','95%-ile', 'Median (50%-ile)']:
    val_col = map(lambda r: r[I[col]], M)
    plt.plot(val_col, label=col, ls=lss[col], color=colors[col], marker=markers[col], markersize=9, mew=2, linewidth=2)

plt.axis(ymax=-70)
plt.xlabel('Reading Number')
plt.ylabel('Silence Level (dBm)')
plt.grid(b='on')
plt.legend(loc=0,ncol=3)
#plt.legend(loc=0)
plt.savefig("roofnet-noise1.pdf", bbox_inches='tight')
#plt.show()
