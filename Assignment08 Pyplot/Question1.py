import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math 

fig = plt.figure()
fig.set_figwidth(10)
fig.set_figheight(8)

matrix = []
cnt = 0
with open("pip-latency-comparison.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        cnt = cnt + 1
        if( cnt > 1 ):
            # print(line.split(","))
            matrix.append((line.split(",")))

#print(matrix)

npmatrix = []

for row in matrix:
    tmprow = []
    for ele in row:
        if( ele != '' and ele != '\n'):
            tmprow.append(float(ele))
        else:
            tmprow.append(ele)
    npmatrix.append(tmprow)

# print(npmatrix)

PIPx = []
PIPy = []
for row in npmatrix:
    if( row[1] != '' and row[1] != '\n'):
        PIPx.append(row[0]) 
        PIPy.append(row[1])
        # print(row[1])


Flushx = []
Flushy = []

for row in npmatrix:
    if( row[2] != '' and row[2] != '\n'):
        Flushx.append(row[0]) 
        Flushy.append(row[2])
        # print(row[2])

PSFQx = []
PSFQy = []

for row in npmatrix:
    if( row[3] != '' and row[3] != '\n'):
        PSFQx.append(row[0]) 
        PSFQy.append(row[3])
        # print(row[3])

Fetchx = []
Fetchy = []

for row in npmatrix:
    if( row[4] != '' and row[4] != '\n'):
        Fetchx.append(row[0]) 
        Fetchy.append(row[4])
        # print(row[4])

plt.xlabel("Number of Hops")  
plt.ylabel("Latency (ms)")  
# color = ["red" , "blue" , "black","green"]
# marker = ["x","+","circle", "upper triangle"]
# linestyle = ["solid","dashed","dashdot","dotted"]
# markersize = 9 
# markeredgewidth = 2
# linewidht = 2

plt.plot(PIPx, PIPy, color = 'red', marker = 'x' , linestyle = 'solid',markersize = 9,markeredgewidth = 2,linewidth = 2)
plt.plot(Flushx, Flushy, color = 'blue', marker = '+' , linestyle = 'dashed',markersize = 9,markeredgewidth = 2,linewidth = 2)
plt.plot(PSFQx, PSFQy, color = 'black', marker = 'o' , linestyle = 'dashdot',markersize = 9,markeredgewidth = 2,linewidth = 2)
plt.plot(Fetchx, Fetchy, color = 'green', marker = '^' , linestyle = 'dotted',markersize = 9,markeredgewidth = 2,linewidth = 2)

plt.legend(["PIP","Flush","PSFQ","Fetch"] , loc ="best")
plt.show()
plt.grid()
plt.savefig("output1.png")



# Question 1 Problem Statement 

# Write a python code to plot a line graph using the data present in the file “pip-latency-comparison.txt”. 
# Note: Follow the below instructions when plotting the graph. Please do not do anything extra apart from the instructions mentioned below.


# 1. Set a figure size of 10,8
# 2. Plot the line graphs for the columns PIP, Flush, PSFQ, Fetch only in the mentioned order.
# 3. For the line graph corresponding to PIP use:
#    1. Color “red”
#    2. Marker “x”
#    3. Linestyle “solid”
# 4. For the line graph corresponding to Flush use:
#    1. Color “blue”
#    2. Marker “+”
#    3. Linestyle “dashed”
# 5. For the line graph corresponding to PSFQ use:
#    1. Color “black”
#    2. Marker circle
#    3. Linestyle “dashdot”
# 6. For the line graph corresponding to Fetch use:
#    1. Color “green”
#    2. Marker upper triangle
#    3. Linestyle “dotted”
# 7. Some common instructions for all three line graphs:
#    1. Make sure that the markersize is set to 9
#    2. Set the markeredgewidth to 2
#    3. Make sure that the line width is set to 2
#    4. Labels should be with the exact name as the corresponding column name.
# 8. The legend should be displayed using the “best” location
# 9. Labels for x,y should be: “Number of Hops” and “Latency (ms)”
# 10. Display the grid.
# 11. Code should save the figure as “output1.png”
# Note: Data contains NaN values as well. Each line should connect all its data points.



# Test Cases Input File Content

# hops,PIP,Flush,PSFQ,Fetch
# 1,7.245,37.62,46.46,94
# 2,7.245,47.85,92.93,
# 3,7.130,61.68,142.49,
# 4,7.105,65.54,185.86,
# 5,7.105,72.32,209.55,
# 6,7.086,80.67,232.33,409
# 7,7.086,87.39,,
# 8,7.086,,,
# 9,7.032,,,

