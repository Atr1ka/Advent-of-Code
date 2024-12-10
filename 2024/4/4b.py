import fileinput
import math

grid = []
for line in fileinput.input(files="in.txt"):
    grid.append(line[:-1])

t=0
print(grid)

for i in range(len(grid[0])-2):
    for j in range(len(grid)-2):
        if grid[i+1][j+1]=="A" and (
            (grid[i][j]=="M" and grid[i+2][j+2]=="S" and grid[i+2][j]=="M" and grid[i][j+2]=="S" )  or \
            (grid[i][j]=="M" and grid[i+2][j+2]=="S" and grid[i+2][j]=="S" and grid[i][j+2]=="M" ) or \
            (grid[i][j]=="S" and grid[i+2][j+2]=="M" and grid[i+2][j]=="M" and grid[i][j+2]=="S" ) or \
            (grid[i][j]=="S" and grid[i+2][j+2]=="M" and grid[i+2][j]=="S" and grid[i][j+2]=="M" ) ):
            # print("\n".join(list(map(lambda x:x[j:j+3], grid[i:i+3]))))
            # print()
            t+=1
print(t)