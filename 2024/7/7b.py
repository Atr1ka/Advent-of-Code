import fileinput
import math

targets = []
vals = []
s=0

for line in fileinput.input(files="in.txt"):
    l = line.split(": ")
    targets.append(int(l[0]))
    vals.append(list(map(int, l[1].split())))

def f(init, vals):
    if len(vals)==0:
        return init
    out = []
    for e in init:
        out.append(e*vals[0])
        out.append(e+vals[0])
        out.append(int(str(e)+str(vals[0])))
    return f(out,vals[1:])
    

for target, val in zip(targets, vals):
    if target in f(val[0:1], val[1:]):
        s+= target


print(s)