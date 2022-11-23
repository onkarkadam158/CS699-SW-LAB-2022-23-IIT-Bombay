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









# Question 3 Problem Statement


# Write a python code to plot a graph using the data present in the file “pip-channel-hop.txt”. 
# Note: Follow the below instructions when plotting the graph. Please do not do anything extra apart from the instructions mentioned below.


# 1. Set a figure size of 8,6
# 2. Plot the bar graphs for the columns Without-Hopping and With-Hopping whereas a line graph for Without-Interference in the mentioned order.
# 3. Use the PktGap column as the x-axis.
# 4. For the bar graph corresponding to Without-Hopping use:
#    1. Color “red”
#    2. Width of “0.30”
#    3. Edge color “black”
# 5. For the bar graph corresponding to With-Hopping use:
#    1. Color “green”
#    2. Use width of “0.30”
#    3. Use hatch as “//”
#    4. Edge color “black”
# 6. For the line graph corresponding to Without-Interference use:
#    1. Color “blue”
#    2. Marker “x”
#    3. Linestyle “dashed”
#    4. Make sure that the markersize is set to 9
#    5. Set the markeredgewidth to 2
#    6. Make sure that the line width is set to 2
# 7. Labels should be with the exact name as the corresponding column name.
# 8. The max value for y-axis should be set to 70
# 9. The legend should be displayed at location (0.25, 0.70)
# 10. Labels for x,y should be: “WiFi inter-packet gap (ms)” and “Throughput (Kbps)”
# 11. Display the grid.
# 12. Code should save the figure as “output3.png”


# Note: Make sure the two bar columns are side by side with equal width and the x-ticks should be at the center of the two bars.


# Testcases input file

# PktGap,Without-Hopping,With-Hopping,Without-Interference
# Cafe,32.45,50.86,62.67
# Library,28.02,49.32,62.67
# 0.040,0.00,14.50,62.67
# 4,1.38,16.95,62.67
# 12,12.58,34.71,62.67
# 24,37.65,49.08,62.67
# 48,48.82,56.13,62.67
# 100,53.95,58.03,62.67
# 248,56.86,58.52,62.67

