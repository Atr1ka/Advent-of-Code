import fileinput
import math
import re 

matches = []
for line in fileinput.input(files="in.txt"):
    matches.extend(list(re.findall("(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", line)))

s = 0
on=1
for e in matches:
    if e=="don't()":
        on=0
    elif e=="do()":
        on=1
    else:
        a = e[4:-1].split(",")
        print(a)
        s+= int(a[0])*int(a[1])*on

print(s)