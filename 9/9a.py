import fileinput
import math

num = []
s=0
for line in fileinput.input(files="in.txt"):
    num+="0"*int(line[0])
    for i in range(1, len(line), 2):
        num+="."*int(line[i])
        # print(int((i+1)/2), int(line[i]), int(line[i+1]))
        num.extend([int((i+1)/2)]*int(line[i+1]))
print(num)
while "." in num:
    if len(num)%100 ==0:
        print (len(num))
    num[num.index(".")] = num[-1]
    num = num[:-1]

for i in range(len(num)):
    s+=i*int(num[i])

print(num, s)