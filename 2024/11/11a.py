import fileinput
import math

L = []
N = 45
t = "{"
for line in fileinput.input(files="in.txt"):
    L = list(map(int, line.split()))
print(L)
for _ in range(N):
    print(_)
    i=0
    L_n = []
    while i<len(L):
        # print(i, len(L))
        if L[i]==0:
            L_n.append(1)
        elif len(str(L[i]))%2 == 0:
            n = str(L[i])
            L_n.append(int(n[:int(len(n)/2)]))
            L_n.append(int(n[int(len(n)/2):]))
            # print("in", L)
            # i-=1
        else:
            L_n.append(2024*int(L[i]))
        i+=1
    L = L_n
    t+=str(_) + ": " + str(len(L)) + ", "
t = t[:-2] + "}"
print(t)
# print(len(L)) 