import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math 

fig = plt.figure()
fig.set_figwidth(10)
fig.set_figheight(6)

matrix = []
cnt = 0
with open("roofnet-noise11.txt", "r") as f:
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
i = 1
FiveileX = []
FiveileY = []
for row in npmatrix:
    # if( row[1] != '' and row[1] != '\n'):
        FiveileX.append(i)
        i = i + 1 
        FiveileY.append(row[0])
        # print(row[1])

i = 1
NinetyFiveileX = []
NinetyFiveileY = []

for row in npmatrix:
    # if( row[2] != '' and row[2] != '\n'):
        NinetyFiveileX.append(i)
        i = i + 1 
        NinetyFiveileY.append(row[1])
        # print(row[2])

MedianX = []
MedianY = []

for row in npmatrix:
    # if( row[3] != '' and row[3] != '\n'):
        MedianX.append(i)
        i = i + 1 
        MedianY.append(row[3])
        # print(row[3])


plt.xlabel("Reading Number")  
plt.ylabel("Silence Level (dBm)")  
# color = ["red" , "blue" , "black"]
# marker = ["x","+","circle"]
# linestyle = ["solid","dashed","dashdot"]
# markersize = 9 
# markeredgewidth = 2
# linewidht = 2

plt.plot( FiveileY, color = 'red', marker = 'x' , linestyle = 'solid',markersize = 9,markeredgewidth = 2,linewidth = 2)
plt.plot( NinetyFiveileY, color = 'blue', marker = '+' , linestyle = 'dashed',markersize = 9,markeredgewidth = 2,linewidth = 2)
plt.plot( MedianY, color = 'black', marker = 'o' , linestyle = 'dashdot',markersize = 9,markeredgewidth = 2,linewidth = 2)

a = plt.gca()
a.set_ylim(top=-70)

plt.legend(["5%-ile","95%-ile","Median (50%-ile)"] , loc ="best")
plt.show()
plt.grid()
plt.savefig("output2.png")



# Question2 Problem Statement

# Write a python code to plot a line graph using the data present in the file “roofnet-noise11.txt”. 
# Note: Follow the below instructions when plotting the graph. Please do not do anything extra apart from the instructions mentioned below.


# 1. Set a figure size of 10,6
# 2. Plot the line graphs for the columns 5%-ile, 95%-ile, Median (50%-ile) only in the mentioned order.
# 3. For the line graph corresponding to 5%-ile use:
#    1. Color “red”
#    2. Marker “x”
#    3. Linestyle “solid”
# 4. For the line graph corresponding to 95%-ile use:
#    1. Color “blue”
#    2. Marker “+”
#    3. Linestyle “dashed”
# 5. For the line graph corresponding to Median (50%-ile) use:
#    1. Color “black”
#    2. Marker circle
#    3. Linestyle “dashdot”
# 6. Some common instructions for all three line graphs:
#    1. Make sure that the markersize is set to 9
#    2. Set the markeredgewidth to 2
#    3. Make sure that the line width is set to 2
#    4. Labels should be with the exact name as the corresponding column name.
# 7. The max value for y-axis should be set to -70
# 8. The legend should be displayed using the “best” location
# 9. Labels for x,y should be: “Reading Number” and “Silence Level (dBm)”
# 10. Code should save the figure as “output2.png”
# 11. Display the grid.



# TestCase Input File:
# "5%-ile","95%-ile","band","Median (50%-ile)"
# -100,-99,1,-100
# -97,-84,13,-94
# -98,-90,8,-94
# -95,-89,6,-93
# -95,-89,6,-93
# -95,-84,11,-93
# -94,-89,5,-93
# -94,-87,7,-92
# -92,-87,5,-91
# -92,-87,5,-91
# -92,-85,7,-91
# -96,-80,16,-90
# -91,-86,5,-90
# -92,-84,8,-90
# -91,-87,4,-90
# -91,-84,7,-90
# -91,-86,5,-89
# -91,-83,8,-89
# -90,-84,6,-89
# -91,-85,6,-89
# -91,-85,6,-89
# -91,-84,7,-89
# -91,-85,6,-89
# -90,-85,5,-89
# -91,-81,10,-88
# -88,-81,7,-86

