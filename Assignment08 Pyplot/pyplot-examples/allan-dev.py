#!/usr/bin/python

import matplotlib.pyplot as plt
import csv, sys, re, random, os, time

datfile="allan-dev.txt"
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

colors = { 'MeasuredAllanDev':'red', 'UniformAllanDev':'blue' }
markers = { 'MeasuredAllanDev':'x', 'UniformAllanDev':'+' }
lss = { 'MeasuredAllanDev':'-', 'UniformAllanDev':'--' }

avg_int_col = map(lambda r: r[I['AvgInt']], M)

for dat in ['MeasuredAllanDev', 'UniformAllanDev']:
    dat_col = map(lambda r: r[I[dat]], M)
    plt.plot(avg_int_col, dat_col, label=dat, ls=lss[dat], color=colors[dat], marker=markers[dat], markersize=9, mew=2, linewidth=2)

plt.xlabel('Averaging Interval (sec)')
plt.ylabel('Allan Deviation')
plt.grid(b='on')
plt.axis(ymin=0.001,ymax=1)
plt.loglog()
#fig, p1 = plt.subplots()
#p1.ticklabel_format(axis='both', style='plain')
from matplotlib.ticker import ScalarFormatter
axes = plt.gca()
axes.xaxis.set_major_formatter(ScalarFormatter())
axes.yaxis.set_major_formatter(ScalarFormatter())
axes.ticklabel_format(axis='both', style='plain')
plt.legend()
plt.savefig("allan-dev.pdf", bbox_inches='tight')
#plt.show()
