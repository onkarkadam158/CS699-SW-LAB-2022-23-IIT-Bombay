#!/usr/bin/python

import csv, sys, re, random, os, time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math 

fig = plt.figure()
fig.set_figwidth(8)
fig.set_figheight(6)

matrix = []
cnt = 0
with open("pip-channel-hop.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        cnt = cnt + 1
        if( cnt > 1 ):
            # print(line.split(","))
            matrix.append((line.split(",")))

# print(matrix)

npmatrix = []
for row in matrix:
    tmprow = []
    i = 0
    for ele in row:
        if(i != 0):
            tmprow.append(float(ele))
        else:
            tmprow.append(ele)
        i = i+1
    npmatrix.append(tmprow)

# print(npmatrix)

withoutHopingX = []
withoutHopingY = []
for row in npmatrix:
    # if( row[1] != '' and row[1] != '\n'):
        withoutHopingX.append(row[0]) 
        withoutHopingY.append(row[1])
        # print(row[1])


withHopingX = []
withHopingY = []

for row in npmatrix:
    # if( row[2] != '' and row[2] != '\n'):
        withHopingX.append(row[0]) 
        withHopingY.append(row[2])
        # print(row[2])

withoutInterferenceX = []
withoutInterferenceY = []

for row in npmatrix:
    # if( row[4] != '' and row[4] != '\n'):
        withoutInterferenceX.append(row[0]) 
        withoutInterferenceY.append(row[3])
        # print(row[4])

plt.xlabel("WiFi inter-packet gap (ms)")  
plt.ylabel("Throughput (Kbps)")  

pkGap = np.arange(len(withHopingX))

x1 = plt.bar(pkGap, withoutHopingY, color = 'red',width= 0.30, edgecolor='black' )
x2 = plt.bar(pkGap+0.3, withHopingY, color = 'green',width= 0.30, edgecolor='black', hatch = '//')

x3 = plt.plot(withoutInterferenceX, withoutInterferenceY, color = 'blue', marker = 'x' , linestyle = 'dashed',markersize = 9,markeredgewidth = 2,linewidth = 2)

plt.xticks(pkGap + 0.5*0.3, withHopingX)
plt.legend((x1[0],x2[0],x3[0]) ,("Without-Hopping","With-Hopping","Without-Interference") , loc = (0.25, 0.70))
plt.show()
plt.grid()
ax = plt.gca()
ax.set_ylim(top=70)
plt.savefig("output3.png")

