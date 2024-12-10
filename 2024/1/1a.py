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

for x,y in zip(l,r):
    # print(x)
    # print(int(x), int(y))
    # print(abs(int(x)-int(y)))
    t += abs(int(x)-int(y))


print(t)