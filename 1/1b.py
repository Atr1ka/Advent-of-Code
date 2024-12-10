import fileinput
import math
l = []
r= []
for line in fileinput.input(files="in.txt"):
    lin = line.split()
    l.append(lin[0])
    r.append(lin[1])

t=0
l.sort()
r.sort()
m = {}
for y in r:
    if y not in m:
        m[y]=1
    else:
        m[y]+=1

for x in l:
    # print(x)
    # print(int(x), int(y))
    # print(abs(int(x)-int(y)))
    if x in m:
        t += abs(int(x)*int(m[x]))


print(t)