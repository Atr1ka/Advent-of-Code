import fileinput
import math

grid = []
for line in fileinput.input(files="in.txt"):
    grid.append(line[:-1])

t=0
# print(grid)

for i in range(len(grid[0])): #vertical search
    for j in range(len(grid)-3):
        if grid[i][j]=="X" and grid[i][j+1]=="M" and grid[i][j+2]=="A" and grid[i][j+3]=="S" or \
            grid[i][j]=="S" and grid[i][j+1]=="A" and grid[i][j+2]=="M" and grid[i][j+3]=="X":
            t+=1

for i in range(len(grid[0])-3): #horizontal search
    for j in range(len(grid)):
        if grid[i][j]=="X" and grid[i+1][j]=="M" and grid[i+2][j]=="A" and grid[i+3][j]=="S" or \
            grid[i][j]=="S" and grid[i+1][j]=="A" and grid[i+2][j]=="M" and grid[i+3][j]=="X":
            t+=1

for i in range(len(grid[0])-3): #diagonal down-right
    for j in range(len(grid)-3):
        if grid[i][j]=="X" and grid[i+1][j+1]=="M" and grid[i+2][j+2]=="A" and grid[i+3][j+3]=="S" or \
            grid[i][j]=="S" and grid[i+1][j+1]=="A" and grid[i+2][j+2]=="M" and grid[i+3][j+3]=="X":
            t+=1

for i in map(lambda x: x+3, range(len(grid[0])-3)): #diagonal down-left
    for j in range(len(grid)-3):
        if grid[i][j]=="X" and grid[i-1][j+1]=="M" and grid[i-2][j+2]=="A" and grid[i-3][j+3]=="S" or \
            grid[i][j]=="S" and grid[i-1][j+1]=="A" and grid[i-2][j+2]=="M" and grid[i-3][j+3]=="X":
            t+=1

print(t)