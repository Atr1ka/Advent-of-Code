import fileinput
import math
import copy

grid = []
toVisit = set()
for line in fileinput.input(files="in.txt"):
    grid.append(list(line[:-1]))
print(grid)


for i in range(len(grid)):
    for j in range(len(grid[0])):
        toVisit.add((i,j))
ogGrid = copy.deepcopy(toVisit)

def f(z):
    C = grid[z[0]][z[1]]
    a = 1
    p = 0
    temp = (z[0]-1, z[1])
    if temp in toVisit and grid[z[0]-1][z[1]]==C:
        toVisit.remove(temp)
        X = f(temp)
        a+=X[0]
        p+=X[1]
    elif (temp not in ogGrid) or grid[z[0]-1][z[1]]!=C:
        p+=1
    
    temp = (z[0]+1, z[1])
    if temp in toVisit and grid[z[0]+1][z[1]]==C:
        toVisit.remove(temp)
        X = f(temp)
        a+=X[0]
        p+=X[1]
    elif (temp not in ogGrid) or grid[z[0]+1][z[1]]!=C:
        p+=1
    
    temp = (z[0], z[1]-1)
    if temp in toVisit and grid[z[0]][z[1]-1]==C:
        toVisit.remove(temp)
        X = f(temp)
        a+=X[0]
        p+=X[1]
    elif (temp not in ogGrid) or grid[z[0]][z[1]-1]!=C:
        p+=1
    
    temp = (z[0], z[1]+1)
    if temp in toVisit and grid[z[0]][z[1]+1]==C:
        toVisit.remove(temp)
        X = f(temp)
        a+=X[0]
        p+=X[1]
    elif (temp not in ogGrid) or grid[z[0]][z[1]+1]!=C:
        p+=1
    

    return a, p


c=0

while len(toVisit)>0:
    z = toVisit.pop()
    a,p = f(z)
    # p = p/2 + len(grid)+len(grid[0])
    print(grid[z[0]][z[1]], a, p)
    c += a * p
    
print(c)
