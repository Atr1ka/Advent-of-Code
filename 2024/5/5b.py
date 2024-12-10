import fileinput
import math
import re

rules = {}
pages = []
wrong = []
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

def checkLine(line):
    for i in range(len(line)):
        if line[i] in rules:
            for e in rules[line[i]]:
                if e in line[:i]:
                    return [i, e]
    return [-1, e] #correct

for line in pages:
    if checkLine(line)[0]!=-1:
        wrong.append(line)
            
for line in wrong:
    while(checkLine(line)[0]!=-1):
        [index, el] = checkLine(line)
        for i in range(line[:index].count(el)):
            line.insert(index, line.pop(line.index(el)))
    print(line)
    t+=int(line[int(len(line)/2)])


print(t)