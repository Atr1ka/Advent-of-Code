import fileinput
import math
import copy
ogrid = []
xi=0
yi=0
pos = []

for line in fileinput.input(files="in.txt"):
    ogrid.append(line[:-1])

ogrid = list(map(lambda x:list(x), list(zip(*ogrid))))
for i in range(len(ogrid[0])):
    for j in range(len(ogrid)):
        if ogrid[i][j]=="^":
            xi=i
            yi=j

for i in range(len(ogrid[0])):
    for j in range(len(ogrid)):
        print(i,j)
        grid = copy.deepcopy(ogrid)
        if not (i==xi and j==yi): 
            grid[i][j]="#"
        x = xi
        y = yi
        places = set()
        pl = [str(x)+","+str(y)]
        facing = 0
        tr=True
        loop = True
        # print("new", i, j)
        while tr and loop:
            # print(places)
            # print(str(x)+","+str(y)+","+str(facing%4))
            if (str(x)+","+str(y)+","+str(facing%4)) in places:
                loop=False
                # print(i,j,x,y)
                break
            places.add(str(x)+","+str(y)+","+str(facing%4))
            pl.append(str(x)+","+str(y))
            if facing%4 == 0: #up
                # print(x, y, "up")
                if y==0:
                    tr=False
                    # print("trig up", x, y)
                elif grid[x][y-1]=="#":
                    # places.remove(str(x)+","+str(y)+","+str(facing%4))
                    # print("Test")
                    facing+=1
                else:
                    y-=1
            elif facing%4 == 1: #right
                # print(x, y, "right")
                if x==len(grid[0])-1:
                    tr=False
                    # print("trig right", x, y)
                elif grid[x+1][y]=="#":
                    # places.remove(str(x)+","+str(y)+","+str(facing%4))
                    facing+=1
                else:
                    x+=1
            elif facing%4 == 2: #down
                # print(x, y, "down")
                if y==len(grid)-1:
                    tr=False
                    # print("trig down", x, y)
                elif grid[x][y+1]=="#":
                    # places.remove(str(x)+","+str(y)+","+str(facing%4))
                    facing+=1
                else:
                    y+=1
            elif facing%4 == 3: #left
                # print(x, y, "left")
                if x==0:
                    tr=False
                    # print("trig left", x, y)
                elif grid[x-1][y]=="#":
                    # places.remove(str(x)+","+str(y)+","+str(facing%4))
                    facing+=1
                else:
                    x-=1
        if loop==False:
            pos.append(str(i)+","+str(j))
            # print(pl)
            # print(grid)


print(pos)
print(len(pos))