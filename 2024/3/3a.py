import fileinput
import math
import re 

matches = []
for line in fileinput.input(files="in.txt"):
    matches.extend(list(re.findall("mul\(\d{1,3},\d{1,3}\)", line)))

s = 0
for e in matches:
    a = e[4:-1].split(",")
    print(a)
    s+= int(a[0])*int(a[1])

print(s)