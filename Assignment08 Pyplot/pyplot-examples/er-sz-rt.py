#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import csv, sys, re, random, os, time

datfile="er-sz-rt.txt"
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

x_col = np.asarray(map(lambda r: int(r[I['x']]), M))

err100_col = map(lambda r: float(r[I['Err100']]), M)
err500_col = map(lambda r: float(r[I['Err500']]), M)
err1400_col = map(lambda r: float(r[I['Err1400']]), M)

rate_col = map(lambda r: r[I['rate']], M)

width = 0.24

plt.semilogy()

r1 = plt.bar(x_col, err100_col, width, color='r')
r2 = plt.bar(x_col+width, err500_col, width, color='w', hatch='/')
r3 = plt.bar(x_col+2*width, err1400_col, width, color='gray', hatch='\\')

plt.axis(xmin=-0.5, ymin=0.001, ymax=1)
#plt.xlabel(None)
plt.ylabel('Error rate')

from matplotlib.ticker import ScalarFormatter
axes = plt.gca()
axes.yaxis.set_major_formatter(ScalarFormatter())
axes.ticklabel_format(axis='y', style='plain')

plt.grid(b='on')
plt.xticks(x_col+1.5*width, rate_col)
plt.legend((r1[0], r2[0], r3[0]), ('100 bytes','500 bytes', '1400 bytes'), loc=0)
plt.text(1.5, 0.0005, 'SNR=13dB')
plt.text(1.5+5, 0.0005, 'SNR=8dB')
plt.text(1.5+10, 0.0005, 'SNR=3dB')
plt.text(1.5+15, 0.0005, 'SNR=2dB')
plt.savefig("er-sz-rt.pdf", bbox_inches='tight')
#plt.show()
