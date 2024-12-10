import fileinput
import math

rules = {}
pages = []
for line in fileinput.input(files="in.txt"):
    if "|" in line:
        a = line[:-1].split("|")
        if a[0] not in rules:
            rules[a[0]] = [a[1]]
        else:   
            rules[a[0]].append(a[1])
    elif "," in line:
        pages.append(line[:-1].split(","))

t=0

for line in pages:
    w=1
    for i in range(len(line)):
        if w==1 and line[i] in rules:
            for e in rules[line[i]]:
                if e in line[:i]:
                    w=0
    t+=w*int(line[int(len(line)/2)])

print(t)