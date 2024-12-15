import fileinput
import math
import copy
import numpy as np

X=101
Y=103

ogrid = []
grid = []
act = []
for line in fileinput.input(files="in.txt"):
    if line[0]=="#":
        ogrid.append(list(line[:-1]))
    elif line[0]!="\r":
        act.extend(list(line[:-1]))

for i in range(len(ogrid)):
    arr = []
    for j in range(len(ogrid[0])):
        if ogrid[i][j]=="#":
            arr.extend(["#", "#"])
        if ogrid[i][j]=="O":
            arr.extend(["[", "]"])
        if ogrid[i][j]==".":
            arr.extend([".", "."])
        if ogrid[i][j]=="@":
            arr.extend(["@", "."])
    grid.append(arr)


def move(x,y,a):
    i = y
    j = x
    if a=="<":
        j-=1
    if a==">":
        j+=1
    if a=="^":
        i-=1
    if a=="v":
        i+=1
    # if (x==2 or x==3) and y==1:
    if grid[i][j]==".":
        # print(i,j)
        # print("before: ", grid[i][j])
        grid[i][j]=grid[y][x]
        # print("after:  ", grid[i][j])
        grid[y][x] = "."
        return (True, i, j)
    elif grid[i][j]=="#":
        return (False, i, j)
    elif grid[i][j]=="[" or grid[i][j]=="]":
        if a=="<" or a==">":
            m = move(j,i,a)
            if m[0]:
                grid[i][j]=grid[y][x]
                grid[y][x] = "."
                return (True, i, j)
            else:
                return (False, i, j)
        else:
            off = 0
            if grid[i][j]=="[":
                off=1
            if testMove(j-1+off,i,a) and testMove(j+off,i,a):
                move(j-1+off,i,a)
                move(j+off,i,a)
                grid[i][j]=grid[y][x]
                # grid[i][j-1+off]=grid[y][x-1+off]
                # grid[i][j+off]=grid[y][x+off]
                # grid[y][x] = "."
                grid[y][x] = "."
                # grid[y][x+off] = "."
                return (True, i, j)
            else:
                return (False, i, j)
                
def testMove(x,y,a):
    i = y
    j = x
    if a=="<":
        j-=1
    if a==">":
        j+=1
    if a=="^":
        i-=1
    if a=="v":
        i+=1
    # if (x==2 or x==3) and y==1:
    if grid[i][j]==".":
        return True
    elif grid[i][j]=="#":
        return False
    elif grid[i][j]=="[" or grid[i][j]=="]":
        if a=="<" or a==">":
            return testMove(j,i,a)
        else:
            off = 0
            if grid[i][j]=="[":
                off=1
            return testMove(j-1+off,i,a) and testMove(j+off,i,a)

# print(grid)
xi = yi = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]=="@":
            xi = j
            yi = i

# print(xi,yi)
for e in act:
    m = move(xi,yi,e)
    if m[0]:
        xi = m[2]
        yi = m[1]

    # print(xi,yi, "\n".join(list(map(str, grid))))

s=0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]=="[":
            s+=100*i + j

print(s)