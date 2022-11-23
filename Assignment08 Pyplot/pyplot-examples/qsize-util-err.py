#!/usr/bin/python

import matplotlib.pyplot as plt
import csv, sys, re, random, os, time

datfile="qsize-util-err.txt"
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

QSizes = [1, 5, 10, 20]
qsize_col = map(lambda r: r[I['QSize']], M)
markers = {1: 's', 5: '^', 10: '.', 20: 'x'}

fig, y1 = plt.subplots()
y2 = plt.twinx()
lines = []

for qs in QSizes:
    qo_col_name = 'QO-Err' + str(qs)
    qo_col = map(lambda r: 100*float(r[I[qo_col_name]]), M)
    qo_label = 'QO: Err ' + str(qs) + '%'
    line, = y1.plot(qsize_col, qo_col, label=qo_label, ls='--', color='b', marker=markers[qs], markersize=9, mew=2, linewidth=2)
    lines.append(line)

    util_col_name = 'Util-Err' + str(qs)
    util_col = map(lambda r: 100*float(r[I[util_col_name]]), M)
    util_label = 'Util: Err ' + str(qs) + '%'
    line, = y2.plot(qsize_col, util_col, label=util_label, ls='-', color='r', marker=markers[qs], markersize=9, mew=2, linewidth=2)
    lines.append(line)

y1.set_xlabel('Queue size')
y1.set_ylabel('Queue overflow %')
y2.set_ylabel('Utilization %')
y1.yaxis.label.set_color('b')
y1.tick_params(axis='y', colors='b')
y2.yaxis.label.set_color('r')
y2.tick_params(axis='y', colors='r')
y1.axis(ymax=20)
y2.axis(ymin=60)
y1.grid(b='on')
y2.grid(b='on')
plt.legend(lines, [l.get_label() for l in lines], loc=(0.75,0.08), prop={'size':11})
plt.savefig("qsize-util-err.pdf", bbox_inches='tight')
#plt.show()
