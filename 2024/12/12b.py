import fileinput
import math
import copy

grid = []
toVisit = set()
for line in fileinput.input(files="in.txt"):
    grid.append(list(line[:-1]))
# print(grid)


for i in range(len(grid)):
    for j in range(len(grid[0])):
        toVisit.add((i,j))
ogGrid = copy.deepcopy(toVisit)

def f(z):
    C = grid[z[0]][z[1]]
    a = 1
    iS = []
    jS = []
    temp = (z[0]-1, z[1])
    if temp in toVisit and grid[z[0]-1][z[1]]==C:
        toVisit.remove(temp)
        X = f(list(temp))
        a+=X[0]
        iS.extend(X[1])
        jS.extend(X[2])
        # iS.append(z)
    elif (temp not in ogGrid) or grid[z[0]-1][z[1]]!=C:
        iS.append([z[0], z[1], 0])
    
    temp = (z[0]+1, z[1])
    if temp in toVisit and grid[z[0]+1][z[1]]==C:
        toVisit.remove(temp)
        X = f(list(temp))
        a+=X[0]
        iS.extend(X[1])
        jS.extend(X[2])
        # iS.append([z[0]+1, z[1]])
    elif (temp not in ogGrid) or grid[z[0]+1][z[1]]!=C:
        iS.append([z[0]+1, z[1], 1])
    
    temp = (z[0], z[1]-1)
    if temp in toVisit and grid[z[0]][z[1]-1]==C:
        toVisit.remove(temp)
        X = f(list(temp))
        a+=X[0]
        iS.extend(X[1])
        jS.extend(X[2])
        # jS.append(z)
    elif (temp not in ogGrid) or grid[z[0]][z[1]-1]!=C:
        jS.append([z[0], z[1], 0])
    
    temp = (z[0], z[1]+1)
    if temp in toVisit and grid[z[0]][z[1]+1]==C:
        toVisit.remove(temp)
        X = f(list(temp))
        a+=X[0]
        iS.extend(X[1])
        jS.extend(X[2])
        # jS.append([z[0], z[1]+1])
    elif (temp not in ogGrid) or grid[z[0]][z[1]+1]!=C:
        jS.append([z[0], z[1]+1, 1])
    

    return a, iS, jS


c=0

while len(toVisit)>0:
    z = toVisit.pop()
    a,iS,jS = f(list(z))
    iS.sort()
    jS = list(map(lambda x: [x[1], x[0], x[2]], jS))
    jS.sort()
    s = 2
    si = 1
    sj = 1
    for i in range(1, len(iS)):
        if iS[i][0]!=iS[i-1][0] or iS[i][1]-iS[i-1][1]>1 or iS[i][2]!=iS[i-1][2]:
            si+=1
    for j in range(1, len(jS)):
        if jS[j][0]!=jS[j-1][0] or jS[j][1]-jS[j-1][1]>1 or jS[j][2]!=jS[j-1][2]:
            # print(jS[j])
            sj+=1

    # print(grid[z[0]][z[1]], a, si, sj)
    # print(iS)
    # print(jS)
    c += a * (si+sj)
    
print(c)
