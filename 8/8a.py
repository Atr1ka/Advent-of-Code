import fileinput
import math

grid = []
for line in fileinput.input(files="in.txt"):
    grid.append(line[:-1])

X = len(grid[0])
Y = len(grid)

nodes = {}
ant = set()
for i in range(X):
    for j in range(Y):
        if grid[i][j] not in nodes:
            nodes[grid[i][j]] = [[i,j]]
        else:
            nodes[grid[i][j]].append([i,j])

del nodes["."]

for A in nodes.values():
    for e in A:
        for f in A:
            if e!=f:
                dx = f[0]-e[0]
                dy = f[1]-e[1]
                ant.add((e[0]-dx, e[1]-dy))
                ant.add((f[0]+dx, f[1]+dy))

filt = [e for e in ant if (e[0]>=0 and e[0]<X and e[1]>=0 and e[1]<Y)]
print(filt)
print(len(filt))