import fileinput
import math

lines = []
for line in fileinput.input(files="in.txt"):
    lines.append(list(map(int, line.split())))

t = 0
for l in lines:
    s1=1
    s2=1
    for i in range(len(l)-1):
        if not (l[i]-l[i+1] > 0 and l[i]-l[i+1] < 4):
            s1=0
    for i in range(len(l)-1):
        if not (l[i+1]-l[i] > 0 and l[i+1]-l[i] < 4):
            s2=0
    if s1==1 or s2==1:
        t+=1

print(t)