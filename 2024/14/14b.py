import fileinput
import math
import copy
import numpy as np
import time

# painful part b, tried checking manually thinking it'd be small and went through a few hundred timesteps before searching for 10 in a row vertically which worked

X=101
Y=103
A=10000
B=101*103

co = []

for line in fileinput.input(files="in.txt"):
    l = line[:-1].split(" ")
    p = list(map(int, l[0][2:].split(",")))
    v = list(map(int, l[1][2:].split(",")))
    co.append([p, v])

for t in range(1,B):
    at = set()
    T = False
    for a in range(len(co)):
        co[a] = [[(co[a][0][0]+co[a][1][0])%X, (co[a][0][1]+co[a][1][1])%Y], co[a][1]]
        at.add(tuple(co[a][0]))
    for i in range(X):
        for j in range(Y-10):
            if (i,j) in at and (i,j+1) in at and (i,j+2) in at and (i,j+3) in at and (i,j+4) in at and (i,j+5) in at and (i,j+6) in at and (i,j+7) in at and (i,j+8) in at and (i,j+9) in at and (i,j+10) in at:
                T=True

    if t>=A or T:
        for j in range(Y):
            for i in range(X):
                if (i,j) in at:
                    print("X", end="")
                else:
                    print(" ", end="")

            print()
        print("N = ", t)
        time.sleep(1)
        print("\n\n")