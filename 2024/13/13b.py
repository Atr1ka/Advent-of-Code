import fileinput
import math
import copy
import numpy as np

A = []
B = []
P = []
c=0
toVisit = set()
for e in fileinput.input(files="in.txt"):
    e = e[:-1].split(": ")
    # print(e)
    if e[0] == "Button A":
        # print(e[1].split(", "))
        A.append(list(map(int, list(map(lambda x:x[2:],e[1].split(", "))))))
    if e[0] == "Button B":
        B.append(list(map(int, list(map(lambda x:x[2:],e[1].split(", "))))))
    if e[0] == "Prize":
        P.append(list(map(int, list(map(lambda x:x[2:],e[1].split(", "))))))
# print(A,B,P)

for a,b,t in zip(A,B,P):
    # print(a,b)
    t = [t[0]+10000000000000, t[1]+10000000000000]
    m = np.matrix([[a[0], b[0]], [a[1], b[1]]])
    x = np.matrix(t)
    X = np.matmul(m.getI(), x.getT())
    X = [X.item(0), X.item(1)]
    # print(X)
    # print(int(X[0]), round(X[0], 4))
    # print(int(X[1]), round(X[1], 4))
    if float(round(X[0]))==round(X[0], 3) and float(round(X[1]))==round(X[1],3) and X[0]>=0 and X[1]>=0:
        c+=3*round(X[0])+round(X[1])
        # print("yess")
        # print(X)
    else:
        print(X)

print(c)