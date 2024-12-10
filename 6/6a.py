import fileinput
import math

grid = []
x=0
y=0

for line in fileinput.input(files="in.txt"):
    grid.append(line[:-1])

grid = list(zip(*grid))
for i in range(len(grid[0])):
    for j in range(len(grid)):
        if grid[i][j]=="^":
            x=i
            y=j
# print (x,y)
places = set()
# pl = [str(x)+","+str(y)]
facing = 0
tr=True
while tr:
    places.add(str(x)+","+str(y))
    # pl.append(str(x)+","+str(y))
    if facing%4 == 0: #up
        if y==0:
            tr=False
        elif grid[x][y-1]=="#":
            facing+=1
        else:
            y-=1
    elif facing%4 == 1: #right
        if x==len(grid[0])-1:
            tr=False
        elif grid[x+1][y]=="#":
            facing+=1
        else:
            x+=1
    elif facing%4 == 2: #down
        if y==len(grid)-1:
            tr=False
        elif grid[x][y+1]=="#":
            facing+=1
        else:
            y+=1
    elif facing%4 == 3: #left
        if x==0:
            tr=False
        elif grid[x-1][y]=="#":
            facing+=1
        else:
            x-=1


# print(pl)
print(len(places))