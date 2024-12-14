import fileinput
import math
import copy
import numpy as np

X=101
Y=103

grid = []

for line in fileinput.input(files="in.txt"):
    l = line[:-1].split(" ")
    p = list(map(int, l[0][2:].split(",")))
    v = list(map(int, l[1][2:].split(",")))
    grid.append([(p[0]+100*v[0])%X, (p[1]+100*v[1])%Y])

a = b = c = d = 0
for e in grid:
    if e[0]<math.floor(X/2) and e[1]<math.floor(Y/2):
        a +=1
    if e[0]<math.floor(X/2) and e[1]>math.floor(Y/2):
        b +=1
    if e[0]>math.floor(X/2) and e[1]<math.floor(Y/2):
        c +=1
    if e[0]>math.floor(X/2) and e[1]>math.floor(Y/2):
        d +=1

print(a,b,c,d)
print(a*b*c*d)