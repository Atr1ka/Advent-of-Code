import fileinput
import math

grid = []
for line in fileinput.input(files="in.txt"):
    grid.append(line[:-1])

def f(n, x, y, z):
    if n=="-1":
        return [[x,y,z]]
    out = []
    if x>0 and grid[x-1][y]==n:
        out.append([x-1,y])
    if y>0 and grid[x][y-1]==n:
        out.append([x,y-1])
    if x+1<len(grid) and grid[x+1][y]==n:
        out.append([x+1,y])
    if y+1<len(grid[0]) and grid[x][y+1]==n:
        out.append([x,y+1])
    o = []
    for e in out:
        o.extend(f(str(int(n)-1), e[0], e[1], z))
    return o

top = []
o = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]=="9":
            o.extend(f("8", i, j, [i,j]))

for e in top:
    o.extend(f("8", e[0], e[1], [e[0],e[1]]))
# print(o)
print(len(o)) # part b 
print(len(set(list(map(lambda x: (x[0], x[1], x[2][0], x[2][1]), o))))) # part a
