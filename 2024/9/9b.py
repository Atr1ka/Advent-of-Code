import fileinput
import math
import copy
num = []
s=0
for line in fileinput.input(files="in.txt"):
    num.append([0,int(line[0]) , 0])
    for i in range(1, len(line), 2):
        num.append([".",int(line[i]), 0])
        # print(int((i+1)/2), int(line[i]), int(line[i+1]))
        num.append([int((i+1)/2),int(line[i+1]), 0])
# print(num)
a=3

while a>-1:
    if a%1000==0:
        print(a)
        a=0
    a+=1
    num = [x for x in num if x[1] != 0]
    i=0
    while i+1<len(num):
        if num[i][0]=="." and num[i+1][0]==".":
            num[i][1]+=num[i+1][1]
            del num[i+1]
        i+=1
    # a-=1
    # print(num)
    index = -1
    for i in range(len(num)-1, index, -1):
        # print(num[i])
        if num[i][0]!="." and num[i][2]==0 and num[i][1]!=0:
            # print("match")
            index = i
            break
    if index==-1:
        # print("fail")
        break
    # print(index)
    for i in range(0, index):
        # print(i, num[i], num[index][1])
        if num[i][0]=="." and num[i][1]>=num[index][1] and num[i][1]!=0:
            if index==8 or index==16:
                # print("index: ", index, num[index])
                # print("i    : ", i, num[i])
                print(num)
            # print("before: ", num[i])
            num[i][1]-=num[index][1]
            # print("after: ", num[i])
            x = copy.deepcopy(num[index])
            x[2]=1
            num[index][0]="."
            num.insert(i, x)
            break
    else:
        num[index][2]=1

print(num)

c=0
for e in num:
    if e[0]==".":
        for i in range(e[1]):
            print((c+i), "\t", e[0])
        c+=e[1]
        continue
    else:
        for i in range(e[1]):
            print((c+i), "\t", e[0])
            s+=(c+i)*e[0]
        c+=e[1]

print(s)