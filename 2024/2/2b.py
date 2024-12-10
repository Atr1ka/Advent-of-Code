import fileinput
import math

lines = []
for line in fileinput.input(files="in.txt"):
    lines.append(list(map(int, line.split())))

t = 0   

def test(l, c):
    # if c==0:
    #     print(l)
    s1=1
    s2=1
    for i in range(len(l)-1):
        if not (l[i]-l[i+1] > 0 and l[i]-l[i+1] < 4):
            s1=0
    for i in range(len(l)-1):
        if not (l[i+1]-l[i] > 0 and l[i+1]-l[i] < 4):
            s2=0

    if s1==1 or s2==1:
        return 1
    elif (c==1):
        for i in range(len(l)):
            t = l.copy() 
            del t[i]   
            if test(t, 0)==1:
                return 1
        return 0
    return 0

for l in lines:
    # print(test(l,1))
    t += test(l, 1)


print(t)


