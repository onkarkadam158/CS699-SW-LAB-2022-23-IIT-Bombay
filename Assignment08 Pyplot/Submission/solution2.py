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

