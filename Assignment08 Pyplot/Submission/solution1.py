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

